import sys
from typing import NamedTuple

from models.aoc_solution import AOCSolution

type Coord = tuple[int, int]

sys.setrecursionlimit(10000)


class Position(NamedTuple):
    x: int
    y: int
    dx: int
    dy: int


class Day16(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 11048, "data": 85420},
        "part_two": {"sample": 64, "data": 492},
    }

    def __post_init__(self) -> None:
        self.grid = self.data.splitlines()
        self.start = self.find_char("S")
        self.end = self.find_char("E")
        self.direction = (1, 0)  # begin facing east

    def find_char(self, char: str) -> tuple[int, int]:
        return next(
            (x, y)
            for y, row in enumerate(self.grid)
            for x, cell in enumerate(row)
            if cell == char
        )

    def nbrs(self, position: Position) -> list[tuple[int, Position]]:
        """Find the valid neigbours and their costs, pair rotations with movements to make things easier"""
        x, y, dx, dy = position
        output = [
            (1, Position(x + dx, y + dy, dx, dy)),  # foward
            (1001, Position(x - dy, y + dx, -dy, dx)),  # clockwise + foward
            (1001, Position(x + dy, y - dx, dy, -dx)),  # counterclockwise + forward
        ]
        return [(cost, nbr) for cost, nbr in output if self.grid[nbr.y][nbr.x] != "#"]

    def path(
        self, position: Position, costs: list[list[int]], current_cost: int = 0
    ) -> None:
        """Path through the maze marking all tiles with costs"""
        for cost, nbr in self.nbrs(position):
            if not costs[nbr.y][nbr.x] or current_cost + cost < costs[nbr.y][nbr.x]:
                costs[nbr.y][nbr.x] = cost + current_cost
                self.path(nbr, costs, cost + current_cost)

    def reverse_path_collect(
        self,
        position: Position,
        costs: list[list[int | None]],
        valid_cells: set[Coord],
        current_cost: int,
    ):
        """Collect cells of valid shortest paths in reverse"""
        valid_cells.add((position.x, position.y))
        for cost, nbr in self.nbrs(position):
            if not costs[nbr.y][nbr.x] or costs[nbr.y][nbr.x] <= current_cost - cost:
                self.reverse_path_collect(nbr, costs, valid_cells, current_cost - cost)

    def generate_costs(self, start_coord: Coord, start_dir: Coord) -> list[list[int]]:
        """Generate a grid of the costs to go from the start position to any other"""
        costs: list[list[int | None]] = [[None for _ in row] for row in self.grid]
        start_position = Position(*start_coord, *start_dir)
        costs[start_position.y][start_position.x] = 0
        self.path(start_position, costs)
        return costs

    def part_one(self) -> int:
        costs = self.generate_costs(self.start, self.direction)
        return costs[self.end[1]][self.end[0]]

    def part_two(self) -> int:
        """Find costs from start to end, then flood fill in reverse
        keeping only the shortest ones"""
        costs = self.generate_costs(self.start, self.direction)
        min_cost = costs[self.end[1]][self.end[0]]
        valid_cells = set()
        self.reverse_path_collect(
            Position(*self.end, 0, 1), costs, valid_cells, min_cost
        )
        return len(valid_cells)


if __name__ == "__main__":
    Day16().run()
