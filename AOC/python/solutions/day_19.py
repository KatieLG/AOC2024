from functools import cache

from models.aoc_solution import AOCSolution


class Day19(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 6, "data": 226},
        "part_two": {"sample": 16, "data": 601201576113503},
    }

    def __post_init__(self) -> None:
        data = self.data.split("\n\n")
        self.patterns = data[0].split(", ")
        self.designs = data[1].splitlines()
        self.count_arrangements.cache_clear()

    @cache
    def count_arrangements(self, design: str) -> int:
        if not design:
            return 1
        return sum(
            self.count_arrangements(design[len(pattern) :])
            for pattern in self.patterns
            if design.startswith(pattern)
        )

    def part_one(self) -> int:
        return len(
            [design for design in self.designs if self.count_arrangements(design)]
        )

    def part_two(self) -> int:
        return sum(self.count_arrangements(design) for design in self.designs)


if __name__ == "__main__":
    Day19().run()
