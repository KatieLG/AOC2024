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
        self.registers = [a[0], b[0], c[0]]
        self.a, self.b, self.c = self.registers
        self.program = program
        self.pointer = 0
        self.output: list[int] = []

    def reset(self) -> None:
        self.a, self.b, self.c = self.registers
        self.pointer = 0
        self.output = []

    def division(self) -> int:
        operand = self.get_combo_operand()
        n, d = self.a, 2**operand
        return n // d

    def adv(self) -> None:
        self.a = self.division()

    def bxl(self) -> None:
        operand = self.get_literal_operand()
        self.b = self.b ^ operand

    def bst(self) -> None:
        operand = self.get_combo_operand()
        self.b = operand % 8

    def jnz(self) -> None:
        """Don't move pointer forward 2 if jumped"""
        if self.a != 0:
            self.pointer = self.get_literal_operand()
            self.pointer -= 2

    def bxc(self) -> None:
        self.b = self.b ^ self.c

    def out(self) -> None:
        self.output.append(self.get_combo_operand() % 8)

    def bdv(self) -> None:
        self.b = self.division()

    def cdv(self) -> None:
        self.c = self.division()

    def get_literal_operand(self) -> int:
        return self.program[self.pointer + 1]

    def get_combo_operand(self) -> int:
        operand = self.program[self.pointer + 1]
        return {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.a,
            5: self.b,
            6: self.c,
        }[operand]

    def handle_opcode(self, opcode: int) -> None:
        func = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }[opcode]
        func()

    def run_code(self) -> str:
        self.reset()
        while self.pointer < len(self.program):
            opcode = self.program[self.pointer]
            self.handle_opcode(opcode)
            self.pointer += 2
        return ",".join(map(str, self.output))

    def part_one(self) -> str:
        return self.run_code()

    def part_two(self) -> int:
        return 0


if __name__ == "__main__":
    Day17().run()
