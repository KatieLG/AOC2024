import sys
from abc import ABC, abstractmethod
from enum import Enum
from pathlib import Path


class Dataset(Enum):
    SAMPLE = "sample"
    DATA = "data"


class AOCSolution(ABC):
    EXPECTED: dict[str, dict[str, str | int]]

    def __init__(self) -> None:
        self.day = int(self.__class__.__name__.replace("Day", ""))
        self.root = Path(__file__).parent.parent.parent
        self.data = ""
        self.sample = False

    def set_data(self, part: str, dataset: Dataset) -> None:
        folder = f"data/day_{self.day:02d}"
        filename = f"sample_{part}" if dataset == Dataset.SAMPLE else "dataset"
        self.sample = dataset.value == Dataset.SAMPLE.value
        self.data = Path(self.root, f"{folder}/{filename}.txt").read_text(
            encoding="utf-8"
        )
        self.__post_init__()

    def __post_init__(self) -> None: ...

    @abstractmethod
    def part_one(self) -> int | str: ...

    @abstractmethod
    def part_two(self) -> int | str: ...

    def run(self) -> None:
        iterable = [Dataset.SAMPLE] if "--sample" in sys.argv else Dataset
        for dataset in iterable:
            print(dataset.value.capitalize())
            for part in ["part_one", "part_two"]:
                self.set_data(part, dataset)
                print(f"{part}: {getattr(self, part)()}")
