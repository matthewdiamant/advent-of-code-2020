EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

def create_grid(input):
    return [[cell for cell in row] for row in input.splitlines()]

def in_bounds(dx, dy, grid):
    return (dx >= 0 and dy >= 0 and dy < len(grid) and dx < len(grid[dy]))

def get_directions(grid, y, x, ignore_floor):
    directions = []
    D = [1, 0, -1]
    for d in D:
        for d2 in D:
            if (d != 0 or d2 != 0):
                dy = y + d
                dx = x + d2
                z = grid[dy][dx] if in_bounds(dx, dy, grid) else 'x'

                if ignore_floor:
                    while z == FLOOR:
                        dy += d
                        dx += d2
                        z = grid[dy][dx] if in_bounds(dx, dy, grid) else 'x'
                directions.append(z)
    return list(directions)

def tick(grid, tolerance, ignore_floor):
    new_grid = []
    for y, row in enumerate(grid):
        new_row = []
        for x, cell in enumerate(row):
            if cell == FLOOR:
                new_row.append(FLOOR)
            else:
                directions = get_directions(grid, y, x, ignore_floor)
                if cell == EMPTY:
                    if directions.count(OCCUPIED) == 0:
                        new_row.append(OCCUPIED)
                    else:
                        new_row.append(EMPTY)

                if cell == OCCUPIED:
                    if directions.count(OCCUPIED) >= tolerance:
                        new_row.append(EMPTY)
                    else:
                        new_row.append(OCCUPIED)

        new_grid.append(new_row)
    return new_grid

def count_occupied(grid):
    i = 0
    for row in grid:
        for cell in row:
            if cell == OCCUPIED:
                i += 1
    return i

def run(grid, tolerance, ignore_floor):
    new_grid = tick(grid, tolerance, ignore_floor)
    while (new_grid != grid):
        grid = new_grid
        new_grid = tick(grid, tolerance, ignore_floor)

    return grid

def solve_part_1(input):
    grid = run(create_grid(input), 4, False)
    return count_occupied(grid)

def solve_part_2(input):
    grid = run(create_grid(input), 5, True)
    return count_occupied(grid)

with open("./input.txt") as f:
    input = f.read()
    print(solve_part_1(input))
    print(solve_part_2(input))
