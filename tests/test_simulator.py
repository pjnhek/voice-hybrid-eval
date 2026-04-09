from pathlib import Path

from voice_eval.bot_tools import ToolResult
from voice_eval.scenario import Scenario, Step
from voice_eval.simulator import _find_real_audio, _scenario_has_recordings, run_directory, run_scenario


def test_run_scenario_uses_extract_slots_and_tracks_conversation_history(mocker, tmp_path):
    scenario = Scenario(
        id="check_order_status_001",
        goal="Check order status",
        steps=[
            Step(user="Where is my order?", bot_expect={"contains": "order number"}),
            Step(user="It's order 12345.", bot_expect={"contains": "on the way"}),
        ],
        acceptance={},
    )

    client = mocker.sentinel.client
    mocker.patch("voice_eval.simulator.Anthropic", return_value=client)
    mocker.patch("voice_eval.simulator.synthesize")
    mocker.patch(
        "voice_eval.simulator.transcribe",
        side_effect=["Where is my order?", "It's order 12345."],
    )

    tool_client = mocker.Mock()
    tool_client.call_tool.side_effect = [
        ToolResult(success=True, data={}),
        ToolResult(success=True, data={"order_number": "12345"}),
    ]
    mocker.patch("voice_eval.simulator.ToolClient", return_value=tool_client)

    captured_histories = []
    captured_clients = []

    def fake_generate_bot_response(client, user_input, slots, conversation_history):
        captured_clients.append(client)
        captured_histories.append([dict(entry) for entry in conversation_history])
        if not conversation_history:
            return {
                "action": "ASK_ORDER_NUMBER",
                "utterance": "Could you please share your order number?",
                "detected_intent": "Check order status",
            }

        return {
            "action": "PROVIDE_STATUS",
            "utterance": "Order 12345 is on the way.",
            "detected_intent": "Check order status",
        }

    mocker.patch(
        "voice_eval.simulator.generate_bot_response",
        side_effect=fake_generate_bot_response,
    )
    mocker.patch("voice_eval.simulator.check_bot_expect_enhanced", return_value=True)

    result = run_scenario(scenario, Path(tmp_path), model_size="tiny", judge="rules")

    assert tool_client.call_tool.call_args_list == [
        mocker.call(
            "extract_slots",
            {"user_input": "Where is my order?", "current_slots": {}},
        ),
        mocker.call(
            "extract_slots",
            {"user_input": "It's order 12345.", "current_slots": {}},
        ),
    ]
    assert captured_histories == [
        [],
        [{"user": "Where is my order?", "bot": "Could you please share your order number?"}],
    ]
    assert captured_clients == [client, client]
    assert result["transcript"][0]["action"] == "ASK_ORDER_NUMBER"
    assert result["transcript"][1]["action"] == "PROVIDE_STATUS"
    assert result["transcript"][1]["slots"] == {"order_number": "12345"}
    assert result["transcript"][0]["detected_intent"] == "Check order status"
    assert result["transcript"][0]["expected_intent"] == "Check order status"
    assert result["transcript"][0]["intent_correct"] is True
    assert result["intent_detected"] is True
    assert result["first_correct_turn"] == 1


def test_run_scenario_marks_turn_failed_when_generate_bot_response_raises(mocker, tmp_path):
    scenario = Scenario(
        id="bot_error_001",
        goal="Check order status",
        steps=[Step(user="Where is my order?", bot_expect={"contains": "order number"})],
        acceptance={},
    )

    mocker.patch("voice_eval.simulator.Anthropic", return_value=mocker.sentinel.client)
    mocker.patch("voice_eval.simulator.synthesize")
    mocker.patch(
        "voice_eval.simulator.transcribe",
        return_value="Where is my order?",
    )

    tool_client = mocker.Mock()
    tool_client.call_tool.return_value = ToolResult(success=True, data={})
    mocker.patch("voice_eval.simulator.ToolClient", return_value=tool_client)

    mocker.patch(
        "voice_eval.simulator.generate_bot_response",
        side_effect=RuntimeError("claude unavailable"),
    )
    evaluator = mocker.patch("voice_eval.simulator.check_bot_expect_enhanced", return_value=True)

    result = run_scenario(scenario, Path(tmp_path), model_size="tiny", judge="rules")

    assert result["transcript"][0]["pass"] is False
    assert "claude unavailable" in result["transcript"][0]["error"]
    assert result["transcript"][0]["detected_intent"] == ""
    assert result["transcript"][0]["intent_correct"] is False
    assert result["intent_detected"] is False
    assert result["first_correct_turn"] is None
    evaluator.assert_not_called()


def test_run_scenario_preserves_slots_after_extraction_failure_on_next_turn(mocker, tmp_path):
    scenario = Scenario(
        id="slot_failure_001",
        goal="Check order status",
        steps=[
            Step(user="My order is 12345.", bot_expect=None),
            Step(user="Still waiting.", bot_expect=None),
            Step(user="Can you check again?", bot_expect={"contains": "12345"}),
        ],
        acceptance={},
    )

    mocker.patch("voice_eval.simulator.Anthropic", return_value=mocker.sentinel.client)
    mocker.patch("voice_eval.simulator.synthesize")
    mocker.patch(
        "voice_eval.simulator.transcribe",
        side_effect=[
            "My order is 12345.",
            "Still waiting.",
            "Can you check again?",
        ],
    )

    tool_client = mocker.Mock()
    tool_client.call_tool.side_effect = [
        ToolResult(success=True, data={"order_number": "12345"}),
        ToolResult(success=False, data=None, error="extract failed"),
        ToolResult(success=True, data={"order_number": "12345"}),
    ]
    mocker.patch("voice_eval.simulator.ToolClient", return_value=tool_client)

    mocker.patch(
        "voice_eval.simulator.generate_bot_response",
        side_effect=[
            {
                "action": "PROVIDE_STATUS",
                "utterance": "I found order 12345.",
                "detected_intent": "Check order status",
            },
            {
                "action": "PROVIDE_STATUS",
                "utterance": "I still have order 12345.",
                "detected_intent": "Check order status",
            },
            {
                "action": "PROVIDE_STATUS",
                "utterance": "Order 12345 is still processing.",
                "detected_intent": "Check order status",
            },
        ],
    )
    mocker.patch("voice_eval.simulator.check_bot_expect_enhanced", return_value=True)

    run_scenario(scenario, Path(tmp_path), model_size="tiny", judge="rules")

    assert tool_client.call_tool.call_args_list[2] == mocker.call(
        "extract_slots",
        {
            "user_input": "Can you check again?",
            "current_slots": {"order_number": "12345"},
        },
    )


def test_run_scenario_uses_claude_judge_when_requested(mocker, tmp_path):
    scenario = Scenario(
        id="judge_claude_001",
        goal="Check order status",
        steps=[Step(user="Where is my order?", bot_expect={"contains": "status"})],
        acceptance={},
    )

    mocker.patch("voice_eval.simulator.Anthropic", return_value=mocker.sentinel.client)
    mocker.patch("voice_eval.simulator.synthesize")
    mocker.patch(
        "voice_eval.simulator.transcribe",
        return_value="Where is my order?",
    )

    tool_client = mocker.Mock()
    tool_client.call_tool.return_value = ToolResult(success=True, data={})
    mocker.patch("voice_eval.simulator.ToolClient", return_value=tool_client)

    mocker.patch(
        "voice_eval.simulator.generate_bot_response",
        return_value={
            "action": "PROVIDE_STATUS",
            "utterance": "Your order status is pending.",
            "detected_intent": "Check order status",
        },
    )
    claude_evaluator = mocker.patch(
        "voice_eval.simulator.check_bot_expect_claude",
        return_value=True,
    )
    rules_evaluator = mocker.patch(
        "voice_eval.simulator.check_bot_expect_enhanced",
        return_value=False,
    )

    run_scenario(scenario, Path(tmp_path), model_size="tiny", judge="claude")

    claude_evaluator.assert_called_once_with(
        "Your order status is pending.",
        {"contains": "status"},
    )
    rules_evaluator.assert_not_called()


def test_run_scenario_counts_only_steps_with_expectations(mocker, tmp_path):
    scenario = Scenario(
        id="expectation_count_001",
        goal="Check order status",
        steps=[
            Step(user="Hello there.", bot_expect=None),
            Step(user="Where is my order?", bot_expect={"contains": "order number"}),
        ],
        acceptance={},
    )

    mocker.patch("voice_eval.simulator.Anthropic", return_value=mocker.sentinel.client)
    mocker.patch("voice_eval.simulator.synthesize")
    mocker.patch(
        "voice_eval.simulator.transcribe",
        side_effect=["Hello there.", "Where is my order?"],
    )

    tool_client = mocker.Mock()
    tool_client.call_tool.side_effect = [
        ToolResult(success=True, data={}),
        ToolResult(success=True, data={}),
    ]
    mocker.patch("voice_eval.simulator.ToolClient", return_value=tool_client)

    mocker.patch(
        "voice_eval.simulator.generate_bot_response",
        side_effect=[
            {
                "action": "ASK_CLARIFY",
                "utterance": "How can I help?",
                "detected_intent": "Check order status",
            },
            {
                "action": "ASK_ORDER_NUMBER",
                "utterance": "Please share your order number.",
                "detected_intent": "Check order status",
            },
        ],
    )
    mocker.patch("voice_eval.simulator.check_bot_expect_enhanced", return_value=True)

    result = run_scenario(scenario, Path(tmp_path), model_size="tiny", judge="rules")

    assert result["steps_expected"] == 1
    assert result["steps_passed"] == 1
    assert result["scenario_pass"] is True


def test_run_scenario_uses_last_turn_for_intent_detected_and_tracks_first_correct_turn(mocker, tmp_path):
    scenario = Scenario(
        id="intent_tracking_001",
        goal="Check order status",
        steps=[
            Step(user="I need help.", bot_expect=None),
            Step(user="It's about order 12345.", bot_expect=None),
            Step(user="Actually, where is it now?", bot_expect={"contains": "pending"}),
        ],
        acceptance={},
    )

    mocker.patch("voice_eval.simulator.Anthropic", return_value=mocker.sentinel.client)
    mocker.patch("voice_eval.simulator.synthesize")
    mocker.patch(
        "voice_eval.simulator.transcribe",
        side_effect=[
            "I need help.",
            "It's about order 12345.",
            "Actually, where is it now?",
        ],
    )

    tool_client = mocker.Mock()
    tool_client.call_tool.side_effect = [
        ToolResult(success=True, data={}),
        ToolResult(success=True, data={"order_number": "12345"}),
        ToolResult(success=True, data={"order_number": "12345"}),
    ]
    mocker.patch("voice_eval.simulator.ToolClient", return_value=tool_client)
    mocker.patch(
        "voice_eval.simulator.generate_bot_response",
        side_effect=[
            {
                "action": "ASK_CLARIFY",
                "utterance": "Can you tell me more?",
                "detected_intent": "Cancel an order",
            },
            {
                "action": "ASK_ORDER_NUMBER",
                "utterance": "Thanks, I can check that order.",
                "detected_intent": "Check order status",
            },
            {
                "action": "PROVIDE_STATUS",
                "utterance": "Your order is pending.",
                "detected_intent": "Cancel an order",
            },
        ],
    )
    mocker.patch("voice_eval.simulator.check_bot_expect_enhanced", return_value=True)

    result = run_scenario(scenario, Path(tmp_path), model_size="tiny", judge="rules")

    assert [entry["intent_correct"] for entry in result["transcript"]] == [False, True, False]
    assert result["intent_detected"] is False
    assert result["first_correct_turn"] == 2


def test_find_real_audio_prefers_higher_priority_extension(tmp_path):
    scenario_dir = tmp_path / "check_order_status_001"
    scenario_dir.mkdir()
    wav_path = scenario_dir / "user_1.wav"
    m4a_path = scenario_dir / "user_1.m4a"
    wav_path.write_text("wav")
    m4a_path.write_text("m4a")

    result = _find_real_audio(tmp_path, "check_order_status_001", 1)

    assert result == str(wav_path)


def test_run_scenario_uses_real_audio_without_synthesizing_user_turn(mocker, tmp_path):
    scenario = Scenario(
        id="check_order_status_001",
        goal="Check order status",
        steps=[Step(user="Where is my order?", bot_expect={"contains": "status"})],
        acceptance={},
    )
    real_audio_dir = tmp_path / "real-audio"
    real_audio_path = real_audio_dir / scenario.id / "user_1.mp3"
    real_audio_path.parent.mkdir(parents=True)
    real_audio_path.write_text("audio")

    mocker.patch("voice_eval.simulator.Anthropic", return_value=mocker.sentinel.client)
    synthesize = mocker.patch("voice_eval.simulator.synthesize")
    transcribe = mocker.patch(
        "voice_eval.simulator.transcribe",
        return_value="Where is my order?",
    )

    tool_client = mocker.Mock()
    tool_client.call_tool.return_value = ToolResult(success=True, data={})
    mocker.patch("voice_eval.simulator.ToolClient", return_value=tool_client)
    mocker.patch(
        "voice_eval.simulator.generate_bot_response",
        return_value={
            "action": "PROVIDE_STATUS",
            "utterance": "Your order is pending.",
            "detected_intent": "Check order status",
        },
    )
    mocker.patch("voice_eval.simulator.check_bot_expect_enhanced", return_value=True)

    result = run_scenario(
        scenario,
        Path(tmp_path),
        model_size="tiny",
        judge="rules",
        real_audio_dir=real_audio_dir,
    )

    synthesize.assert_called_once_with(
        "Your order is pending.",
        f"{tmp_path}/{scenario.id}/bot_1.wav",
    )
    transcribe.assert_called_once_with(str(real_audio_path), model_size="tiny")
    assert result["transcript"][0]["user_wav"] == str(real_audio_path)


def test_run_scenario_falls_back_to_tts_when_real_audio_is_missing(mocker, tmp_path):
    scenario = Scenario(
        id="check_order_status_001",
        goal="Check order status",
        steps=[Step(user="Where is my order?", bot_expect={"contains": "status"})],
        acceptance={},
    )
    real_audio_dir = tmp_path / "real-audio"

    mocker.patch("voice_eval.simulator.Anthropic", return_value=mocker.sentinel.client)
    synthesize = mocker.patch("voice_eval.simulator.synthesize")
    transcribe = mocker.patch(
        "voice_eval.simulator.transcribe",
        return_value="Where is my order?",
    )

    tool_client = mocker.Mock()
    tool_client.call_tool.return_value = ToolResult(success=True, data={})
    mocker.patch("voice_eval.simulator.ToolClient", return_value=tool_client)
    mocker.patch(
        "voice_eval.simulator.generate_bot_response",
        return_value={
            "action": "PROVIDE_STATUS",
            "utterance": "Your order is pending.",
            "detected_intent": "Check order status",
        },
    )
    mocker.patch("voice_eval.simulator.check_bot_expect_enhanced", return_value=True)

    run_scenario(
        scenario,
        Path(tmp_path),
        model_size="tiny",
        judge="rules",
        real_audio_dir=real_audio_dir,
    )

    synthesize.assert_any_call(
        "Where is my order?",
        f"{tmp_path}/{scenario.id}/user_1.wav",
    )
    synthesize.assert_any_call(
        "Your order is pending.",
        f"{tmp_path}/{scenario.id}/bot_1.wav",
    )
    transcribe.assert_called_once_with(
        f"{tmp_path}/{scenario.id}/user_1.wav",
        model_size="tiny",
    )


def test_run_directory_passes_real_audio_dir_through(mocker, tmp_path):
    scenario = Scenario(
        id="check_order_status_001",
        goal="Check order status",
        steps=[],
        acceptance={},
    )

    mocker.patch("voice_eval.simulator.load_scenarios", return_value=[scenario])
    run_scenario_mock = mocker.patch(
        "voice_eval.simulator.run_scenario",
        return_value={"scenario_id": scenario.id},
    )
    real_audio_dir = tmp_path / "real-audio"

    result = run_directory(
        tmp_path / "scenarios",
        tmp_path / "audio",
        model_size="base",
        judge="claude",
        real_audio_dir=real_audio_dir,
    )

    assert result == [{"scenario_id": scenario.id}]
    run_scenario_mock.assert_called_once_with(
        scenario,
        tmp_path / "audio",
        "base",
        "claude",
        real_audio_dir=real_audio_dir,
    )


def test_run_directory_real_audio_only_skips_scenarios_without_recordings(mocker, tmp_path):
    has_audio = Scenario(id="cancel_order_004", goal="Cancel an order", steps=[], acceptance={})
    no_audio = Scenario(id="cancel_order_005", goal="Cancel an order", steps=[], acceptance={})

    mocker.patch("voice_eval.simulator.load_scenarios", return_value=[has_audio, no_audio])
    run_scenario_mock = mocker.patch(
        "voice_eval.simulator.run_scenario",
        return_value={"scenario_id": has_audio.id},
    )

    real_audio_dir = tmp_path / "recordings"
    audio_dir = real_audio_dir / has_audio.id
    audio_dir.mkdir(parents=True)
    (audio_dir / "user_1.m4a").write_text("audio")

    result = run_directory(
        tmp_path / "scenarios",
        tmp_path / "audio",
        real_audio_dir=real_audio_dir,
        real_audio_only=True,
    )

    assert len(result) == 1
    run_scenario_mock.assert_called_once_with(
        has_audio,
        tmp_path / "audio",
        "tiny",
        "rules",
        real_audio_dir=real_audio_dir,
    )


def test_run_directory_real_audio_only_false_runs_all_scenarios(mocker, tmp_path):
    s1 = Scenario(id="cancel_order_004", goal="Cancel an order", steps=[], acceptance={})
    s2 = Scenario(id="cancel_order_005", goal="Cancel an order", steps=[], acceptance={})

    mocker.patch("voice_eval.simulator.load_scenarios", return_value=[s1, s2])
    run_scenario_mock = mocker.patch(
        "voice_eval.simulator.run_scenario",
        side_effect=[{"scenario_id": s1.id}, {"scenario_id": s2.id}],
    )

    real_audio_dir = tmp_path / "recordings"
    audio_dir = real_audio_dir / s1.id
    audio_dir.mkdir(parents=True)
    (audio_dir / "user_1.m4a").write_text("audio")

    result = run_directory(
        tmp_path / "scenarios",
        tmp_path / "audio",
        real_audio_dir=real_audio_dir,
        real_audio_only=False,
    )

    assert len(result) == 2
    assert run_scenario_mock.call_count == 2
