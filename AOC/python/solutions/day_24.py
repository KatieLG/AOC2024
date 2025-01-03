import contextlib
import json
import re
from pathlib import Path

from models.aoc_solution import AOCSolution


class Day24(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 2024, "data": 49520947122770},
        "part_two": {"sample": 0, "data": 0},
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
    def parse_gate(gate: str, wires: dict[str, int]) -> int:
        a, op, b = re.findall(r"(\w{3}) (AND|OR|XOR) (\w{3})", gate)[0]
        return {
            "AND": wires[a] & wires[b],
            "OR": wires[a] | wires[b],
            "XOR": wires[a] ^ wires[b],
        }[op]

    def evaluate_gates(self, gates: dict[str, str]) -> dict[str, int]:
        wires = self.values.copy()
        gates = gates.copy()
        while gates:
            for out, gate in list(gates.items()):
                with contextlib.suppress(KeyError):
                    wires[out] = self.parse_gate(gate, wires)
                    gates.pop(out)
        return wires

    @staticmethod
    def prefixed_values(prefix: str, values: dict[str, int]) -> list[tuple[str, str]]:
        return sorted(
            [(out, str(val)) for out, val in values.items() if out.startswith(prefix)],
            reverse=True,
        )

    @staticmethod
    def prefixed_gates(prefix: str, gates: dict[str, str]) -> list[tuple[str, str]]:
        return sorted(
            [(out, gate) for out, gate in gates.items() if out.startswith(prefix)],
            reverse=True,
        )

    def unpack_gate(self, gate: str) -> str:
        a, op, b = re.findall(r"(\w{3}) (AND|OR|XOR) (\w{3})", gate)[0]
        if a[0] not in {"x", "y"}:
            a = f"({self.unpack_gate(self.gates[a])})"
        if b[0] not in {"x", "y"}:
            b = f"({self.unpack_gate(self.gates[b])})"
        op = {"AND": "&", "OR": "|", "XOR": "^"}[op]
        return f"{a} {op} {b}"

    def unpack_gates(self, gates: dict[str, str]) -> dict[str, str]:
        """Perform replacements until only x and y gates remain"""
        gates = gates.copy()
        for key, value in gates.items():
            gates[key] = self.unpack_gate(value)
        return gates

    def part_one(self) -> int:
        wires = self.evaluate_gates(self.gates)
        z_values = self.prefixed_values("z", wires)
        values = "".join((value for _, value in z_values))
        return int(values, 2)

    def part_two(self) -> int:
        """
        By observation z12 is the first problem
        """
        gates = self.unpack_gates(self.gates)
        prefixed = self.prefixed_gates("z", gates)
        Path("debug.json").write_text(json.dumps(dict(reversed(prefixed)), indent=4))
        print(gates)
        return 0


if __name__ == "__main__":
    Day24().run()
