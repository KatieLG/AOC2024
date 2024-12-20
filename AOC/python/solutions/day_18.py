import sys

from helpers.grid_helpers import costs
from models.aoc_solution import AOCSolution

sys.setrecursionlimit(10000)


class Day18(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 22, "data": 322},
        "part_two": {"sample": "6,1", "data": "60,21"},
    }

    def __post_init__(self) -> None:
        self.bytes = [
            tuple(map(int, line.split(","))) for line in self.data.splitlines()
        ]
        self.size = 7 if self.sample else 71

    def make_grid(self, byte_count: int) -> list[list[str]]:
        grid = [["." for _ in range(self.size)] for _ in range(self.size)]
        for byte in self.bytes[:byte_count]:
            x, y = byte
            grid[y][x] = "#"
        return grid

    def blocked(self, fallen: int) -> bool:
        """Is the grid blocked after this many bytes have fallen"""
        grid = self.make_grid(fallen)
        dist_costs = costs(grid, {"#"}, (0, 0))
        return dist_costs[-1][-1] == -1

    def part_one(self) -> int:
        grid = self.make_grid(12 if self.sample else 1024)
        dist_costs = costs(grid, {"#"}, (0, 0))
        return dist_costs[-1][-1]

    def part_two(self) -> str:
        fallen = 0
        while not self.blocked(fallen):
            fallen += 100
        while self.blocked(fallen):
            fallen -= 1
        return ",".join(map(str, self.bytes[fallen]))


if __name__ == "__main__":
    Day18().run()
