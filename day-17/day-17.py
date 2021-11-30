from itertools import chain
import unittest

def unique(array):
    return list(set(array))

def flatten(array):
    return list(chain(*array))

def parse_input_to_grid(input, dimensions):
    grid = set()
    lines = input.split('\n')
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            if val == "#":
                coord = (x, y, 0, 0) if dimensions == 4 else (x, y, 0)
                grid.add(coord)
    return grid

def neighbors(coord, dimensions):
    deltas = [-1, 0, 1]
    if dimensions == 4:
        x, y, z, w = coord
        directions_nested = [[[[(x + dx, y + dy, z + dz, w + dw) for dw in deltas] for dz in deltas] for dy in deltas] for dx in deltas]
        directions = flatten(flatten(flatten(directions_nested)))
    else:
        x, y, z = coord
        directions_nested = [[[(x + dx, y + dy, z + dz) for dz in deltas] for dy in deltas] for dx in deltas]
        directions = flatten(flatten(directions_nested))
    return filter(lambda delta: delta != coord, directions)

def candidates(grid, dimensions):
    return unique(flatten([neighbors(coord, dimensions) for coord in grid]))

def active(grid, coord, dimensions):
    active_neighbors = len(filter(lambda n: n in grid, neighbors(coord, dimensions)))
    return active_neighbors == 3 or (coord in grid and active_neighbors == 2)

def epoch(grid, dimensions):
    new_candidates = candidates(grid, dimensions)
    new_grid = set()
    for candidate in new_candidates:
        if active(grid, candidate, dimensions):
            new_grid.add(candidate)
    return new_grid

def epochs(grid, times, dimensions):
    for _ in range(times):
        grid = epoch(grid, dimensions)
    return grid

def solve(input, dimensions):
    grid = parse_input_to_grid(input, dimensions)
    return len(epochs(grid, 6, dimensions))

# TESTS

sample = """.#.
..#
###
"""

sample_grid = set([(1, 0, 0), (0, 2, 0), (1, 2, 0), (2, 1, 0), (2, 2, 0)])

sample_neighbors = [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 2), (0, 2, 3), (0, 2, 4), (0, 3, 2), (0, 3, 3), (0, 3, 4), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 2), (1, 2, 4), (1, 3, 2), (1, 3, 3), (1, 3, 4), (2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 3, 2), (2, 3, 3), (2, 3, 4)]

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_parse_input_to_grid(self):
        self.assertEqual(parse_input_to_grid(sample, 3), sample_grid)

    def test_neighbors(self):
        self.assertEqual(neighbors((1, 2, 3), 3), sample_neighbors)

    def test_solve_part_1_sample(self):
        self.assertEqual(solve(sample, 3), 112)

    def test_solve_part_2_sample(self):
        self.assertEqual(solve(sample, 4), 848)

    def test_solve_part_1_input(self):
        self.assertEqual(solve(input, 3), 382)

    def test_solve_part_2_input(self):
        self.assertEqual(solve(input, 4), 2552)

unittest.main()
