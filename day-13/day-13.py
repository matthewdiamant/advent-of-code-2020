def solve_part_1(input):
    time = int(input[0])
    buses = [int(bus) for bus in input[1].split(',') if bus != 'x']
    wait_time = buses[0]
    chosen_bus = None
    for bus in buses:
        if bus - (time % bus) < wait_time:
            wait_time = bus - (time % bus)
            chosen_bus = bus
    return chosen_bus * wait_time

# Part 2 requires some Chinese Remainder Theorem stuff that I never
#  learned in school, so I skipped it. Brute forcing is impossible.

with open("./input.txt") as f:
    input = f.read().splitlines()
    print(solve_part_1(input))
