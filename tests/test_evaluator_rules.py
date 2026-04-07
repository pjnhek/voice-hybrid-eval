from voice_eval.evaluator_rules import check_bot_expect_enhanced


def test_contains_match_passes():
    assert check_bot_expect_enhanced(
        "I can help with your order number.",
        {"contains": "order number"},
    ) is True


def test_contains_no_match_fails():
    assert check_bot_expect_enhanced(
        "I can help with your refund.",
        {"contains": "order number"},
    ) is False


def test_contains_is_case_insensitive():
    assert check_bot_expect_enhanced(
        "Your Refund Has Been Processed.",
        {"contains": "refund has been processed"},
    ) is True


def test_contains_any_passes_on_first_match():
    assert check_bot_expect_enhanced(
        "Please share your order number.",
        {"contains_any": ["order number", "last four digits"]},
    ) is True


def test_contains_any_passes_on_second_match():
    assert check_bot_expect_enhanced(
        "Please share the last four digits of the card.",
        {"contains_any": ["order number", "last four digits"]},
    ) is True


def test_contains_any_with_no_match_fails():
    assert check_bot_expect_enhanced(
        "I updated your shipping address.",
        {"contains_any": ["refund", "return label"]},
    ) is False


def test_empty_expect_returns_true():
    assert check_bot_expect_enhanced("Anything", {}) is True


def test_unknown_key_returns_false():
    assert check_bot_expect_enhanced("Anything", {"equals": "Anything"}) is False
