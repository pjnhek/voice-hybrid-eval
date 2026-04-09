from types import SimpleNamespace

from voice_eval.bot_brain import generate_bot_response


def _make_client(mocker, response_text):
    response = SimpleNamespace(content=[SimpleNamespace(text=response_text)])
    client = mocker.Mock()
    client.messages.create.return_value = response
    return client


def test_generate_bot_response_returns_structured_dict(mocker):
    client = _make_client(
        mocker,
        '{"action": "ASK_ORDER_NUMBER", "utterance": "Could you share your order number?", "detected_intent": "Check order status"}',
    )

    result = generate_bot_response(
        client=client,
        user_input="Where is my package?",
        slots={},
        conversation_history=[],
    )

    assert result == {
        "action": "ASK_ORDER_NUMBER",
        "utterance": "Could you share your order number?",
        "detected_intent": "Check order status",
    }
    client.messages.create.assert_called_once()
    assert client.messages.create.call_args.kwargs["model"] == "claude-haiku-4-5"
    output_format = client.messages.create.call_args.kwargs["output_config"]["format"]
    assert output_format["type"] == "json_schema"
    assert "name" not in output_format
    schema = output_format["schema"]
    assert "detected_intent" in schema["properties"]
    assert "detected_intent" in schema["required"]


def test_generate_bot_response_passes_conversation_history_to_api(mocker):
    client = _make_client(
        mocker,
        '{"action": "PROVIDE_STATUS", "utterance": "Your order is on the way.", "detected_intent": "Check order status"}',
    )

    history = [
        {"user": "I need help with my order.", "bot": "Sure, what is your order number?"},
        {"user": "It is 12345.", "bot": "Thanks, let me check that."},
    ]

    generate_bot_response(
        client=client,
        user_input="Any update?",
        slots={"order_number": "12345"},
        conversation_history=history,
    )

    assert client.messages.create.call_args.kwargs["messages"] == [
        {"role": "user", "content": "I need help with my order."},
        {"role": "assistant", "content": "Sure, what is your order number?"},
        {"role": "user", "content": "It is 12345."},
        {"role": "assistant", "content": "Thanks, let me check that."},
        {"role": "user", "content": "Any update?"},
    ]


def test_generate_bot_response_includes_empty_slots_in_system_prompt(mocker):
    client = _make_client(
        mocker,
        '{"action": "ASK_EMAIL", "utterance": "What email is on the account?", "detected_intent": "Reset account password"}',
    )

    generate_bot_response(
        client=client,
        user_input="I forgot my password.",
        slots={},
        conversation_history=[],
    )

    system_prompt = client.messages.create.call_args.kwargs["system"]
    assert "No information extracted yet." in system_prompt
    assert "Your current task is:" not in system_prompt
    assert "must figure out what they need" in system_prompt


def test_generate_bot_response_includes_populated_slots_in_system_prompt(mocker):
    client = _make_client(
        mocker,
        '{"action": "CONFIRM_CANCELLATION", "utterance": "Order 12345 has been cancelled.", "detected_intent": "Cancel an order"}',
    )

    generate_bot_response(
        client=client,
        user_input="Please cancel order 12345.",
        slots={"order_number": "12345"},
        conversation_history=[],
    )

    system_prompt = client.messages.create.call_args.kwargs["system"]
    assert '"order_number": "12345"' in system_prompt


def test_generate_bot_response_system_prompt_lists_all_valid_intents(mocker):
    client = _make_client(
        mocker,
        '{"action": "ASK_CLARIFY", "utterance": "Could you tell me more?", "detected_intent": "Report a missing package"}',
    )

    generate_bot_response(
        client=client,
        user_input="My delivery never showed up.",
        slots={},
        conversation_history=[],
    )

    system_prompt = client.messages.create.call_args.kwargs["system"]
    for intent in [
        "Return a damaged item",
        "Request refund for duplicate charge",
        "Change shipping address",
        "Cancel an order",
        "Check order status",
        "Reset account password",
        "Report a missing package",
        "Upgrade subscription plan",
    ]:
        assert f'"{intent}"' in system_prompt


def test_generate_bot_response_skips_missing_bot_history_entries(mocker):
    client = _make_client(
        mocker,
        '{"action": "ASK_CLARIFY", "utterance": "Can you tell me more?", "detected_intent": "Check order status"}',
    )

    generate_bot_response(
        client=client,
        user_input="Can you help?",
        slots={},
        conversation_history=[{"user": "hello"}],
    )

    assert client.messages.create.call_args.kwargs["messages"] == [
        {"role": "user", "content": "hello"},
        {"role": "user", "content": "Can you help?"},
    ]
