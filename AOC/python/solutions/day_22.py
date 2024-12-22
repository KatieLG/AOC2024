from functools import cache

from models.aoc_solution import AOCSolution


class Day22(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 37327623, "data": 14726157693},
        "part_two": {"sample": 0, "data": 0},
    }

    def __post_init__(self) -> None:
        self.secrets = list(map(int, self.data.splitlines()))

    @staticmethod
    def mix_and_prune(a: int, b: int) -> int:
        return (a ^ b) % 16777216

    @cache
    def process(self, secret: int):
        secret = self.mix_and_prune(secret, secret * 64)
        secret = self.mix_and_prune(secret, secret // 32)
        secret = self.mix_and_prune(secret, secret * 2048)
        return secret

    def part_one(self) -> int:
        secrets = self.secrets
        for _ in range(2000):
            secrets = [self.process(secret) for secret in secrets]
        return sum(secrets)

    def part_two(self) -> int:
        return 0


if __name__ == "__main__":
    Day22().run()
