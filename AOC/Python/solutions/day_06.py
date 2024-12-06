from models.aoc_solution import AOCSolution


class Day06(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 41, "data": 4374},
        "part_two": {"sample": 0, "data": 0},
    }

    def __post_init__(self) -> None:
        self.grid = self.data.splitlines()
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        caret = self.data.index("^")
        self.start = caret % (self.width + 1), caret // (self.width + 1)

    def part_one(self) -> int:
        x, y = self.start
        positions = {(x, y)}
        dx, dy = 0, -1
        while x + dx in range(self.width) and y + dy in range(self.height):
            if self.grid[y + dy][x + dx] == "#":
                dx, dy = -dy, dx
            x += dx
            y += dy
            positions.add((x, y))
        return len(positions)

    def part_two(self) -> int:
        return 0


if __name__ == "__main__":
    Day06().run()
