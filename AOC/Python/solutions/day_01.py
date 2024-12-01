from models.aoc_solution import AOCSolution


class Day01(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 11, "data": 2000468},
        "part_two": {"sample": 31, "data": 18567089},
    }

    @property
    def parsed_data(self) -> list[list[int]]:
        """Retuns input data as the two adjacent integer columns"""
        return [
            [int(row.split()[i]) for row in self.data.splitlines()] for i in range(2)
        ]

    def part_one(self) -> int:
        """Sum the differences between the sorted columns"""
        first, second = self.parsed_data
        return sum(abs(a - b) for a, b in zip(sorted(first), sorted(second)))

    def part_two(self) -> int:
        """Sum the numbers in the first column multiplied by their occurences in the second"""
        first, second = self.parsed_data
        return sum(number * second.count(number) for number in first)


if __name__ == "__main__":
    Day01().run()
