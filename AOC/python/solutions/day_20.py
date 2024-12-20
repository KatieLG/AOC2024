import sys

from helpers.grid_helpers import costs, find_char
from models.aoc_solution import AOCSolution

type Coord = tuple[int, int]

sys.setrecursionlimit(10000)


class Day20(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 1, "data": 1363},
        "part_two": {"sample": 285, "data": 1007186},
    }

    def __post_init__(self) -> None:
        self.grid = [list(line) for line in self.data.splitlines()]
        self.size = len(self.grid)
        self.start = find_char(self.grid, "S")
        self.end = find_char(self.grid, "E")

    def generate_cheats(self, max_length: int) -> set[tuple[Coord, Coord]]:
        """Generate the start, end position of all possible cheats"""
        ml = max_length
        return {
            ((x, y), (x2, y2))
            for x in range(self.size)
            for y in range(self.size)
            for x2 in range(max(x - ml, 0), min(x + ml + 1, self.size))
            for y2 in range(max(y - ml, 0), min(y + ml + 1, self.size))
            if abs(x2 - x) + abs(y2 - y) <= ml
            and (x, y) <= (x2, y2)
            and self.grid[y2][x2] != "#"
            and self.grid[y][x] != "#"
        }

    def count_best_cheats(self, *, max_cheat_length: int) -> int:
        base_costs = costs(self.grid, {"#"}, self.start)
        cheats = self.generate_cheats(max_cheat_length)
        saving_threshold = 50 if self.sample else 100
        best_cheats = 0
        for (x, y), (x2, y2) in cheats:
            cost_a = base_costs[y][x]
            cost_b = base_costs[y2][x2]
            saving = abs(cost_a - cost_b) - (abs(y2 - y) + abs(x2 - x))
            if saving >= saving_threshold:
                best_cheats += 1
        return best_cheats

    def part_one(self) -> int:
        return self.count_best_cheats(max_cheat_length=2)

    def part_two(self) -> int:
        return self.count_best_cheats(max_cheat_length=20)


if __name__ == "__main__":
    Day20().run()
