import contextlib
import re

from models.aoc_solution import AOCSolution


class Day24(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 2024, "data": 49520947122770},
        "part_two": {"sample": 0, "data": 0},
    }

    def __post_init__(self) -> None:
        wires, gates = self.data.split("\n\n")
        self.wires = {
            wire: int(value)
            for line in wires.splitlines()
            for wire, value in [line.split(":")]
        }
        self.gates = {
            output: gate
            for line in gates.splitlines()
            for gate, output in [line.split(" -> ")]
        }
        self.calculate_wires()

    def parse_gate(self, gate: str) -> int:
        a, op, b = re.findall(r"(\w{3}) (AND|OR|XOR) (\w{3})", gate)[0]
        return {
            "AND": self.wires[a] & self.wires[b],
            "OR": self.wires[a] | self.wires[b],
            "XOR": self.wires[a] ^ self.wires[b],
        }[op]

    def calculate_wires(self) -> None:
        while self.gates:
            for out, gate in list(self.gates.items()):
                with contextlib.suppress(KeyError):
                    self.wires[out] = self.parse_gate(gate)
                    self.gates.pop(out)

    def part_one(self) -> int:
        z_values = sorted(
            [(out, str(val)) for out, val in self.wires.items() if out.startswith("z")],
            reverse=True,
        )
        values = "".join((value for _, value in z_values))
        return int(values, 2)

    def part_two(self) -> int:
        return 0


if __name__ == "__main__":
    Day24().run()
