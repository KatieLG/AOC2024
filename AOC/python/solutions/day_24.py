import contextlib
import re

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
        gates = gates.copy()
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
            gates[key] = self.strip(key, self.unpack_gate(value))
        return gates

    def part_one(self) -> int:
        wires = self.evaluate_gates(self.gates)
        z_values = self.prefixed_values("z", wires)
        values = "".join((value for _, value in z_values))
        return int(values, 2)

    def part_two(self) -> str:
        bad = set()
        for output, eq in self.gates.items():
            a, op, b = re.findall(r"(\w{3}) (AND|OR|XOR) (\w{3})", eq)[0]
            if output[0] == "z" and op != "XOR" and output != "z45":
                bad.add(output)
            if op == "XOR" and all(x[0] not in {"x", "y", "z"} for x in [a, b, output]):
                bad.add(output)
            if (op == "AND" and "x00" not in [a, b]) or op == "XOR":
                for out2, eq2 in self.gates.items():
                    c, op2, d = re.findall(r"(\w{3}) (AND|OR|XOR) (\w{3})", eq2)[0]
                    if output in {c, d} and (
                        op2 == "OR" if op == "XOR" else op2 != "OR"
                    ):
                        bad.add(output)
        return ",".join(sorted(bad))


if __name__ == "__main__":
    Day24().run()
