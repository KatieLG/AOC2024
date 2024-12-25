from models.aoc_solution import AOCSolution


class Day25(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 3, "data": 3065},
        "part_two": {"sample": 0, "data": 0},
    }

    def __post_init__(self) -> None:
        grids = [self.parse_grid(grid) for grid in self.data.split("\n\n")]
        self.locks = [grid for grid, is_key in grids if not is_key]
        self.keys = [grid for grid, is_key in grids if is_key]
        self.height = 7

    @staticmethod
    def parse_grid(grid: str) -> tuple[list[int], bool]:
        """return heights and is_key"""
        rows = grid.splitlines()
        tranposed = [[line[i] for line in rows] for i in range(len(rows[0]))]
        if {*rows[0]} == {"."}:
            return [line[::-1].index(".") for line in tranposed], True
        return [line.index(".") for line in tranposed], False

    def fits(self, lock: list[int], key: list[int]) -> bool:
        return all(h + k <= self.height for h, k in zip(lock, key))

    def part_one(self) -> int:
        return sum(self.fits(lock, key) for lock in self.locks for key in self.keys)

    def part_two(self) -> int:
        return 0


if __name__ == "__main__":
    Day25().run()
