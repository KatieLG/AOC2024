import sys

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

    def nbrs(self, grid: list[list[str]], x: int, y: int) -> list[tuple[int, int]]:
        """Find valid neighbours of a point"""
        return [
            (x2, y2)
            for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
            if 0 <= x2 < self.size and 0 <= y2 < self.size and grid[y][x] != "#"
        ]

    def costs(self, grid: list[list[str]], start: tuple[int, int]) -> list[list[int]]:
        """Traverse the grid marking costs"""
        costs = [[-1 for _ in range(self.size)] for _ in range(self.size)]

        def traverse(x: int, y: int, cost: int = 0) -> None:
            costs[y][x] = cost
            for x2, y2 in self.nbrs(grid, x, y):
                if costs[y2][x2] == -1 or cost + 1 < costs[y2][x2]:
                    traverse(x2, y2, cost + 1)

        traverse(*start)
        return costs

    def blocked(self, fallen: int) -> bool:
        """Is the grid blocked after this many bytes have fallen"""
        grid = self.make_grid(fallen)
        costs = self.costs(grid, (0, 0))
        return costs[-1][-1] == -1

    def part_one(self) -> int:
        grid = self.make_grid(12 if self.sample else 1024)
        costs = self.costs(grid, (0, 0))
        return costs[-1][-1]

    def part_two(self) -> str:
        fallen = 0
        while not self.blocked(fallen):
            fallen += 100
        while self.blocked(fallen):
            fallen -= 1
        return ",".join(map(str, self.bytes[fallen]))


if __name__ == "__main__":
    Day18().run()
