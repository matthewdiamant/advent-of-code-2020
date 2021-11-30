from itertools import chain
import unittest
import cProfile

def unique(array):
    return list(set(array))

def flatten(array):
    return list(chain(*array))

def neighbors(key):
    x, y, z = key
    deltas = [-1, 0, 1]
    directions_nested = [[[(x + dx, y + dy, z + dz) for dz in deltas] for dy in deltas] for dx in deltas]
    directions_flat = flatten(flatten(directions_nested))
    directions_filtered = filter(lambda delta: delta != (x, y, z), directions_flat)
    return directions_filtered

def parse_input_to_grid(input):
    grid = {}
    lines = input.split('\n')
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            key = (x, y, 0)
            grid[key] = val
    return grid

def candidates(grid):
    return unique(flatten([neighbors(key) for key in grid.keys()]))

def active(grid, key):
    candidate_neighbors = neighbors(key)
    active_neighbors = 0
    for neighbor in candidate_neighbors:
        neighbor_active = grid[neighbor] == "#" if grid.has_key(neighbor) else False
        active_neighbors += 1 if neighbor_active else 0
    active = grid[key] == "#" if grid.has_key(key) else False
    new_active = True if (active and (active_neighbors == 2)) or active_neighbors == 3 else False
    return new_active

def trim_side(grid, axis, direction):
    bound = get_bounds(grid, axis)[direction];
    face = filter(lambda c: int(c[axis]) == bound, grid.keys())
    while (len(filter(lambda c: grid[c] == '#', face)) == 0):
        for c in face:
            grid.pop(c, None)
        bound = get_bounds(grid, axis)[direction]
        face = filter(lambda c: int(c[axis]) == bound, grid.keys())

def trim_grid(grid):
    trim_side(grid, 0, 0)
    trim_side(grid, 0, 1)
    trim_side(grid, 1, 0)
    trim_side(grid, 1, 1)
    trim_side(grid, 2, 0)
    trim_side(grid, 2, 1)
    return grid

def epoch(grid):
    new_candidates = candidates(grid)
    new_grid = {}
    for key in new_candidates:
        candidate_active = active(grid, key)
        new_grid[key] = '#' if candidate_active else '.'
    return trim_grid(new_grid)

def get_bounds(grid, x):
    bounds = sorted(map(lambda key: key[x], grid.keys()))
    return [bounds[0], bounds[-1]]

def grid_to_string(grid):
    [low_z_bound, high_z_bound] = get_bounds(grid, 2);
    [low_y_bound, high_y_bound] = get_bounds(grid, 1);
    [low_x_bound, high_x_bound] = get_bounds(grid, 0);
    grid_output = ""
    for z in range(low_z_bound, high_z_bound + 1):
        grid_output += "z={}".format(z) + '\n'
        for y in range(low_y_bound, high_y_bound + 1):
            line_output = ""
            for x in range(low_x_bound, high_x_bound + 1):
                line_output += grid[(x, y, z)]
            grid_output += line_output + '\n'
        grid_output += '\n'
    return grid_output

def epochs(grid, times):
    new_grid = grid
    for _ in range(times):
        new_grid = epoch(new_grid)
    return new_grid

def count_active(grid):
    return len(filter(lambda val: val == "#", grid.values()))

def solve_part_1(input):
    grid = parse_input_to_grid(input)
    active = count_active(epochs(grid, 6))
    return active

with open("./input.txt") as f:
    file = f.read()
    print(solve_part_1(file))

### TESTS

sample = """.#.
..#
###
"""

sample_grid = {(1, 1, 0): '.', (2, 1, 0): '#', (0, 2, 0): '#', (1, 0, 0): '#', (2, 2, 0): '#', (1, 2, 0): '#', (0, 0, 0): '.', (0, 1, 0): '.', (2, 0, 0): '.'}

sample_neighbors = [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 2), (0, 2, 3), (0, 2, 4), (0, 3, 2), (0, 3, 3), (0, 3, 4), (1, 1, 2), (1, 1, 3), (1, 1, 4), (1, 2, 2), (1, 2, 4), (1, 3, 2), (1, 3, 3), (1, 3, 4), (2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 3, 2), (2, 3, 3), (2, 3, 4)]

sample_grid_string = 'z=0\n.#.\n..#\n###\n\n'

class Test(unittest.TestCase):

    def test_parse_input_to_grid(self):
        self.assertEqual(parse_input_to_grid(sample), sample_grid)

    def test_neighbors(self):
        self.assertEqual(neighbors((1, 2, 3)), sample_neighbors)

    def test_grid_to_string(self):
        grid = parse_input_to_grid(sample)
        self.assertEqual(grid_to_string(grid), sample_grid_string)

    def test_solve_part_1(self):
        self.assertEqual(solve_part_1(sample), 112)
        pass

unittest.main()
