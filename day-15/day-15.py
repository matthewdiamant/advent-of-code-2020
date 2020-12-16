def get_nth(n, numbers):
    recent_occurences = {}
    last_number = numbers[-1]

    for turn in range(len(numbers) - 1):
        recent_occurences[numbers[turn]] = turn

    for turn in range(len(numbers), n):
        matching_last = recent_occurences.get(last_number)
        if matching_last == None:
            recent_occurences[last_number] = turn - 1
            last_number = 0
        else:
            recent_occurences[last_number] = turn - 1
            last_number = turn - matching_last - 1

    return last_number

def solve_part_1(numbers):
    return get_nth(2020, numbers)

def solve_part_2(numbers):
    return get_nth(30_000_000, numbers)

with open("./input.txt") as f:
    input = [int(n) for n in f.read().strip().split(',')]
    print(solve_part_1(input))
    print(solve_part_2(input))
