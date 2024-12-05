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

    def is_valid_update(self, update: list[int]) -> bool:
        """Check if an update satisfies the ordering rules"""
        for i, page in enumerate(update):
            for after in update[i + 1 :]:
                if (after, page) in self.rules:
                    return False
        return True

    def part_fix_update(self, update: list[int]) -> list[int]:
        """Swap first two update elements that are in the wrong order"""
        for i, page in enumerate(update):
            for j, after in enumerate(update[i + 1 :], start=i + 1):
                if (after, page) in self.rules:
                    update[i], update[j] = after, page
                    return update
        return update

    def part_one(self) -> int:
        """Sum the middle number of valid updates"""
        return sum(
            update[len(update) // 2]
            for update in filter(self.is_valid_update, self.updates)
        )

    def part_two(self) -> int:
        """Sum the middle number of fixed invalid updates"""
        total = 0
        for update in self.updates:
            if self.is_valid_update(update):
                continue
            while not self.is_valid_update(update):
                update = self.part_fix_update(update)
            total += update[len(update) // 2]
        return total


if __name__ == "__main__":
    Day05().run()
