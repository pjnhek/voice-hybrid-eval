# Markdown report generation for evaluation results
from pathlib import Path


def write_markdown_report(results: list[dict], out_path: Path) -> None:
    """Write markdown report for evaluation results."""
    # Ensure parent directories exist
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        # H1: "Hybrid Voice Eval Report"
        f.write("# Hybrid Voice Eval Report\n\n")

        # Summary table: Scenario | Result | Steps Passed
        f.write("## Summary\n\n")
        total = len(results)
        intent_correct = sum(1 for result in results if result["intent_detected"])
        accuracy = (100 * intent_correct // total) if total else 0
        f.write(f"**Intent Detection Accuracy:** {intent_correct}/{total} ({accuracy}%)\n\n")
        f.write("| Scenario | Intent | Result | Steps Passed |\n")
        f.write("|----------|--------|--------|--------------|\n")

        for result in results:
            status = "✅ PASS" if result["scenario_pass"] else "❌ FAIL"
            intent = "✅" if result["intent_detected"] else "❌"
            first = (
                f" (turn {result['first_correct_turn']})"
                if result["first_correct_turn"] is not None
                else ""
            )
            f.write(
                f"| {result['scenario_id']} | {intent}{first} | {status} | "
                f"{result['steps_passed']}/{result['steps_expected']} |\n"
            )

        f.write("\n")

        # For each scenario
        for result in results:
            # H2 with scenario_id and goal
            f.write(f"## {result['scenario_id']}: {result['goal']}\n\n")

            # For each turn
            for turn in result["transcript"]:
                # Show ✅/❌, user_text, user_asr, bot_text
                status_icon = "✅" if turn["pass"] else "❌"
                f.write(f"### Turn {turn['turn']} {status_icon}\n\n")

                f.write(f"**User Text:** {turn['user_text']}\n\n")
                f.write(f"**User ASR:** {turn['user_asr']}\n\n")
                f.write(f"**Bot Text:** {turn['bot_text']}\n\n")

                detected_intent = turn.get("detected_intent") or "(missing)"
                if turn["intent_correct"]:
                    f.write(f"**Detected Intent:** {detected_intent} ✅\n\n")
                else:
                    f.write(
                        f"**Detected Intent:** {detected_intent} ❌ "
                        f"(expected: {turn['expected_intent']})\n\n"
                    )

                # Show links (relative paths) to user_wav and bot_wav
                f.write(f"**Audio Files:**\n")
                f.write(f"- User: [{turn['user_wav']}]({turn['user_wav']})\n")
                f.write(f"- Bot: [{turn['bot_wav']}]({turn['bot_wav']})\n\n")

                # Show Expected (dict) if present
                if turn["expectation"]:
                    f.write(f"**Expected:** {turn['expectation']}\n\n")

                f.write("---\n\n")
