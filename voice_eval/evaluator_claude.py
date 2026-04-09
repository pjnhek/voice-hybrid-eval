import json
from typing import Any, Dict

from anthropic import Anthropic


_CLAUDE_EVALUATION_SCHEMA = {
    "type": "object",
    "properties": {
        "pass": {"type": "boolean"},
        "reason": {"type": "string"},
    },
    "required": ["pass", "reason"],
    "additionalProperties": False,
}


def check_bot_expect_claude(bot_text: str, expect: Dict[str, Any]) -> bool:
    """Use Claude structured outputs to semantically evaluate a bot response."""
    if not expect:
        return True

    client = Anthropic()
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=256,
        messages=[
            {
                "role": "user",
                "content": _create_claude_evaluation_prompt(bot_text, expect),
            }
        ],
        output_config={
            "format": {
                "type": "json_schema",
                "schema": _CLAUDE_EVALUATION_SCHEMA,
            }
        },
    )

    result = json.loads(response.content[0].text)
    return bool(result["pass"])


def _create_claude_evaluation_prompt(bot_text: str, expect: Dict[str, Any]) -> str:
    return f"""You are grading a customer-support bot reply for a voice evaluation.

Bot reply:
{bot_text}

Expectation:
{json.dumps(expect, indent=2)}

Judge whether the reply satisfies the expectation using semantic understanding, not just exact substring matching.
- Treat paraphrases, equivalent wording, and clearly implied fulfillment as passing.
- If the expectation uses "contains", decide whether the bot meaningfully covers that phrase or idea.
- If the expectation uses "contains_any", pass when the reply meaningfully covers at least one listed phrase or idea.
- If the reply misses the requested idea, fail.
- Return only the JSON object defined by the schema.
"""
