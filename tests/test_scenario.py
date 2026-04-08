import pytest

from voice_eval.scenario import load_scenario, load_scenarios


def test_load_scenario_reads_expected_fields(tmp_path):
    scenario_file = tmp_path / "single.yaml"
    scenario_file.write_text(
        """
id: address_change_001
goal: Change shipping address
steps:
  - user: "I need to update my address"
    bot_expect:
      contains: "order number"
""".strip(),
        encoding="utf-8",
    )

    scenario = load_scenario(scenario_file)

    assert scenario.id == "address_change_001"
    assert scenario.goal == "Change shipping address"
    assert len(scenario.steps) == 1
    assert scenario.steps[0].user == "I need to update my address"
    assert scenario.steps[0].bot_expect == {"contains": "order number"}


def test_load_scenario_requires_id_field(tmp_path):
    scenario_file = tmp_path / "missing_id.yaml"
    scenario_file.write_text(
        """
goal: Change shipping address
steps: []
""".strip(),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="missing required 'id' field"):
        load_scenario(scenario_file)


def test_load_scenarios_supports_multi_scenario_yaml_files(tmp_path):
    scenario_file = tmp_path / "multi.yaml"
    scenario_file.write_text(
        """
- id: cancel_order_001
  goal: Cancel an order
  steps:
    - user: "Please cancel my order"
      bot_expect:
        contains: "order number"
- id: cancel_order_002
  goal: Cancel an order
  steps:
    - user: "Cancel order 12345"
      bot_expect:
        contains: "cancelled"
""".strip(),
        encoding="utf-8",
    )

    scenarios = load_scenarios(tmp_path)

    assert [scenario.id for scenario in scenarios] == ["cancel_order_001", "cancel_order_002"]
    assert scenarios[0].steps[0].user == "Please cancel my order"
    assert scenarios[1].steps[0].bot_expect == {"contains": "cancelled"}


def test_load_scenarios_returns_all_yaml_files(tmp_path):
    first = tmp_path / "a.yaml"
    second = tmp_path / "b.yaml"
    first.write_text(
        """
id: first
goal: One
steps: []
""".strip(),
        encoding="utf-8",
    )
    second.write_text(
        """
- id: second
  goal: Two
  steps: []
- id: third
  goal: Three
  steps: []
""".strip(),
        encoding="utf-8",
    )

    scenarios = load_scenarios(tmp_path)

    assert [scenario.id for scenario in scenarios] == ["first", "second", "third"]
