from functools import cache

from helpers.grid_helpers import find_char
from models.aoc_solution import AOCSolution

type Coord = tuple[int, int]


class Day21(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 126384, "data": 278748},
        "part_two": {"sample": 0, "data": 0},
    }

    def __post_init__(self) -> None:
        self.codes = self.data.splitlines()
        self.keypad = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [None, "0", "A"],
        ]
        self.directions = [
            [None, "^", "A"],
            ["<", "v", ">"],
        ]
        self.key_start = find_char(self.keypad, "A")
        self.dir_start = find_char(self.directions, "A")
        self.numpad_paths.cache_clear()

    @cache
    def numpad_paths(self, start: str, end: str, is_numpad: bool) -> set[str]:
        """Generate all paths between start and end avoiding None tiles"""
        grid = self.keypad if is_numpad else self.directions
        x, y = find_char(grid, start)
        x2, y2 = find_char(grid, end)
        dx, dy = x2 - x, y2 - y
        paths: set[str] = set()
        path = f"{'<>'[dx > 0] * abs(dx)}{'^v'[dy > 0] * abs(dy)}"
        if grid[y][x + dx] is not None:
            paths.add(f"{path}A")
        if grid[y + dy][x] is not None:
            paths.add(f"{path[::-1]}A")
        return paths

    def code_paths(self, code: str, is_numpad: bool) -> set[str]:
        """Generate all paths for a given code"""
        if len(code) < 2:
            return {""}
        starts = self.numpad_paths(code[0], code[1], is_numpad)
        return {
            start + path
            for start in starts
            for path in self.code_paths(code[1:], is_numpad)
        }

    def generate_parent_paths(self, code: str) -> set[str]:
        """Generate all paths for a given code"""
        paths = self.code_paths(f"A{code}", True)
        parent_paths = set()
        for _ in range(2):
            parent_paths = set()
            for path in paths:
                parent_paths.update(self.code_paths(f"A{path}", False))
            paths = parent_paths
        return parent_paths

    def part_one(self) -> int:
        total = 0
        for code in self.codes:
            paths = self.generate_parent_paths(code)
            shortest = min(len(path) for path in paths)
            numeric = int(code[:-1])
            total += numeric * shortest
        return total

    def part_two(self) -> int:
        return 0


if __name__ == "__main__":
    Day21().run()
