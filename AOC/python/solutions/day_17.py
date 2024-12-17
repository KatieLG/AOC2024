import re

from models.aoc_solution import AOCSolution


class Day17(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": "4,6,3,5,6,3,5,2,1,0", "data": "1,5,0,1,7,4,1,0,3"},
        "part_two": {"sample": 117440, "data": 47910079998866},
    }

    def __post_init__(self) -> None:
        a, b, c, _, program = [
            list(map(int, re.findall(r"(\d+)", line)))
            for line in self.data.splitlines()
        ]
        self.registers = (a[0], b[0], c[0])
        self.program = program

    def run_code(self, registers: tuple[int, int, int]) -> list[int]:
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
        return output

    def part_one(self) -> str:
        return ",".join(map(str, self.run_code(self.registers)))

    def part_two(self) -> int:
        """
        Translating the input program into hardcoded form, it reads as follows:
        (2, 4): b = a % 8
        (1, 6): b = b ^ 6
        (7, 5): c = a // 2**b
        (4, 4): b = b ^ c
        (1, 7): b = b ^ 7
        (0, 3): a = a // 2**3
        (5, 5): print(b % 8)
        (3, 0): if a != 0: goto 0

        Which simplifies to:
        b = a % 8
        b = b ^ 6
        b = b ^ (a // 2**b) ^ 7
        a = a // 8
        print(b % 8)
        if a != 0: goto 0

        For the sample:
        (0, 3): a = a // 8
        (5, 4): print(a % 8)
        (3, 0): if a != 0: goto 0

        For the sample, just keep multiplying by 8 and getting the number that gives the correct output mod 8
        a = 0
        for r in reversed(self.program[:-1]):
            a += r
            a *= 8

        For the program, roughly the same
        valid = [0]
        then for each character from the end, keep any of the 8 values that output that character first
        """
        print(self.program)
        a, b, c = self.registers
        valid = [0]
        for r in reversed(self.program):
            valid = [
                8 * a + k
                for a in valid
                for k in range(8)
                if self.run_code((8 * a + k, b, c))[0] == r
            ]
        return valid[0]


if __name__ == "__main__":
    Day17().run()
