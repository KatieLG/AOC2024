from datetime import datetime
from importlib import import_module
from types import ModuleType

import pytest

from models.aoc_solution import Dataset

today = datetime.now()


def _load_module(name: str) -> ModuleType | None:
    """Don't test modules that don't exist yet"""
    try:
        return import_module(name)
    except ModuleNotFoundError:
        return None


MODULES = [
    module
    for day in range(1, 26)
    if (module := _load_module(f"solutions.day_{day:02d}"))
]


@pytest.mark.parametrize("module", MODULES)
@pytest.mark.parametrize("dataset", Dataset)
@pytest.mark.parametrize("part", ["part_one", "part_two"])
def test_solution(module: ModuleType, dataset: Dataset, part: str) -> None:
    day = module.__name__[-2:]
    solution = getattr(module, f"Day{day}")()
    solution.set_data(part, dataset)
    assert getattr(solution, part)() == solution.EXPECTED[part][dataset.value]
