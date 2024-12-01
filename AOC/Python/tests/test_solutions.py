from datetime import datetime
from importlib import import_module

import pytest

from models.aoc_solution import Dataset

today = datetime.today()


@pytest.mark.skipif(
    today.month != 12 or today.year != 2024, reason="Only runs during December 2024"
)
@pytest.mark.parametrize("day", range(1, min(today.day, 25) + 1))
@pytest.mark.parametrize("dataset", Dataset)
@pytest.mark.parametrize("part", ["part_one", "part_two"])
def test_solution(day: int, dataset: Dataset, part: str) -> None:
    module = import_module(f"solutions.day_{day:02d}")
    solution = getattr(module, f"Day{day:02d}")()
    solution.set_data(part, dataset)
    assert getattr(solution, part)() == solution.EXPECTED[part][dataset.value]
