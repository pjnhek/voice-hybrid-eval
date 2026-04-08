# Rule-based bot tools for voice evaluation
import re
from typing import Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class ToolResult:
    success: bool
    data: Any
    error: Optional[str] = None


def extract_slots_tool(user_input: str, current_slots: Dict[str, Any]) -> ToolResult:
    """Extract supported slots from user input."""
    try:
        slots = dict(current_slots)
        user_lower = user_input.lower()

        if m := re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", user_input):
            slots["email"] = m.group(0)

        if "account" in user_lower:
            account_patterns = [
                r"\baccount\s+number\s+is\s+([A-Za-z0-9]{5,8})\b",
                r"\bmy\s+account\s+number\s+is\s+([A-Za-z0-9]{5,8})\b",
                r"\bmy\s+account\s+is\s+([A-Za-z0-9]{5,8})\b",
                r"\baccount\s+is\s+([A-Za-z0-9]{5,8})\b",
                r"\baccount\s+([A-Za-z0-9]{5,8})\b",
            ]

            for pattern in account_patterns:
                if m := re.search(pattern, user_input, re.IGNORECASE):
                    slots["account_number"] = m.group(1)
                    break

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

        if goal == "Cancel an order":
            if "order_number" in available_slots:
                return ToolResult(success=True, data={"action": "CONFIRM_CANCELLATION"})
            return ToolResult(success=True, data={"action": "ASK_ORDER_NUMBER"})

        if goal == "Check order status":
            if "order_number" in available_slots:
                return ToolResult(success=True, data={"action": "PROVIDE_STATUS"})
            return ToolResult(success=True, data={"action": "ASK_ORDER_NUMBER"})

        if goal == "Reset account password":
            if "email" in available_slots:
                return ToolResult(success=True, data={"action": "SEND_RESET_LINK"})
            return ToolResult(success=True, data={"action": "ASK_EMAIL"})

        if goal == "Report a missing package":
            if "order_number" in available_slots:
                return ToolResult(success=True, data={"action": "OPEN_INVESTIGATION"})
            return ToolResult(success=True, data={"action": "ASK_ORDER_NUMBER"})

        if goal == "Upgrade subscription plan":
            if "account_number" in available_slots:
                return ToolResult(success=True, data={"action": "CONFIRM_UPGRADE"})
            return ToolResult(success=True, data={"action": "ASK_ACCOUNT_NUMBER"})

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
            "CONFIRM_CANCELLATION": f"Your order {slots.get('order_number', 'that order')} has been cancelled. You will receive a confirmation email shortly.",
            "PROVIDE_STATUS": f"Order {slots.get('order_number', 'that order')} is currently being processed and is expected to arrive within 3-5 business days.",
            "SEND_RESET_LINK": f"I've sent a password reset link to {slots.get('email', 'your email address')}. Please check your inbox and spam folder.",
            "OPEN_INVESTIGATION": f"I've opened an investigation for order {slots.get('order_number', 'that order')}. Our team will look into the missing package and follow up within 24-48 hours.",
            "CONFIRM_UPGRADE": f"Your subscription has been upgraded. The changes to account {slots.get('account_number', 'your account')} will take effect immediately.",
            "ASK_ORDER_NUMBER": "I can help you with that. Could you please provide your order number?",
            "ASK_CARD_INFO": "I can help you with that. Could you please provide the last four digits of your card?",
            "ASK_EMAIL": "I can help you with that. Could you please provide the email address associated with your account?",
            "ASK_ACCOUNT_NUMBER": "I can help you with that. Could you please provide your account number?",
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
