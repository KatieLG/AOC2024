from collections import deque
from itertools import chain

from models.aoc_solution import AOCSolution


class Day09(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 1928, "data": 6378826667552},
        "part_two": {"sample": 2858, "data": 6413328569890},
    }

    def __post_init__(self) -> None:
        self.groups = [
            ["." if i % 2 else str(i // 2)] * int(k) for i, k in enumerate(self.data)
        ]
        self.blocks = list(chain.from_iterable(self.groups))

    def compact(self) -> list[str]:
        file_blocks = deque([b for b in self.blocks if b != "."])
        i = 0
        compact: list[str] = []
        while file_blocks:
            if self.blocks[i] == ".":
                compact.append(file_blocks.pop())
            else:
                compact.append(file_blocks.popleft())
            i += 1
        return compact

    @staticmethod
    def checksum(items: list[str]) -> int:
        idx = total = 0
        for item in items:
            if item.isnumeric():
                total += int(item) * idx
            idx += 1
        return total

    def group_compact(self) -> list[str]:
        """Defer moves that would modify list size until the end"""
        deferred_moves: list[tuple[int, list[str]]] = []
        for f, file_group in reversed(list(enumerate(self.groups))):
            if not file_group or "." in file_group:
                continue
            for g, group in enumerate(self.groups[:f]):
                if "." in group and len(group) >= len(file_group):
                    self.groups[f] = ["."] * len(file_group)
                    if len(group) == len(file_group):
                        self.groups[g] = file_group
                    else:
                        deferred_moves.append((g, file_group))
                        self.groups[g] = self.groups[g][len(file_group) :]
                    break
        for idx, group in sorted(
            deferred_moves, key=lambda x: (x[0], len(x[1])), reverse=True
        ):
            self.groups.insert(idx, group)
        return list(chain.from_iterable(self.groups))

    def part_one(self) -> int:
        compact = self.compact()
        return self.checksum(compact)

    def part_two(self) -> int:
        compact = self.group_compact()
        return self.checksum(compact)


if __name__ == "__main__":
    Day09().run()
