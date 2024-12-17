import re

from models.aoc_solution import AOCSolution


class Day17(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": "4,6,3,5,6,3,5,2,1,0", "data": "1,5,0,1,7,4,1,0,3"},
        "part_two": {"sample": 117440, "data": 0},
    }

    def __post_init__(self) -> None:
        a, b, c, _, program = [
            list(map(int, re.findall(r"(\d+)", line)))
            for line in self.data.splitlines()
        ]
        self.registers = (a[0], b[0], c[0])
        self.program = program

    def run_code(self, registers: tuple[int, int, int]) -> str:
        a, b, c = registers
        pointer = 0
        output: list[int] = []
        while pointer < len(self.program):
            op = self.program[pointer]
            operand = self.program[pointer + 1]
            combo = {4: a, 5: b, 6: c}.get(operand, operand)
            if op == 0:  # adv
                a = a // 2**combo
            elif op == 1:  # bxl
                b = b ^ operand
            elif op == 2:  # bst
                b = combo % 8
            elif op == 3 and a != 0:  # jnz
                pointer = operand - 2
            elif op == 4:  # bxc
                b = b ^ c
            elif op == 5:  # out
                output.append(combo % 8)
            elif op == 6:  # bdv
                b = a // 2**combo
            elif op == 7:  # cdv
                c = a // 2**combo
            pointer += 2
        return ",".join(map(str, output))

    def part_one(self) -> str:
        return self.run_code(self.registers)

    def part_two(self) -> int:
        return 0


if __name__ == "__main__":
    Day17().run()
