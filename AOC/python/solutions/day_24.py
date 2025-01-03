import contextlib
import re
from typing import Generator

from models.aoc_solution import AOCSolution


class Day24(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 2024, "data": 49520947122770},
        "part_two": {
            "sample": "z00,z01,z02,z03,z04,z05",
            "data": "gjc,gvm,qjj,qsb,wmp,z17,z26,z39",
        },
    }

    def __post_init__(self) -> None:
        wires, gates = self.data.split("\n\n")
        self.values = {
            wire: int(value)
            for line in wires.splitlines()
            for wire, value in [line.split(":")]
        }
        self.gates = {
            output: gate
            for line in gates.splitlines()
            for gate, output in [line.split(" -> ")]
        }

    @staticmethod
    def parse_gate(gate: str) -> tuple[str, str, str]:
        return re.findall(r"(\w{3}) (AND|OR|XOR) (\w{3})", gate)[0]

    def evaluate_gate(self, gate: str, wires: dict[str, int]) -> int:
        a, op, b = self.parse_gate(gate)
        return {
            "AND": wires[a] & wires[b],
            "OR": wires[a] | wires[b],
            "XOR": wires[a] ^ wires[b],
        }[op]

    def evaluate_gates(self, gates: dict[str, str]) -> dict[str, int]:
        wires = self.values.copy()
        while gates:
            for out, gate in list(gates.items()):
                with contextlib.suppress(KeyError):
                    wires[out] = self.evaluate_gate(gate, wires)
                    gates.pop(out)
        return wires

    @staticmethod
    def prefixed_values(prefix: str, values: dict[str, int]) -> list[tuple[str, str]]:
        return sorted(
            [(out, str(val)) for out, val in values.items() if out.startswith(prefix)],
            reverse=True,
        )

    def gates_containing(
        self, value: str
    ) -> Generator[tuple[str, str, str], None, None]:
        for gate in self.gates.values():
            a, op, b = self.parse_gate(gate)
            if value in {a, b}:
                yield a, op, b

    def part_one(self) -> int:
        wires = self.evaluate_gates(self.gates.copy())
        z_values = self.prefixed_values("z", wires)
        values = "".join((value for _, value in z_values))
        return int(values, 2)

    def part_two(self) -> str:
        swap = set()
        for output, gate in self.gates.items():
            a, op, b = self.parse_gate(gate)
            if output[0] == "z" and op != "XOR" and output != "z45":
                # z gate but not an XOR gate
                swap.add(output)
            if output[0] != "z" and op == "XOR" and {a[0], b[0]} != {"x", "y"}:
                swap.add(output)
            if op == "XOR":
                # OR gates cannot have XOR gates as input
                for c, op2, d in self.gates_containing(output):
                    if op2 == "OR":
                        swap.add(output)
            if op == "AND" and {a, b} != {"x00", "y00"}:
                # Excluding the first one, can't have XOR gates with AND input
                for c, op2, d in self.gates_containing(output):
                    if op2 == "XOR":
                        swap.add(output)

        return ",".join(sorted(swap))


if __name__ == "__main__":
    Day24().run()
