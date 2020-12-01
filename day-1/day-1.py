def solve_part_1(numbers):
    for a in numbers:
        for b in numbers:
            if (a + b == 2020):
                return a * b

def solve_part_2(numbers):
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if (a + b + c == 2020):
                    return a * b * c

with open('./input.txt') as f:
    numbers = [int(n) for n in f.read().splitlines()]
    print(solve_part_1(numbers))
    print(solve_part_2(numbers))
