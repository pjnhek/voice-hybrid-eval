from types import SimpleNamespace

from voice_eval.evaluator_claude import check_bot_expect_claude


def test_check_bot_expect_claude_returns_true_when_model_passes(mocker):
    response = SimpleNamespace(
        content=[SimpleNamespace(text='{"pass": true, "reason": "semantic match"}')]
    )
    client = mocker.Mock()
    client.messages.create.return_value = response
    anthropic_cls = mocker.patch("voice_eval.evaluator_claude.Anthropic", return_value=client)

    result = check_bot_expect_claude(
        "I have already updated the address for your order.",
        {"contains": "address updated"},
    )

    assert result is True
    anthropic_cls.assert_called_once_with()
    client.messages.create.assert_called_once()


def test_check_bot_expect_claude_returns_false_when_model_fails(mocker):
    response = SimpleNamespace(
        content=[SimpleNamespace(text='{"pass": false, "reason": "missing refund detail"}')]
    )
    client = mocker.Mock()
    client.messages.create.return_value = response
    mocker.patch("voice_eval.evaluator_claude.Anthropic", return_value=client)

    result = check_bot_expect_claude(
        "I can look into that for you.",
        {"contains": "refund processed"},
    )

    assert result is False


def test_check_bot_expect_claude_skips_api_call_for_empty_expect(mocker):
    anthropic_cls = mocker.patch("voice_eval.evaluator_claude.Anthropic")

    result = check_bot_expect_claude("Anything", {})

    assert result is True
    anthropic_cls.assert_not_called()
