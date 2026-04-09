from voice_eval.reporters.markdown import write_markdown_report


def test_write_markdown_report_includes_intent_accuracy_summary(tmp_path):
    out_path = tmp_path / "report.md"

    write_markdown_report(
        [
            {
                "scenario_id": "check_order_status_001",
                "goal": "Check order status",
                "scenario_pass": True,
                "intent_detected": True,
                "first_correct_turn": 2,
                "steps_expected": 2,
                "steps_passed": 2,
                "transcript": [
                    {
                        "turn": 1,
                        "user_text": "Where is my order?",
                        "user_asr": "Where is my order?",
                        "bot_text": "Can you share your order number?",
                        "detected_intent": "Ask for help",
                        "expected_intent": "Check order status",
                        "intent_correct": False,
                        "pass": True,
                        "expectation": {"contains": "order number"},
                        "user_wav": "audio/user_1.wav",
                        "bot_wav": "audio/bot_1.wav",
                    },
                    {
                        "turn": 2,
                        "user_text": "It's 12345.",
                        "user_asr": "It's 12345.",
                        "bot_text": "Your order is on the way.",
                        "detected_intent": "Check order status",
                        "expected_intent": "Check order status",
                        "intent_correct": True,
                        "pass": True,
                        "expectation": {"contains": "on the way"},
                        "user_wav": "audio/user_2.wav",
                        "bot_wav": "audio/bot_2.wav",
                    },
                ],
            }
        ],
        out_path,
    )

    content = out_path.read_text(encoding="utf-8")

    assert "**Intent Detection Accuracy:** 1/1 (100%)" in content
    assert "| Scenario | Intent | Result | Steps Passed |" in content
    assert "| check_order_status_001 | ✅ (turn 2) | ✅ PASS | 2/2 |" in content


def test_write_markdown_report_shows_detected_intent_per_turn(tmp_path):
    out_path = tmp_path / "report.md"

    write_markdown_report(
        [
            {
                "scenario_id": "missing_package_001",
                "goal": "Report a missing package",
                "scenario_pass": False,
                "intent_detected": False,
                "first_correct_turn": None,
                "steps_expected": 1,
                "steps_passed": 0,
                "transcript": [
                    {
                        "turn": 1,
                        "user_text": "My package never arrived.",
                        "user_asr": "My package never arrived.",
                        "bot_text": "Can you share your order number?",
                        "detected_intent": "Check order status",
                        "expected_intent": "Report a missing package",
                        "intent_correct": False,
                        "pass": False,
                        "expectation": {"contains": "order number"},
                        "user_wav": "audio/user_1.wav",
                        "bot_wav": "audio/bot_1.wav",
                    },
                    {
                        "turn": 2,
                        "user_text": "It's order 12345.",
                        "user_asr": "It's order 12345.",
                        "bot_text": "I've opened an investigation.",
                        "detected_intent": "Report a missing package",
                        "expected_intent": "Report a missing package",
                        "intent_correct": True,
                        "pass": True,
                        "expectation": {},
                        "user_wav": "audio/user_2.wav",
                        "bot_wav": "audio/bot_2.wav",
                    },
                ],
            }
        ],
        out_path,
    )

    content = out_path.read_text(encoding="utf-8")

    assert (
        "**Detected Intent:** Check order status ❌ "
        "(expected: Report a missing package)"
    ) in content
    assert "**Detected Intent:** Report a missing package ✅" in content
