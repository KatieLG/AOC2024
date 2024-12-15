from models.aoc_solution import AOCSolution


class Day02(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 2, "data": 242},
        "part_two": {"sample": 4, "data": 311},
    }

    @property
    def parsed_data(self) -> list[list[int]]:
        """Lines of lists of integers"""
        return [list(map(int, line.split())) for line in self.data.splitlines()]

    @staticmethod
    def is_increasing(line: list[int]) -> bool:
        """If line is increasing with differences of at least 1 and at most 3"""
        return all(b > a and 0 < b - a < 4 for a, b in zip(line, line[1:]))

    def is_safe(self, line: list[int]) -> bool:
        """If line is increasing or decreasing by increments of 1-3 inclusive"""
        return self.is_increasing(line) or self.is_increasing(line[::-1])

    def is_increasing_with_removal(self, line: list[int]) -> bool:
        """Is increasing in increments of 1-3 when up to 1 element is removed"""
        for i in range(len(line)):
            if self.is_safe(line[:i] + line[i + 1 :]):
                return True
        return self.is_safe(line)

    def is_safe_with_removal(self, line: list[int]) -> bool:
        """If safe when up to 1 element is removed"""
        return self.is_increasing_with_removal(line) or self.is_increasing_with_removal(
            line[::-1]
        )

    def part_one(self) -> int:
        """Count up the number of safe lines"""
        return len([line for line in self.parsed_data if self.is_safe(line)])

    def part_two(self) -> int:
        """Number of safe lines or lines that are safe when 1 element is removed"""
        return len(
            [line for line in self.parsed_data if self.is_safe_with_removal(line)]
        )


if __name__ == "__main__":
    Day02().run()
