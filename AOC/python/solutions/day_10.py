from typing import Generator

from models.aoc_solution import AOCSolution

type Coord = tuple[int, int]


class Day10(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 36, "data": 430},
        "part_two": {"sample": 81, "data": 928},
    }

    def __post_init__(self) -> None:
        self.grid = [list(map(int, line)) for line in self.data.splitlines()]
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.heads = [
            (x, y)
            for y, row in enumerate(self.grid)
            for x, cell in enumerate(row)
            if cell == 0
        ]

    def nbrs(self, x: int, y: int) -> list[Coord]:
        """Get the valid neighbours of a cell"""
        return [
            (x + dx, y + dy)
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if 0 <= x + dx < self.width
            and 0 <= y + dy < self.height
            and self.grid[y + dy][x + dx] == 1 + self.grid[y][x]
        ]

    def find_trails(
        self, x: int, y: int, current: list[Coord]
    ) -> Generator[list[Coord], None, None]:
        """Find paths to all reachable 9s from the start position"""
        current.append((x, y))
        if self.grid[y][x] == 9:
            yield current
        for x2, y2 in self.nbrs(x, y):
            yield from self.find_trails(x2, y2, current)

    def part_one(self) -> int:
        """Score of a trail is unique end positions"""
        return sum(
            len({trail[-1] for trail in self.find_trails(x, y, [])})
            for x, y in self.heads
        )

    def part_two(self) -> int:
        """Rating of a trail is unique paths"""
        return sum(len(list(self.find_trails(x, y, []))) for x, y in self.heads)


if __name__ == "__main__":
    Day10().run()
