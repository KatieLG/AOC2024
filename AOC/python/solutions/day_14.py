import re
from collections import defaultdict

from models.aoc_solution import AOCSolution


class Day14(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 12, "data": 222208000},
        "part_two": {"sample": 0, "data": 7623},
    }

    def __post_init__(self) -> None:
        """Sample uses a smaller grid"""
        self.sample = len(self.data.splitlines()) < 20
        self.width = 11 if self.sample else 101
        self.height = 7 if self.sample else 103
        self.robots = [
            tuple(map(int, re.findall(r"-?\d+", line)))
            for line in self.data.splitlines()
        ]

    def part_one(self) -> int:
        """Find product of robots in each quadrant after 100 moves"""
        ends = [
            ((x + dx * 100) % self.width, (y + dy * 100) % self.height)
            for x, y, dx, dy in self.robots
        ]
        lu = ru = ld = rd = 0
        mw = self.width // 2
        mh = self.height // 2
        for x, y in ends:
            lu += x < mw and y < mh
            ru += x > mw and y < mh
            ld += x < mw and y > mh
            rd += x > mw and y > mh
        return lu * ru * ld * rd

    @staticmethod
    def find_start_period(
        vectors: list[tuple[int, int]], max_pos: int
    ) -> tuple[int, int]:
        """Given a list of (u, du) find the period where 30 or more line up"""
        start = period = 0
        for moves in range(1000):
            pos = defaultdict(int)
            for u, du in vectors:
                pos[(u + du * moves) % max_pos] += 1
            if max(pos.values()) >= 30:
                if not start:
                    start = moves
                else:
                    period = moves - start
                if start and period:
                    return start, period
        return 0, 0

    def part_two(self) -> int:
        """Sometimes robots line up vertically or horizontally, find the first time
        and the period of this happening, and where the two alignments overlap, return moves"""
        if self.sample:
            return 0
        xs, xp = self.find_start_period(
            [(x, dx) for x, _, dx, _ in self.robots], self.width
        )
        ys, yp = self.find_start_period(
            [(y, dy) for _, y, _, dy in self.robots], self.height
        )
        for x in range(xp):
            total = xs - ys + xp * x
            if total % yp == 0:
                return xs + xp * x
        return 0


if __name__ == "__main__":
    Day14().run()
