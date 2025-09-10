from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any, List
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


def load_scenario(path: Path) -> Scenario:
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    
    if "id" not in data:
        raise ValueError(f"Scenario file {path} missing required 'id' field")
    
    steps = []
    for step_data in data.get("steps", []):
        step = Step(
            user=step_data.get("user"),
            bot_expect=step_data.get("bot_expect")
        )
        steps.append(step)
    
    return Scenario(
        id=data["id"],
        goal=data.get("goal", ""),
        steps=steps,
        acceptance=data.get("acceptance", {})
    )


def load_scenarios(dir_path: Path) -> List[Scenario]:
    scenarios = []
    for yaml_file in dir_path.glob("*.yaml"):
        scenario = load_scenario(yaml_file)
        scenarios.append(scenario)
    return scenarios
