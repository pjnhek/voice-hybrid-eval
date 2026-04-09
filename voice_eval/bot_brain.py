"""LLM-powered bot brain using Claude for policy decisions and response generation."""

import json
from typing import Any, Dict, List, NotRequired, TypedDict

from anthropic import Anthropic


class HistoryEntry(TypedDict):
    user: str
    bot: NotRequired[str]


_BOT_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "action": {"type": "string"},
        "utterance": {"type": "string"},
        "detected_intent": {"type": "string"},
    },
    "required": ["action", "utterance", "detected_intent"],
    "additionalProperties": False,
}


def generate_bot_response(
    client: Anthropic,
    user_input: str,
    slots: Dict[str, Any],
    conversation_history: List[HistoryEntry],
) -> Dict[str, Any]:
    """Use Claude to decide the next action and generate a response."""
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=256,
        system=_create_system_prompt(slots),
        messages=_build_messages(conversation_history, user_input),
        output_config={
            "format": {
                "type": "json_schema",
                "schema": _BOT_RESPONSE_SCHEMA,
            }
        },
    )

    return json.loads(response.content[0].text)


def _build_messages(
    conversation_history: List[HistoryEntry],
    user_input: str,
) -> List[Dict[str, str]]:
    messages: List[Dict[str, str]] = []
    for entry in conversation_history:
        messages.append({"role": "user", "content": entry["user"]})
        if entry.get("bot"):
            messages.append({"role": "assistant", "content": entry["bot"]})

    messages.append({"role": "user", "content": user_input})
    return messages


def _create_system_prompt(slots: Dict[str, Any]) -> str:
    extracted_info = (
        json.dumps(slots, indent=2, sort_keys=True)
        if slots
        else "No information extracted yet."
    )

    return f"""You are a customer service bot for a retail company. The customer is calling in and you must figure out what they need, then help them.

You have access to the following extracted information from the conversation:
{extracted_info}

For every response, you must:
1. Determine what the customer's intent is based on everything they've said so far.
2. Decide the next action to take.
3. Respond naturally to the customer.

Rules:
- If you need information from the customer (order number, card info, email, account number), ask for it politely.
- If you have enough information to fulfill the request, confirm the action and provide details.
- Be concise and professional. One to two sentences max.
- Do NOT make up order numbers, tracking info, or other specific data not in the extracted slots.
- When confirming an action, reference the specific information the customer provided.

Your detected_intent must be one of these exact strings:
- "Return a damaged item"
- "Request refund for duplicate charge"
- "Change shipping address"
- "Cancel an order"
- "Check order status"
- "Reset account password"
- "Report a missing package"
- "Upgrade subscription plan"

Valid actions: ASK_ORDER_NUMBER, ASK_CARD_INFO, ASK_EMAIL, ASK_ACCOUNT_NUMBER, ASK_CLARIFY,
CONFIRM_RETURN, CONFIRM_ADDRESS_CHANGE, CONFIRM_CANCELLATION, PROCESS_REFUND,
PROVIDE_STATUS, SEND_RESET_LINK, OPEN_INVESTIGATION, CONFIRM_UPGRADE"""
