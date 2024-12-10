from models.aoc_solution import AOCSolution


class Day10(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 0, "data": 0},
        "part_two": {"sample": 0, "data": 0},
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

    def nbrs(self, x: int, y: int) -> list[tuple[int, int]]:
        """Get the valid neighbours of a cell"""
        return [
            (x + dx, y + dy)
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if 0 <= x + dx < self.width
            and 0 <= y + dy < self.height
            and self.grid[y + dy][x + dx] == 1 + self.grid[y][x]
        ]

    def find_trails(self, x: int, y: int) -> set[tuple[int, int]]:
        """Find all reachable 9s from the start position"""
        if self.grid[y][x] == 9:
            return {(x, y)}
        trails: set[tuple[int, int]] = set()
        for nbr in self.nbrs(x, y):
            x, y = nbr
            trails.update(self.find_trails(x, y))
        return trails

    def part_one(self) -> int:
        trail_scores: list[int] = []
        for start in self.heads:
            x, y = start
            trail_scores.append(len(self.find_trails(x, y)))
        return sum(trail_scores)

    def part_two(self) -> int:
        return 0


if __name__ == "__main__":
    Day10().run()
