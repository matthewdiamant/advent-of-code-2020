D = ['N', 'E', 'S', 'W']

def navigate(direction):
    if direction[0] == 'N':
        return [0, int(direction[1:])]
    if direction[0] == 'S':
        return [0, -int(direction[1:])]
    if direction[0] == 'E':
        return [int(direction[1:]), 0]
    if direction[0] == 'W':
        return [-int(direction[1:]), 0]

def solve_day_1(instructions):
    bearing = 'E'
    x = 0
    y = 0
    for instruction in instructions:
        if instruction[0] not in D and instruction[0] != 'F':
            if instruction[0] == 'R':
                turns = int(int(instruction[1:]) / 90)
                bearing = D[(D.index(bearing) + turns) % len(D)]
                instruction = instruction.replace('R', bearing)
            if instruction[0] == 'L':
                turns = int(int(instruction[1:]) / 90)
                bearing = D[(D.index(bearing) - turns) % len(D)]
                instruction = instruction.replace('L', bearing)
        else:
            if instruction[0] == 'F':
                instruction = instruction.replace('F', bearing)
            d = navigate(instruction)
            x += d[0]
            y += d[1]
    return abs(x) + abs(y)


def solve_day_2(instructions):
    x = 0
    y = 0
    waypoint_x = 10
    waypoint_y = 1
    for instruction in instructions:
        if instruction[0] in D:
            d = navigate(instruction)
            waypoint_x += d[0]
            waypoint_y += d[1]
        elif instruction[0] == 'F':
            for _ in range(int(instruction[1:])):
                x += waypoint_x
                y += waypoint_y
        elif instruction[0] == 'R':
            for _ in range(int(int(instruction[1:]) / 90)):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif instruction[0] == 'L':
            for _ in range(int(int(instruction[1:]) / 90)):
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
    return abs(x) + abs(y)

with open("./input.txt") as f:
    input = f.read().splitlines()
    print(solve_day_1(input))
    print(solve_day_2(input))
