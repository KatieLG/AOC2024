from models.aoc_solution import AOCSolution


class Day04(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 18, "data": 2575},
        "part_two": {"sample": 9, "data": 2041},
    }

    def __post_init__(self):
        self.parsed_data = self.data.splitlines()
        self.width = len(self.parsed_data[0])
        self.height = len(self.parsed_data)
        self.columns = ["".join(col) for col in zip(*self.parsed_data)]

    def _diagonals(self, *, size: int, is_left: bool) -> list[str]:
        direction = 1 if is_left else -1
        return [
            "".join(self.parsed_data[y + i][x + i * direction] for i in range(size))
            for y in range(self.height)
            for x in range(self.width)
            if -1 <= x + size * direction <= self.width and y + size <= self.height
        ]

    def left_diagonals(self, size: int) -> list[str]:
        return self._diagonals(size=size, is_left=True)

    def right_diagonals(self, size: int) -> list[str]:
        return self._diagonals(size=size, is_left=False)

    def find_occurences(self, word: str) -> int:
        return sum(
            line.count(word) + line.count(word[::-1])
            for group in [
                self.columns,
                self.parsed_data,
                self.left_diagonals(4),
                self.right_diagonals(4),
            ]
            for line in group
        )

    def part_one(self) -> int:
        return self.find_occurences("XMAS")

    def part_two(self) -> int:
        count = 0
        for left, right in zip(self.left_diagonals(3), self.right_diagonals(3)):
            if left in {"MAS", "SAM"} and right in {"MAS", "SAM"}:
                count += 1
        return count


if __name__ == "__main__":
    Day04().run()
