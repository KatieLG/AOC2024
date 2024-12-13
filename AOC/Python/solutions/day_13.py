from __future__ import annotations

import re
from math import lcm

from models.aoc_solution import AOCSolution


class Day13(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 480, "data": 31589},
        "part_two": {"sample": 875318608908, "data": 98080815200063},
    }

    def __post_init__(self) -> None:
        self.machines = [
            tuple(map(int, re.findall(r"-?\d+", group)))
            for group in self.data.split("\n\n")
        ]

    def min_cost(self, machine: tuple[int, ...]) -> int:
        ax, ay, bx, by, tx, ty = machine
        lcmx = lcm(ax, ay)
        mx, my = lcmx // ax, lcmx // ay
        coef_y = bx * mx - by * my
        total = tx * mx - ty * my

        if total % coef_y == 0:
            b_uses = total // coef_y
            remaining = tx - b_uses * bx
            if remaining % ax == 0:
                return 3 * remaining // ax + b_uses
        return 0

    def part_one(self) -> int:
        return sum(self.min_cost(machine) for machine in self.machines)

    def part_two(self) -> int:
        offset = 10000000000000
        return sum(
            self.min_cost((ax, ay, bx, by, tx + offset, ty + offset))
            for ax, ay, bx, by, tx, ty in self.machines
        )


if __name__ == "__main__":
    Day13().run()