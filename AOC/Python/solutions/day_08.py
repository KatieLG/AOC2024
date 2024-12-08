from collections import defaultdict
from typing import Callable

from models.aoc_solution import AOCSolution

type Coord = tuple[int, int]


class Day08(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 14, "data": 222},
        "part_two": {"sample": 34, "data": 884},
    }

    def __post_init__(self) -> None:
        self.grid = self.data.splitlines()
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.nodes: dict[str, list[Coord]] = defaultdict(list)
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                if char != ".":
                    self.nodes[char].append((x, y))

    def is_valid(self, point: Coord) -> bool:
        """Is point on grid"""
        return 0 <= point[0] < self.width and 0 <= point[1] < self.height

    def find_antinodes(self, x: int, y: int, x2: int, y2: int) -> set[Coord]:
        """Find the two antinodes either sides of the two points"""
        xdiff = x2 - x
        ydiff = y2 - y
        return {
            point
            for point in [(x - xdiff, y - ydiff), (x2 + xdiff, y2 + ydiff)]
            if self.is_valid(point)
        }

    def find_many_antinodes(
        self, x: int, y: int, x2: int, y2: int, *, direction: int
    ) -> set[Coord]:
        """Find all the antinodes either sides of the two points"""
        points: set[Coord] = set()
        xdiff = x2 - x
        ydiff = y2 - y
        i = 0
        while self.is_valid(point := (x + xdiff * i, y + ydiff * i)):
            i += direction
            points.add(point)
        return points

    def antinode_union(
        self, find_func: Callable[[int, int, int, int], set[Coord]]
    ) -> set[Coord]:
        """Iterate over nodes with antinode finding function"""
        union = set()
        for coords in self.nodes.values():
            for i, (x, y) in enumerate(coords):
                for x2, y2 in coords[i + 1 :]:
                    union.update(find_func(x, y, x2, y2))
        return union

    def part_one(self) -> int:
        antinodes = self.antinode_union(self.find_antinodes)
        return len(antinodes)

    def part_two(self) -> int:
        antinodes = self.antinode_union(
            lambda x, y, x2, y2: self.find_many_antinodes(x, y, x2, y2, direction=1)
            | self.find_many_antinodes(x, y, x2, y2, direction=-1)
        )
        return len(antinodes)


if __name__ == "__main__":
    Day08().run()
