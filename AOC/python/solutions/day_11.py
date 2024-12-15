from functools import cache

from models.aoc_solution import AOCSolution


class Day11(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 55312, "data": 212655},
        "part_two": {"sample": 65601038650482, "data": 253582809724830},
    }

    def __post_init__(self) -> None:
        self.stones = list(map(int, self.data.split()))

    @staticmethod
    def transform_stone(stone: int) -> list[int]:
        """One blink on a stone"""
        if stone == 0:
            return [1]
        string = str(stone)
        if len(string) % 2 == 0:
            half = len(string) // 2
            return [int(string[:half]), int(string[half:])]
        return [stone * 2024]

    @cache
    def blink(self, stone: int, times: int) -> int:
        """How many stones result from blinking a given number of times"""
        if times == 0:
            return 1
        return sum(self.blink(s, times - 1) for s in self.transform_stone(stone))

    def part_one(self) -> int:
        return sum(self.blink(stone, 25) for stone in self.stones)

    def part_two(self) -> int:
        return sum(self.blink(stone, 75) for stone in self.stones)


if __name__ == "__main__":
    Day11().run()
