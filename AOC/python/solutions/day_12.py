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
        perimeter = 0
        for x, y in group:
            perimeter += 4 - len(self.nbrs(x, y))
        return perimeter

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

    def sides(self, group: list[Coord]) -> int:
        """Find number of sides, by using the lines, and searching for gaps within them."""
        hlines, vlines = self.lines(group)
        total = 0
        for y, y2 in hlines:
            segments = []
            for x in range(self.width):
                if ((x, y) in group) != ((x, y2) in group):
                    if not segments:
                        segments.append([x])
                    else:
                        last = segments[-1]
                        # check continuity but not just across, also above, below
                        above_prev = (x - 1, y) in group and (x - 1, y2) not in group
                        above = (x, y) in group and (x, y2) not in group
                        if last[-1] == x - 1 and above_prev == above:
                            last.append(x)
                        else:
                            segments.append([x])
            total += len(segments)
        for x, x2 in vlines:
            segments = []
            for y in range(self.height):
                if ((x, y) in group) != ((x2, y) in group):
                    if not segments:
                        segments.append([y])
                    else:
                        last = segments[-1]
                        # check continuity but not just across, also left right
                        left_prev = (x, y - 1) in group and (x2, y - 1) not in group
                        left = (x, y) in group and (x2, y) not in group
                        if last[-1] == y - 1 and left_prev == left:
                            last.append(y)
                        else:
                            segments.append([y])
            total += len(segments)
        return total

    def part_one(self) -> int:
        """Sum the areas"""
        return sum(self.perimeter(group) * len(group) for group in self.groups())

    def part_two(self) -> int:
        return sum(self.sides(group) * len(group) for group in self.groups())


if __name__ == "__main__":
    Day12().run()
