import re

from models.aoc_solution import AOCSolution


class Day03(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 161, "data": 181345830},
        "part_two": {"sample": 48, "data": 98729041},
    }

    def part_one(self) -> int:
        multiplications = re.findall(r"mul\((\d+),(\d+)\)", self.data, re.IGNORECASE)
        return sum(int(a) * int(b) for a, b in multiplications)

    def part_two(self) -> int:
        instructions = re.findall(
            r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", self.data, re.IGNORECASE
        )
        total = 0
        enabled = True
        for instruction in instructions:
            if "do" in instruction:
                enabled = True
            elif "don't" in instruction:
                enabled = False
            elif enabled:
                a, b, *_ = instruction
                total += int(a) * int(b)
        return total


if __name__ == "__main__":
    Day03().run()
