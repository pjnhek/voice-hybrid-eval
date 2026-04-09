from types import SimpleNamespace

import pytest

from voice_eval.bot_brain import generate_bot_response


def _make_response(response_text):
    return SimpleNamespace(content=[SimpleNamespace(text=response_text)])


def _make_client(mocker, responses):
    client = mocker.Mock()
    side_effects = []
    for response in responses:
        if isinstance(response, Exception):
            side_effects.append(response)
        else:
            side_effects.append(_make_response(response))
    client.messages.create.side_effect = side_effects
    return client


def test_generate_bot_response_returns_structured_dict_and_makes_two_calls(mocker):
    client = _make_client(
        mocker,
        [
            '{"detected_intent": "Check order status"}',
            '{"action": "ASK_ORDER_NUMBER", "utterance": "Could you share your order number?"}',
        ],
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
    assert client.messages.create.call_count == 2
    assert client.messages.create.call_args_list[0].kwargs["model"] == "claude-haiku-4-5"
    assert client.messages.create.call_args_list[1].kwargs["model"] == "claude-haiku-4-5"


def test_generate_bot_response_passes_conversation_history_to_both_api_calls(mocker):
    client = _make_client(
        mocker,
        [
            '{"detected_intent": "Check order status"}',
            '{"action": "PROVIDE_STATUS", "utterance": "Your order is on the way."}',
        ],
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

    expected_messages = [
        {"role": "user", "content": "I need help with my order."},
        {"role": "assistant", "content": "Sure, what is your order number?"},
        {"role": "user", "content": "It is 12345."},
        {"role": "assistant", "content": "Thanks, let me check that."},
        {"role": "user", "content": "Any update?"},
    ]
    assert client.messages.create.call_args_list[0].kwargs["messages"] == expected_messages
    assert client.messages.create.call_args_list[1].kwargs["messages"] == expected_messages


def test_first_call_uses_eight_intent_enum_schema(mocker):
    client = _make_client(
        mocker,
        [
            '{"detected_intent": "Report a missing package"}',
            '{"action": "ASK_ORDER_NUMBER", "utterance": "Which order is missing?"}',
        ],
    )

    generate_bot_response(
        client=client,
        user_input="My delivery never showed up.",
        slots={},
        conversation_history=[],
    )

    first_call = client.messages.create.call_args_list[0].kwargs
    output_format = first_call["output_config"]["format"]
    assert output_format["type"] == "json_schema"
    schema = output_format["schema"]
    assert schema["required"] == ["detected_intent"]
    assert schema["properties"]["detected_intent"]["enum"] == [
        "Return a damaged item",
        "Request refund for duplicate charge",
        "Change shipping address",
        "Cancel an order",
        "Check order status",
        "Reset account password",
        "Report a missing package",
        "Upgrade subscription plan",
    ]
    assert "No information extracted yet." in first_call["system"]


def test_cancel_order_second_call_only_allows_cancel_actions(mocker):
    client = _make_client(
        mocker,
        [
            '{"detected_intent": "Cancel an order"}',
            '{"action": "CONFIRM_CANCELLATION", "utterance": "Order 12345 has been cancelled."}',
        ],
    )

    generate_bot_response(
        client=client,
        user_input="Please cancel order 12345.",
        slots={"order_number": "12345"},
        conversation_history=[],
    )

    second_call = client.messages.create.call_args_list[1].kwargs
    schema = second_call["output_config"]["format"]["schema"]
    assert schema["properties"]["action"]["enum"] == [
        "ASK_ORDER_NUMBER",
        "CONFIRM_CANCELLATION",
    ]
    assert '"order_number": "12345"' in second_call["system"]
    assert 'The customer\'s intent has already been detected as: "Cancel an order"' in second_call["system"]
    assert 'Include "cancelled" or "canceled".' in second_call["system"]


@pytest.mark.parametrize(
    ("intent", "slots", "expected_actions"),
    [
        (
            "Request refund for duplicate charge",
            {"card_info": "4829"},
            ["ASK_CARD_INFO", "PROCESS_REFUND"],
        ),
        (
            "Reset account password",
            {"email": "user@example.com"},
            ["ASK_EMAIL", "SEND_RESET_LINK"],
        ),
        (
            "Upgrade subscription plan",
            {"account_number": "80421"},
            ["ASK_ACCOUNT_NUMBER", "CONFIRM_UPGRADE"],
        ),
    ],
)
def test_second_call_only_allows_actions_valid_for_detected_intent(
    mocker,
    intent,
    slots,
    expected_actions,
):
    client = _make_client(
        mocker,
        [
            json_for_intent(intent),
            '{"action": "%s", "utterance": "ok"}' % expected_actions[0],
        ],
    )

    generate_bot_response(
        client=client,
        user_input="Can you help?",
        slots=slots,
        conversation_history=[],
    )

    second_call = client.messages.create.call_args_list[1].kwargs
    schema = second_call["output_config"]["format"]["schema"]
    assert schema["properties"]["action"]["enum"] == expected_actions


def test_intent_detection_prompt_lists_all_valid_intents(mocker):
    client = _make_client(
        mocker,
        [
            '{"detected_intent": "Report a missing package"}',
            '{"action": "ASK_ORDER_NUMBER", "utterance": "Which order is missing?"}',
        ],
    )

    generate_bot_response(
        client=client,
        user_input="My delivery never showed up.",
        slots={},
        conversation_history=[],
    )

    system_prompt = client.messages.create.call_args_list[0].kwargs["system"]
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
        [
            '{"detected_intent": "Check order status"}',
            '{"action": "ASK_ORDER_NUMBER", "utterance": "Can you tell me your order number?"}',
        ],
    )

    generate_bot_response(
        client=client,
        user_input="Can you help?",
        slots={},
        conversation_history=[{"user": "hello"}],
    )

    expected_messages = [
        {"role": "user", "content": "hello"},
        {"role": "user", "content": "Can you help?"},
    ]
    assert client.messages.create.call_args_list[0].kwargs["messages"] == expected_messages
    assert client.messages.create.call_args_list[1].kwargs["messages"] == expected_messages


def test_generate_bot_response_preserves_detected_intent_when_action_call_fails(mocker):
    client = _make_client(
        mocker,
        [
            '{"detected_intent": "Reset account password"}',
            RuntimeError("second call failed"),
        ],
    )

    result = generate_bot_response(
        client=client,
        user_input="I forgot my password.",
        slots={},
        conversation_history=[],
    )

    assert result == {
        "action": "ASK_CLARIFY",
        "utterance": "I'm sorry, I encountered an error. Could you please try again?",
        "detected_intent": "Reset account password",
    }
    assert client.messages.create.call_count == 2


def json_for_intent(intent):
    return '{"detected_intent": "%s"}' % intent
