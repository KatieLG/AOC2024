from typing import Generator

from models.aoc_solution import AOCSolution


class GridError(Exception): ...


class Day15(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 10092, "data": 1406628},
        "part_two": {"sample": 9021, "data": 1432781},
    }

    def __post_init__(self) -> None:
        grid, moves = self.data.split("\n\n")
        self.grid = [list(row) for row in grid.splitlines()]
        self.moves = list(moves.replace("\n", ""))
        self.pos = self.get_pos("@")

    def get_pos(self, char: str) -> tuple[int, int]:
        return next(
            (x, y)
            for y, row in enumerate(self.grid)
            for x, cell in enumerate(row)
            if cell == char
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
        elif next_tile == "O":
            self.move_box(dx, dy)
        elif next_tile in {"[", "]"}:
            self.move_big_box(dx, dy)
        else:
            raise GridError(f"Invalid tile: {next_tile}")

    def move_box(self, dx: int, dy: int) -> None:
        """Move single O box(es) in the direction of dx, dy"""
        x, y = self.pos
        bx, by = x + dx, y + dy
        while self.grid[by][bx] == "O":
            bx += dx
            by += dy

        if self.grid[by][bx] == "#":
            return

        self.grid[by][bx] = "O"
        self.goto(x + dx, y + dy)

    def move_big_box(self, dx: int, dy: int) -> None:
        if dx:
            self._move_big_box_horizontally(dx, dy)
        else:
            try:
                x, y = self.pos
                bx = x if self.grid[y + dy][x] == "[" else x - 1
                moves = self._move_big_box_vertically(bx, y + dy, dy)
                unique_moves = list(dict.fromkeys(moves))
            except GridError:
                return

            for bx, by, dy in unique_moves:
                self._complete_move(bx, by, dy)
            self.goto(x + dx, y + dy)

    def _move_big_box_horizontally(self, dx: int, dy: int) -> None:
        """Horizontal movement of a big box is similar to a single box"""
        x, y = self.pos
        bx, by = x + dx, y + dy
        big_box_new = []
        while self.grid[by][bx] in {"[", "]"}:
            big_box_new.append((bx + dx, by + dy, self.grid[by][bx]))
            bx += dx
            by += dy

        if self.grid[by][bx] == "#":
            return

        # shift all along by 1
        for bx, by, box in big_box_new:
            self.grid[by][bx] = box
        self.goto(x + dx, y + dy)

    def _move_big_box_vertically(
        self, bx: int, by: int, dy: int
    ) -> Generator[tuple[int, int, int], None, None]:
        """
        Vertical movement might push numerous boxes simultaneously
        This function expects to be provided the left side of the box
        Yields the series of box moves to be performed if there are no obstructions
        This may contain duplicates which need removing
        """
        # base case, no obstructions
        if self.grid[by + dy][bx] == "." and self.grid[by + dy][bx + 1] == ".":
            yield bx, by, dy
            return
        # base case, wall
        if self.grid[by + dy][bx] == "#" or self.grid[by + dy][bx + 1] == "#":
            raise GridError("Wall is obstructing movement")
        # else push other boxes first
        if self.grid[by + dy][bx] == "[":
            yield from self._move_big_box_vertically(bx, by + dy, dy)
        if self.grid[by + dy][bx] == "]":
            yield from self._move_big_box_vertically(bx - 1, by + dy, dy)
        if self.grid[by + dy][bx + 1] == "[":
            yield from self._move_big_box_vertically(bx + 1, by + dy, dy)
        yield bx, by, dy

    def _complete_move(self, bx: int, by: int, dy: int) -> None:
        """Finish moving a big box if it's not obstructed"""
        self.grid[by + dy][bx] = "["
        self.grid[by + dy][bx + 1] = "]"
        self.grid[by][bx] = "."
        self.grid[by][bx + 1] = "."

    def gps_sum(self) -> int:
        return sum(
            100 * y + x
            for y, row in enumerate(self.grid)
            for x, cell in enumerate(row)
            if cell in {"O", "["}
        )

    def double_grid(self) -> None:
        """Double the width of everything in the grid"""
        self.grid = [
            list(
                "".join(row)
                .replace("#", "##")
                .replace("O", "[]")
                .replace(".", "..")
                .replace("@", "@.")
            )
            for row in self.grid
        ]

    def part_one(self) -> int:
        """Calculate sum of gps coords after all moves"""
        for p in self.parsed_moves:
            self.move(*p)
        return self.gps_sum()

    def part_two(self) -> int:
        """Double grid and reuse part a"""
        self.double_grid()
        self.pos = self.get_pos("@")
        for p in self.parsed_moves:
            self.move(*p)
        return self.gps_sum()


if __name__ == "__main__":
    Day15().run()
