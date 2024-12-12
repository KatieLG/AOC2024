from models.aoc_solution import AOCSolution

type Coord = tuple[int, int]


class Day12(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 1930, "data": 1473408},
        "part_two": {"sample": 1206, "data": 0},
    }

    def __post_init__(self) -> None:
        self.grid = self.data.splitlines()
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def nbrs(self, x: int, y: int) -> list[Coord]:
        """Adjacent cells with the same value."""
        points = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [
            (x2, y2)
            for x2, y2 in points
            if 0 <= x2 < self.width
            and 0 <= y2 < self.height
            and self.grid[y][x] == self.grid[y2][x2]
        ]

    def group(self, x: int, y: int) -> list[Coord]:
        """Find group containing a given coordinate."""
        group = []
        queue = [(x, y)]
        while queue:
            x, y = queue.pop()
            if (x, y) in group:
                continue
            group.append((x, y))
            queue.extend(self.nbrs(x, y))
        return group

    def groups(self) -> list[list[Coord]]:
        """Get all groups of cells in the grid."""
        visited = set()
        groups = []
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in visited:
                    continue
                group = self.group(x, y)
                visited.update(group)
                groups.append(group)
        return groups

    def perimeter(self, group: list[Coord]) -> int:
        """Use nbrs to determine how many sides need covering."""
        perimeter = 0
        for x, y in group:
            perimeter += 4 - len(self.nbrs(x, y))
        return perimeter

    def part_one(self) -> int:
        """Sum the areas"""
        return sum(self.perimeter(group) * len(group) for group in self.groups())

    def part_two(self) -> int:
        return 0


if __name__ == "__main__":
    Day12().run()
