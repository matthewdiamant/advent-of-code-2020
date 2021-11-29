import itertools
import unittest

def flatten(array):
    return list(itertools.chain(*array))

def neighbors(key):
    [x, y, z] = map(int, key.split(','))
    deltas = [-1, 0, 1]
    directions_nested = [[[[x + dx, y + dy, z + dz] for dz in deltas] for dy in deltas] for dx in deltas]
    directions_flat = flatten(flatten(directions_nested))
    directions_filtered = filter(lambda delta: delta != [x, y, z], directions_flat)
    return directions_filtered

def parse_input_to_grid(input):
    grid = {}
    lines = input.split('\n')
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            key = "{},{},0".format(x, y)
            grid[key] = val
    return grid

def solve_part_1(input):
    grid = parse_input_to_grid(input)

with open("./input.txt") as f:
    file = f.read()
    print(solve_part_1(file))

### TESTS

sample = """.#.
..#
###
"""

sample_grid = {
    '0,0,0': '.',
    '1,0,0': '#',
    '2,0,0': '.',
    '0,1,0': '.',
    '1,1,0': '.',
    '2,1,0': '#',
    '0,2,0': '#',
    '1,2,0': '#',
    '2,2,0': '#'
}

sample_neighbors = [[0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 2, 2], [0, 2, 3], [0, 2, 4], [0, 3, 2], [0, 3, 3], [0, 3, 4], [1, 1, 2], [1, 1, 3], [1, 1, 4], [1, 2, 2], [1, 2, 4], [1, 3, 2], [1, 3, 3], [1, 3, 4], [2, 1, 2], [2, 1, 3], [2, 1, 4], [2, 2, 2], [2, 2, 3], [2, 2, 4], [2, 3, 2], [2, 3, 3], [2, 3, 4]]

class Test(unittest.TestCase):

    def test_parse_input_to_grid(self):
        self.assertEqual(parse_input_to_grid(sample), sample_grid)

    def test_neighbors(self):
        self.assertEqual(neighbors('1,2,3'), sample_neighbors)

with open("./sample.txt") as f:
    sample = f.read()

unittest.main()
