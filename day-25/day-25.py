import unittest

DIVISOR = 20201227

def parse_input(input):
    [card, door] = input.strip().split('\n')
    return (int(card), int(door))

def transform(loop_size, subject_number=7):
    value = 1
    for _ in range(loop_size):
        value = (value * subject_number) % DIVISOR
    return value

def transform_until(target, subject_number=7):
    value = 1
    loop_size = 0
    while (value != target):
        value = (value * subject_number) % DIVISOR
        loop_size += 1
    return loop_size

def find_loop_size(public_key):
    return transform_until(public_key)

def solve(input):
    card_public, door_public = parse_input(input)
    card_loop_size = transform_until(card_public)
    door_loop_size = transform_until(door_public)
    return transform(card_loop_size, transform(door_loop_size))

# TESTS

sample = """5764801
17807724
"""

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(parse_input(sample), (5764801, 17807724))

    def test_transform(self):
        self.assertEqual(transform(8), 5764801)
        self.assertEqual(transform(11), 17807724)
        self.assertEqual(transform(8, transform(11)), 14897079)
        self.assertEqual(transform(11, transform(8)), 14897079)

    def test_transform_until(self):
        self.assertEqual(transform_until(5764801), 8)
        self.assertEqual(transform_until(17807724), 11)

    def test_solve_part_1_sample(self):
        self.assertEqual(solve(sample), 14897079)

    def test_solve_part_1_input(self):
        self.assertEqual(solve(input), 18329280)

unittest.main()
