from models.aoc_solution import AOCSolution

type Coord = tuple[int, int]


class Day12(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 1930, "data": 1473408},
        "part_two": {"sample": 1206, "data": 886364},
    }

    def __post_init__(self) -> None:
        self.grid = self.data.splitlines()
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def nbrs(self, x: int, y: int, *, nocheck: bool = False) -> list[Coord]:
        """Adjacent cells with the same value."""
        points = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [
            (x2, y2)
            for x2, y2 in points
            if nocheck
            or 0 <= x2 < self.width
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
        return sum(4 - len(self.nbrs(x, y)) for x, y in group)

    def lines(self, group: list[Coord]) -> tuple[set[Coord], set[Coord]]:
        """Find the horizontal and vertical lines for a particular group."""
        boundaries = [
            (x, y, x2, y2)
            for x, y in group
            for x2, y2 in self.nbrs(x, y, nocheck=True)
            if (x2, y2) not in group
        ]
        hlines = {(min(y, y2), max(y, y2)) for x, y, x2, y2 in boundaries if x == x2}
        vlines = {(min(x, x2), max(x, x2)) for x, y, x2, y2 in boundaries if y == y2}
        return hlines, vlines

    def count_segments(
        self, group: list[Coord], lines: set[Coord], is_horizontal: bool
    ):
        total = 0
        r = 1 if is_horizontal else -1
        for a, b in lines:
            segments = []
            for i in range(self.width if is_horizontal else self.height):
                if ((i, a)[::r] in group) != ((i, b)[::r] in group):
                    if segments:
                        prev = (i - 1, a)[::r] in group and (i - 1, b)[::r] not in group
                        curr = (i, a)[::r] in group and (i, b)[::r] not in group
                        last = segments[-1]
                        if last[-1] == i - 1 and prev == curr:
                            last.append(i)
                            continue
                    segments.append([i])
            total += len(segments)
        return total

    def sides(self, group: list[Coord]) -> int:
        """Find number of sides, by using the lines, and searching for gaps within them."""
        hlines, vlines = self.lines(group)
        return self.count_segments(group, hlines, True) + self.count_segments(
            group, vlines, False
        )

    def part_one(self) -> int:
        """Sum the areas"""
        return sum(self.perimeter(group) * len(group) for group in self.groups())

    def part_two(self) -> int:
        return sum(self.sides(group) * len(group) for group in self.groups())


if __name__ == "__main__":
    Day12().run()
