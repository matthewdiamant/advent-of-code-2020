import math

X = 0
Y = 1

SLOPES = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

def solve_part_1(forest, slope):
    trees = 0
    x = slope[X] * -1
    for index, row in enumerate(forest):
        if index % slope[Y] == 0:
            x += slope[X]
            if row[x % len(row)] == '#':
                trees += 1
    return trees

def solve_part_2(forest):
    trees_per_slope = []
    for slope in SLOPES:
        trees = solve_part_1(forest, slope)
        trees_per_slope.append(trees)
    return math.prod(trees_per_slope)

with open('./input.txt') as f:
    forest = f.read().splitlines()
    print(solve_part_1(forest, [3, 1]))
    print(solve_part_2(forest))
