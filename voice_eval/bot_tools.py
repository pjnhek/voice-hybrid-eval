# Rule-based bot tools for voice evaluation
import re
from typing import Dict, Any
from dataclasses import dataclass


@dataclass
class ToolResult:
    success: bool
    data: Any
    error: str = None


def extract_slots_tool(user_input: str, current_slots: Dict[str, Any]) -> ToolResult:
    """Extract order numbers and card info from user input."""
    try:
        slots = dict(current_slots)
        user_lower = user_input.lower()

        if "order" in user_lower:
            order_patterns = [
                r"order\s+number\s+is\s+(\d+)\b",
                r"my\s+order\s+number\s+is\s+(\d+)\b",
                r"order\s+(\d{1,3}(?:,\d{3})+(?:-\d+)?)\b",
                r"order\s+#?(\d+)\b",
            ]

            for pattern in order_patterns:
                if m := re.search(pattern, user_lower):
                    slots["order_number"] = m.group(1).replace(",", "")
                    break

        if "card ending" in user_lower:
            card_patterns = [
                r"card\s+ending\s+(\d{1,3}(?:,\d{3})+)\b",
                r"card\s+ending\s+(\d{4})\b",
            ]

            for pattern in card_patterns:
                if m := re.search(pattern, user_lower):
                    slots["card_info"] = m.group(1).replace(",", "")
                    break

        return ToolResult(success=True, data=slots)

    except Exception as e:
        return ToolResult(success=False, data=current_slots, error=str(e))


def policy_decision_tool(goal: str, user_input: str, available_slots: Dict[str, Any]) -> ToolResult:
    """Determine the appropriate action based on goal and available information."""
    try:
        if goal == "Change shipping address":
            if "order_number" in available_slots:
                return ToolResult(success=True, data={"action": "CONFIRM_ADDRESS_CHANGE"})
            return ToolResult(success=True, data={"action": "ASK_ORDER_NUMBER"})

        if goal == "Return a damaged item":
            if "order_number" in available_slots:
                return ToolResult(success=True, data={"action": "CONFIRM_RETURN"})
            return ToolResult(success=True, data={"action": "ASK_ORDER_NUMBER"})

        if goal == "Request refund for duplicate charge":
            if "card_info" in available_slots:
                return ToolResult(success=True, data={"action": "PROCESS_REFUND"})
            return ToolResult(success=True, data={"action": "ASK_CARD_INFO"})

        return ToolResult(success=True, data={"action": "ASK_CLARIFY"})

    except Exception as e:
        return ToolResult(success=False, data={"action": "ASK_CLARIFY"}, error=str(e))


def generate_response_tool(action: str, slots: Dict[str, Any]) -> ToolResult:
    """Generate the bot response text for a tool action."""
    try:
        responses = {
            "CONFIRM_ADDRESS_CHANGE": f"Thank you! I have updated your shipping address for order {slots.get('order_number', 'that order')}. The change has been confirmed.",
            "CONFIRM_RETURN": f"Thank you! I have initiated the return for order {slots.get('order_number', 'that order')}. I've emailed you a return label and you should receive it shortly.",
            "PROCESS_REFUND": f"Thank you! I have processed your refund for the duplicate charge ending in {slots.get('card_info', 'your card')}. You should see the credit within 3-5 business days.",
            "ASK_ORDER_NUMBER": "I can help you with that. Could you please provide your order number?",
            "ASK_CARD_INFO": "I can help you with that. Could you please provide the last four digits of your card?",
            "ASK_CLARIFY": "I'm not sure I understand. Could you please clarify what you'd like help with?"
        }

        utterance = responses.get(action, "I'm not sure how to help with that.")

        return ToolResult(success=True, data={
            "action": action,
            "utterance": utterance,
        })

    except Exception as e:
        return ToolResult(success=False, data={
            "action": "ASK_CLARIFY",
            "utterance": "I'm sorry, I encountered an error. Could you please try again?",
        }, error=str(e))
