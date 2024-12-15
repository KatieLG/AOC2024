from models.aoc_solution import AOCSolution


class Day15(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 10092, "data": 0},
        "part_two": {"sample": 0, "data": 0},
    }

    def __post_init__(self) -> None:
        grid, moves = self.data.split("\n\n")
        self.grid = [list(row) for row in grid.splitlines()]
        self.moves = list(moves.replace("\n", ""))
        self.pos = next(
            (x, y)
            for y, row in enumerate(self.grid)
            for x, cell in enumerate(row)
            if cell == "@"
        )

    def debug(self) -> None:
        for row in self.grid:
            print("".join(row))

    @property
    def parsed_moves(self) -> list[tuple[int, int]]:
        lookup = {
            "<": (-1, 0),
            ">": (1, 0),
            "^": (0, -1),
            "v": (0, 1),
        }
        return [lookup[move] for move in self.moves]

    def goto(self, x: int, y: int) -> None:
        """Move to a square in the grid"""
        cx, cy = self.pos
        self.grid[cy][cx] = "."
        self.pos = (x, y)
        self.grid[y][x] = "@"

    def move(self, dx: int, dy: int) -> None:
        """Move and push any boxes out of the way where they wouldn't hit a wall"""
        x, y = self.pos
        next_tile = self.grid[y + dy][x + dx]
        if next_tile == "#":
            return
        if next_tile == ".":
            self.goto(x + dx, y + dy)
            return
        if next_tile != "O":
            raise ValueError(f"Unexpected tile {next_tile}")

        bx, by = x + dx, y + dy
        while self.grid[by][bx] == "O":
            bx += dx
            by += dy

        if self.grid[by][bx] == "#":
            return

        self.grid[by][bx] = "O"
        self.goto(x + dx, y + dy)

    def gps_sum(self) -> int:
        return sum(
            100 * y + x
            for y, row in enumerate(self.grid)
            for x, cell in enumerate(row)
            if cell == "O"
        )
    
    def part_one(self) -> int:
        for p in self.parsed_moves:
            self.move(*p)
        return self.gps_sum()

    def part_two(self) -> int:
        self.debug()
        return 0


if __name__ == "__main__":
    Day15().run()
