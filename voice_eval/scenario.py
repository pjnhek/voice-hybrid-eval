from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml


@dataclass
class Step:
    user: Optional[str] = None
    bot_expect: Optional[Dict[str, Any]] = None


@dataclass
class Scenario:
    id: str
    goal: str
    steps: List[Step]
    acceptance: Dict[str, Any]


def _parse_scenario(data: Dict[str, Any], path: Path) -> Scenario:
    if not isinstance(data, dict):
        raise ValueError(f"Scenario file {path} must contain a scenario mapping")

    if "id" not in data:
        raise ValueError(f"Scenario file {path} missing required 'id' field")

    steps = []
    for step_data in data.get("steps", []):
        if not isinstance(step_data, dict):
            raise ValueError(f"Scenario file {path} has an invalid step entry")

        steps.append(
            Step(
                user=step_data.get("user"),
                bot_expect=step_data.get("bot_expect"),
            )
        )

    return Scenario(
        id=data["id"],
        goal=data.get("goal", ""),
        steps=steps,
        acceptance=data.get("acceptance", {}),
    )


def load_scenario(path: Path) -> Scenario:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    if isinstance(data, list):
        raise ValueError(f"Scenario file {path} contains multiple scenarios; use load_scenarios instead")

    return _parse_scenario(data, path)


def load_scenarios(dir_path: Path) -> List[Scenario]:
    scenarios = []
    for yaml_file in sorted(dir_path.glob("*.yaml")):
        data = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))

        if isinstance(data, list):
            for item in data:
                scenarios.append(_parse_scenario(item, yaml_file))
        else:
            scenarios.append(_parse_scenario(data, yaml_file))

    return scenarios
