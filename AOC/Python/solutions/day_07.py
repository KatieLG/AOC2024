from typing import Generator

from models.aoc_solution import AOCSolution


class Day07(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 3749, "data": 2664460013123},
        "part_two": {"sample": 11387, "data": 426214131924213},
    }

    def __post_init__(self) -> None:
        self.equations = [
            (int(data[0]), [int(k) for k in data[1].split() if k.isnumeric()])
            for line in self.data.splitlines()
            for data in [line.split(":")]
        ]
        self.operations = [
            lambda a, b: a + b,
            lambda a, b: a * b,
        ]

    def possible_totals(
        self, current: int, remaining: list[int]
    ) -> Generator[int, None, None]:
        if not remaining:
            yield current
            return
        for operation in self.operations:
            yield from self.possible_totals(
                operation(current, remaining[0]), remaining[1:]
            )

    def is_equation_valid(self, total: int, numbers: list[int]) -> bool:
        return any(
            value == total for value in self.possible_totals(numbers[0], numbers[1:])
        )

    def part_one(self) -> int:
        return sum(
            total
            for total, numbers in self.equations
            if self.is_equation_valid(total, numbers)
        )

    def part_two(self) -> int:
        self.operations.append(lambda a, b: int(f"{a}{b}"))
        return sum(
            total
            for total, numbers in self.equations
            if self.is_equation_valid(total, numbers)
        )


if __name__ == "__main__":
    Day07().run()
