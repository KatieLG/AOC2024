from collections import defaultdict
from functools import cached_property

from models.aoc_solution import AOCSolution


class Day23(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 7, "data": 1230},
        "part_two": {
            "sample": "co,de,ka,ta",
            "data": "az,cj,kp,lm,lt,nj,rf,rx,sn,ty,ui,wp,zo",
        },
    }

    def __post_init__(self) -> None:
        self.connections = [tuple(line.split("-")) for line in self.data.splitlines()]
        self.__dict__.pop("groups", None)

    @cached_property
    def groups(self) -> dict[str, set[str]]:
        groups: dict[str, set[str]] = defaultdict(set)
        for a, b in self.connections:
            groups[a] |= {b}
            groups[b] |= {a}
        return groups

    def part_one(self) -> int:
        threes = {
            tuple(sorted((computer, conn1, conn2)))
            for computer in self.groups
            for conn1 in self.groups[computer]
            for conn2 in self.groups[conn1]
            if computer in self.groups[conn2]
        }
        return sum((any(computer[0] == "t" for computer in three)) for three in threes)

    def part_two(self) -> str:
        connected_groups: set[tuple[str, ...]] = set()
        for comp, connections in self.groups.items():
            connected_group = {comp}
            for conn in connections:
                if all(nbr in self.groups[conn] for nbr in connected_group):
                    connected_group |= {conn}
            connected_groups.add(tuple(sorted(connected_group)))
        biggest = max(connected_groups, key=len)
        return ",".join(biggest)


if __name__ == "__main__":
    Day23().run()
