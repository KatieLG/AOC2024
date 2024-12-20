from typing import Callable


def find_char[T](grid: list[list[T]], char: T) -> tuple[int, int]:
    """Find a particular character in a 2D grid"""
    return next(
        (x, y)
        for y, row in enumerate(grid)
        for x, cell in enumerate(row)
        if cell == char
    )


def nbrs[T](
    grid: list[list[T]], invalid_tiles: set[T], x: int, y: int
) -> list[tuple[int, int]]:
    """Find valid neighbours of a point in a 2D grid given a list of blocking tiles"""
    width, height = len(grid[0]), len(grid)
    return [
        (x2, y2)
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
        if 0 <= x2 < width and 0 <= y2 < height and grid[y][x] not in invalid_tiles
    ]


def costs[T](
    grid: list[list[T]],
    invalid_tiles: set[T],
    start: tuple[int, int],
    nbrs_func: Callable[
        [list[list[T]], set[T], int, int], list[tuple[int, int]]
    ] = nbrs,
) -> list[list[int]]:
    """Traverse a grid marking distance costs"""
    width, height = len(grid[0]), len(grid)
    cost_grid = [[-1 for _ in range(width)] for _ in range(height)]

    def traverse(x: int, y: int, cost: int = 0) -> None:
        cost_grid[y][x] = cost
        for x2, y2 in nbrs_func(grid, invalid_tiles, x, y):
            if cost_grid[y2][x2] == -1 or cost + 1 < cost_grid[y2][x2]:
                traverse(x2, y2, cost + 1)

    traverse(*start)
    return cost_grid
