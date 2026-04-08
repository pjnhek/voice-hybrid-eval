from pathlib import Path

from voice_eval.bot_tools import ToolResult
from voice_eval.scenario import Scenario, Step
from voice_eval.simulator import run_scenario


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

    def fake_generate_bot_response(goal, user_input, slots, conversation_history):
        captured_histories.append([dict(entry) for entry in conversation_history])
        if not conversation_history:
            return {
                "action": "ASK_ORDER_NUMBER",
                "utterance": "Could you please share your order number?",
            }

        return {
            "action": "PROVIDE_STATUS",
            "utterance": "Order 12345 is on the way.",
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
    assert result["transcript"][0]["action"] == "ASK_ORDER_NUMBER"
    assert result["transcript"][1]["action"] == "PROVIDE_STATUS"
    assert result["transcript"][1]["slots"] == {"order_number": "12345"}
