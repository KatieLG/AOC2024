from models.aoc_solution import AOCSolution


class Day06(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 41, "data": 4374},
        "part_two": {"sample": 6, "data": 1705},
    }

    def __post_init__(self) -> None:
        self.grid = [[*line] for line in self.data.splitlines()]
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        caret = self.data.index("^")
        self.start = caret % (self.width + 1), caret // (self.width + 1)

    def visited_positions(self) -> tuple[set[tuple[int, int]], bool]:
        """Returns visited positions, as well as whether there is a loop"""
        x, y = self.start
        dx, dy = 0, -1
        positions = {(x, y)}
        states = {(x, y, dx, dy)}
        while 0 <= x + dx < self.width and 0 <= y + dy < self.height:
            if self.grid[y + dy][x + dx] == "#":
                dx, dy = -dy, dx
            else:
                x += dx
                y += dy
                positions.add((x, y))
            if (x, y, dx, dy) in states:
                return positions, True
            states.add((x, y, dx, dy))
        return positions, False

    def part_one(self) -> int:
        """Turn 90deg at every # until moving off the grid"""
        positions, _ = self.visited_positions()
        return len(positions)

    def part_two(self) -> int:
        """Brute force"""
        positions, _ = self.visited_positions()
        obstacles: set[tuple[int, int]] = set()
        for x, y in positions:
            if self.grid[y][x] != ".":
                continue
            self.grid[y][x] = "#"
            _, loop = self.visited_positions()
            if loop:
                obstacles.add((x, y))
            self.grid[y][x] = "."
        return len(obstacles)


if __name__ == "__main__":
    Day06().run()
