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
    },
    "required": ["action", "utterance"],
    "additionalProperties": False,
}


def generate_bot_response(
    client: Anthropic,
    goal: str,
    user_input: str,
    slots: Dict[str, Any],
    conversation_history: List[HistoryEntry],
) -> Dict[str, Any]:
    """Use Claude to decide the next action and generate a response."""
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=256,
        system=_create_system_prompt(goal, slots),
        messages=_build_messages(conversation_history, user_input),
        output_config={
            "format": {
                "type": "json_schema",
                "name": "bot_response",
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


def _create_system_prompt(goal: str, slots: Dict[str, Any]) -> str:
    extracted_info = (
        json.dumps(slots, indent=2, sort_keys=True)
        if slots
        else "No information extracted yet."
    )

    return f"""You are a customer service bot. Your current task is: {goal}

You have access to the following extracted information from the conversation:
{extracted_info}

Based on the conversation so far, decide what to do next and respond naturally.

Rules:
- If you need information from the customer (order number, card info, email, account number), ask for it politely.
- If you have enough information to fulfill the request, confirm the action and provide details.
- Be concise and professional. One to two sentences max.
- Do NOT make up order numbers, tracking info, or other specific data not in the extracted slots.
- When confirming an action, reference the specific information the customer provided (e.g., the order number).

Valid actions: ASK_ORDER_NUMBER, ASK_CARD_INFO, ASK_EMAIL, ASK_ACCOUNT_NUMBER, ASK_CLARIFY,
CONFIRM_RETURN, CONFIRM_ADDRESS_CHANGE, CONFIRM_CANCELLATION, PROCESS_REFUND,
PROVIDE_STATUS, SEND_RESET_LINK, OPEN_INVESTIGATION, CONFIRM_UPGRADE"""
