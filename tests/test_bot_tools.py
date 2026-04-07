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


def test_generate_response_tool_uses_action_template():
    result = generate_response_tool("CONFIRM_ADDRESS_CHANGE", {"order_number": "12345"})

    assert result.success is True
    assert result.data["action"] == "CONFIRM_ADDRESS_CHANGE"
    assert "updated your shipping address" in result.data["utterance"].lower()
    assert "12345" in result.data["utterance"]
