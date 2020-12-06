from functools import reduce
from operator import ior, iand

def answer_sets(answer_group):
    return [set(list(answers)) for answers in answer_group]

def union_count(answer_group):
    return len(reduce(ior, answer_sets(answer_group)))

def intersection_count(answer_group):
    return len(reduce(iand, answer_sets(answer_group)))

def solve_part_1(answer_groups):
    return sum([union_count(answer_group) for answer_group in answer_groups])

def solve_part_2(answer_groups):
    return sum([intersection_count(answer_group) for answer_group in answer_groups])

with open("./input.txt") as f:
    input = [group.strip().split("\n") for group in f.read().split("\n\n")]
    print(solve_part_1(input))
    print(solve_part_2(input))
