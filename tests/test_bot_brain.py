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
        '{"action": "ASK_ORDER_NUMBER", "utterance": "Could you share your order number?"}',
    )

    result = generate_bot_response(
        client=client,
        goal="Check order status",
        user_input="Where is my package?",
        slots={},
        conversation_history=[],
    )

    assert result == {
        "action": "ASK_ORDER_NUMBER",
        "utterance": "Could you share your order number?",
    }
    client.messages.create.assert_called_once()
    assert client.messages.create.call_args.kwargs["model"] == "claude-haiku-4-5"


def test_generate_bot_response_passes_conversation_history_to_api(mocker):
    client = _make_client(
        mocker,
        '{"action": "PROVIDE_STATUS", "utterance": "Your order is on the way."}',
    )

    history = [
        {"user": "I need help with my order.", "bot": "Sure, what is your order number?"},
        {"user": "It is 12345.", "bot": "Thanks, let me check that."},
    ]

    generate_bot_response(
        client=client,
        goal="Check order status",
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
        '{"action": "ASK_EMAIL", "utterance": "What email is on the account?"}',
    )

    generate_bot_response(
        client=client,
        goal="Reset account password",
        user_input="I forgot my password.",
        slots={},
        conversation_history=[],
    )

    system_prompt = client.messages.create.call_args.kwargs["system"]
    assert "Reset account password" in system_prompt
    assert "No information extracted yet." in system_prompt


def test_generate_bot_response_includes_populated_slots_in_system_prompt(mocker):
    client = _make_client(
        mocker,
        '{"action": "CONFIRM_CANCELLATION", "utterance": "Order 12345 has been cancelled."}',
    )

    generate_bot_response(
        client=client,
        goal="Cancel an order",
        user_input="Please cancel order 12345.",
        slots={"order_number": "12345"},
        conversation_history=[],
    )

    system_prompt = client.messages.create.call_args.kwargs["system"]
    assert '"order_number": "12345"' in system_prompt
    assert "Cancel an order" in system_prompt


def test_generate_bot_response_skips_missing_bot_history_entries(mocker):
    client = _make_client(
        mocker,
        '{"action": "ASK_CLARIFY", "utterance": "Can you tell me more?"}',
    )

    generate_bot_response(
        client=client,
        goal="General support",
        user_input="Can you help?",
        slots={},
        conversation_history=[{"user": "hello"}],
    )

    assert client.messages.create.call_args.kwargs["messages"] == [
        {"role": "user", "content": "hello"},
        {"role": "user", "content": "Can you help?"},
    ]
