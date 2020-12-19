from copy import deepcopy

def parse_field(instruction):
    name, ranges = instruction.split(":")
    first_range, second_range = ranges.split(" or ")
    first_range_start, first_range_end = first_range.split("-")
    second_range_start, second_range_end = second_range.split("-")
    return {
        "name": name,
        "first_range": range(int(first_range_start), int(first_range_end) + 1),
        "second_range": range(int(second_range_start), int(second_range_end) + 1)
    }

def parse_instructions(instructions):
    return [parse_field(field) for field in instructions]

def parse_valid_ranges(parsed_instructions):
    valid_ranges = set()
    for instructions in parsed_instructions:
        for value in instructions["first_range"]:
            valid_ranges.add(value)
        for value in instructions["second_range"]:
            valid_ranges.add(value)
    return valid_ranges

def add_invalid_values(tickets, valid_ranges):
    sum = 0
    for ticket in tickets[1:]:
        values = [int(value.strip()) for value in ticket.split(',')]
        for value in values:
            if not value in valid_ranges:
                sum += value
    return sum

def solve_day_1(input):
    instructions, my_ticket, nearby_tickets = input.split("\n\n")
    instructions = instructions.split("\n")
    parsed_instructions = parse_instructions(instructions)
    valid_ranges = parse_valid_ranges(parsed_instructions)
    nearby_tickets = nearby_tickets.split("\n")
    return add_invalid_values(nearby_tickets, valid_ranges)

def narrow_down_remaining_fields(possible_fields):
    done = False
    while not done:
        done = True
        for possible_field in possible_fields:
            if len(possible_field) == 1:
                for field in possible_fields:
                    for x in field:
                        if field != possible_field and possible_field[0] == x:
                            done = False
                            field.remove(x)
    return possible_fields

def determine_fields(valid_tickets, parsed_instructions):
    possible_fields = []
    for _ in range(len(valid_tickets[0])):
        possible_fields.append(deepcopy(parsed_instructions))

    for valid_ticket in valid_tickets:
        for i, value in enumerate(valid_ticket):
            fields = possible_fields[i]
            for test_field in fields:
                if not value in test_field["first_range"] and not value in test_field["second_range"]:
                    fields.remove(test_field)

    possible_fields = narrow_down_remaining_fields(possible_fields)

    return [possible_field[0] for possible_field in possible_fields]

def get_valid_tickets(tickets, valid_ranges):
    valid_tickets = []
    for ticket in tickets[1:]:
        values = [int(value.strip()) for value in ticket.split(',')]
        invalid_values = [value for value in values if not value in valid_ranges]
        if len(invalid_values) == 0:
            valid_tickets.append(values)
    return valid_tickets

def depature_value_product(my_ticket, fields):
    prod = 1
    for i, field in enumerate(fields):
        if field["name"][:9] == "departure":
            prod *= my_ticket[i]
    return prod

def solve_day_2(input):
    instructions, my_ticket, nearby_tickets = input.split("\n\n")
    instructions = instructions.split("\n")
    my_ticket = [int(value) for value in my_ticket.split("\n")[1].split(",")]
    parsed_instructions = parse_instructions(instructions)
    valid_ranges = parse_valid_ranges(parsed_instructions)
    nearby_tickets = nearby_tickets.split("\n")
    valid_tickets = get_valid_tickets(nearby_tickets, valid_ranges)
    fields = determine_fields(valid_tickets, parsed_instructions)

    return depature_value_product(my_ticket, fields)

with open("./input.txt") as f:
    input = f.read().strip()
    print(solve_day_1(input))
    print(solve_day_2(input))
