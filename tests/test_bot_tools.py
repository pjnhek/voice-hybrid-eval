import pytest

from voice_eval.bot_tools import (
    extract_slots_tool,
    generate_response_tool,
    policy_decision_tool,
)


def test_extract_slots_tool_extracts_order_number():
    result = extract_slots_tool("My order 12345 is delayed.", {})

    assert result.success is True
    assert result.data["order_number"] == "12345"


def test_extract_slots_tool_normalizes_order_number_with_commas():
    result = extract_slots_tool("I need help with order 12,345.", {})

    assert result.success is True
    assert result.data["order_number"] == "12345"


def test_extract_slots_tool_extracts_card_ending():
    result = extract_slots_tool("It was on my card ending 1234.", {})

    assert result.success is True
    assert result.data["card_info"] == "1234"


def test_extract_slots_tool_extracts_email_address():
    result = extract_slots_tool(
        "Please send it to jennifer.walsh@gmail.com as soon as possible.",
        {},
    )

    assert result.success is True
    assert result.data["email"] == "jennifer.walsh@gmail.com"


def test_extract_slots_tool_extracts_account_number():
    result = extract_slots_tool("My account number is AB1234.", {})

    assert result.success is True
    assert result.data["account_number"] == "AB1234"


def test_extract_slots_tool_preserves_existing_slots():
    current_slots = {"customer_id": "abc", "order_number": "11111"}

    result = extract_slots_tool("No new details yet.", current_slots)

    assert result.success is True
    assert result.data == current_slots


def test_policy_decision_tool_requests_order_number_when_missing():
    result = policy_decision_tool("Change shipping address", "help", {})

    assert result.success is True
    assert result.data == {"action": "ASK_ORDER_NUMBER"}


def test_policy_decision_tool_confirms_return_when_order_number_present():
    result = policy_decision_tool(
        "Return a damaged item",
        "I want to return it.",
        {"order_number": "12345"},
    )

    assert result.success is True
    assert result.data == {"action": "CONFIRM_RETURN"}


def test_policy_decision_tool_processes_refund_when_card_info_present():
    result = policy_decision_tool(
        "Request refund for duplicate charge",
        "Refund me.",
        {"card_info": "1234"},
    )

    assert result.success is True
    assert result.data == {"action": "PROCESS_REFUND"}


@pytest.mark.parametrize(
    ("goal", "slots", "expected_action"),
    [
        ("Cancel an order", {"order_number": "12345"}, "CONFIRM_CANCELLATION"),
        ("Cancel an order", {}, "ASK_ORDER_NUMBER"),
        ("Check order status", {"order_number": "12345"}, "PROVIDE_STATUS"),
        ("Check order status", {}, "ASK_ORDER_NUMBER"),
        ("Reset account password", {"email": "user@example.com"}, "SEND_RESET_LINK"),
        ("Reset account password", {}, "ASK_EMAIL"),
        ("Report a missing package", {"order_number": "12345"}, "OPEN_INVESTIGATION"),
        ("Report a missing package", {}, "ASK_ORDER_NUMBER"),
        ("Upgrade subscription plan", {"account_number": "AB1234"}, "CONFIRM_UPGRADE"),
        ("Upgrade subscription plan", {}, "ASK_ACCOUNT_NUMBER"),
    ],
)
def test_policy_decision_tool_handles_new_goals(goal, slots, expected_action):
    result = policy_decision_tool(goal, "help", slots)

    assert result.success is True
    assert result.data == {"action": expected_action}


def test_generate_response_tool_uses_action_template():
    result = generate_response_tool("CONFIRM_ADDRESS_CHANGE", {"order_number": "12345"})

    assert result.success is True
    assert result.data["action"] == "CONFIRM_ADDRESS_CHANGE"
    assert "updated your shipping address" in result.data["utterance"].lower()
    assert "12345" in result.data["utterance"]


@pytest.mark.parametrize(
    ("action", "slots", "expected_text"),
    [
        ("CONFIRM_CANCELLATION", {"order_number": "12345"}, "12345"),
        ("PROVIDE_STATUS", {"order_number": "12345"}, "currently being processed"),
        ("SEND_RESET_LINK", {"email": "user@example.com"}, "user@example.com"),
        ("OPEN_INVESTIGATION", {"order_number": "12345"}, "opened an investigation"),
        ("CONFIRM_UPGRADE", {"account_number": "AB1234"}, "AB1234"),
        ("ASK_EMAIL", {}, "email address associated with your account"),
        ("ASK_ACCOUNT_NUMBER", {}, "provide your account number"),
    ],
)
def test_generate_response_tool_supports_new_actions(action, slots, expected_text):
    result = generate_response_tool(action, slots)

    assert result.success is True
    assert result.data["action"] == action
    assert expected_text in result.data["utterance"]
