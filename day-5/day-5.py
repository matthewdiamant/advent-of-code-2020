def row(partitioning):
    return int(partitioning[0:7].replace('F', '0').replace('B', '1'), 2)

def column(partitioning):
    return int(partitioning[7:10].replace('L', '0').replace('R', '1'), 2)

def seat_id(row, column):
    return row * 8 + column

def seat_ids(seats):
    return [seat_id(row(seat), column(seat)) for seat in seats]

def all_seat_ids(seats):
    return list(range(max(seats) + 1)[min(seats):])

def missing_seat(seats, all_seats):
    return [id for id in all_seats if id not in set(seats)][0]

def solve_part_1(seats):
    return max(seat_ids(seats))

def solve_part_2(seats):
    ids = seat_ids(seats)
    return missing_seat(ids, all_seat_ids(ids))

with open('./input.txt') as f:
    input = f.read().splitlines()
    print(solve_part_1(input))
    print(solve_part_2(input))
