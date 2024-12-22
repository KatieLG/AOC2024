from functools import cache

from models.aoc_solution import AOCSolution

type Seq = tuple[int, int, int, int]


class Day22(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 37327623, "data": 14726157693},
        "part_two": {"sample": 23, "data": 1614},
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

    def generate_prices(self, secret: int, count: int) -> list[int]:
        prices = [secret % 10]
        for _ in range(count):
            secret = self.process(secret)
            prices.append(secret % 10)
        return prices

    def difference_values(self, secret: int, count: int) -> dict[Seq, int]:
        """Generate all sequences of 4 integers"""
        prices = self.generate_prices(secret, count)
        differences = [prices[i + 1] - prices[i] for i in range(count - 1)]
        values: dict[Seq, int] = {}
        for i in range(count - 4):
            tup = (
                differences[i],
                differences[i + 1],
                differences[i + 2],
                differences[i + 3],
            )
            if tup not in values:
                values[tup] = prices[i + 4]
        return values

    def part_one(self) -> int:
        secrets = self.secrets
        for _ in range(2000):
            secrets = [self.process(secret) for secret in secrets]
        return sum(secrets)

    def part_two(self) -> int:
        """2000 changes = 2001 secret values"""
        dicts = [self.difference_values(secret, 2001) for secret in self.secrets]
        unique_seqs = {key for seq in dicts for key in seq}
        sales = {seq: sum(d[seq] for d in dicts if seq in d) for seq in unique_seqs}
        return max(sales.values())


if __name__ == "__main__":
    Day22().run()
