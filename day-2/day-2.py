def solve_part_1(entries):
    valid_count = 0
    for entry in entries:
        char_range, char, password = entry.split(' ')
        low_range, high_range = char_range.split('-')
        char_count = password.count(char[0])
        if char_count >= int(low_range) and char_count <= int(high_range):
            valid_count += 1
    return valid_count

def solve_part_2(entries):
    valid_count = 0
    for entry in entries:
        char_positions, char, password = entry.split(' ')
        char_index_1, char_index_2 = char_positions.split('-')
        char_1 = password[int(char_index_1) - 1]
        char_2 = password[int(char_index_2) - 1]
        char = char[0]
        if char_1 == char or char_2 == char:
            if char_1 != char_2:
                valid_count += 1
    return valid_count

with open('./input.txt') as f:
    entries = f.read().splitlines()
    print(solve_part_1(entries))
    print(solve_part_2(entries))
