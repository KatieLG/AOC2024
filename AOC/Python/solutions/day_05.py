from models.aoc_solution import AOCSolution


class Day05(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 143, "data": 4662},
        "part_two": {"sample": 123, "data": 5900},
    }

    def __post_init__(self) -> None:
        rules, updates = map(str.splitlines, self.data.split("\n\n"))
        self.rules = {tuple(map(int, rule.split("|"))) for rule in rules}
        self.updates = [list(map(int, update.split(","))) for update in updates]

    def invalid_positions(self, update: list[int]) -> tuple[int, int] | None:
        """Find first invalid position (if any) baded on the ordering rules"""
        for i, page in enumerate(update):
            for j, after in enumerate(update[i + 1 :], start=i + 1):
                if (after, page) in self.rules:
                    return i, j

    def part_one(self) -> int:
        """Sum the middle number of valid updates"""
        return sum(
            update[len(update) // 2]
            for update in self.updates
            if not self.invalid_positions(update)
        )

    def part_two(self) -> int:
        """Sum the middle number of fixed invalid updates"""
        total = 0
        for update in self.updates:
            if not (coords := self.invalid_positions(update)):
                continue
            while coords:
                i, j = coords
                update[i], update[j] = update[j], update[i]
                coords = self.invalid_positions(update)
            total += update[len(update) // 2]
        return total


if __name__ == "__main__":
    Day05().run()
