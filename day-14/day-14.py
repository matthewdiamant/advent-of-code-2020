def mask_instruction(instruction, mask):
    binary = "{0:b}".format(instruction).zfill(36)
    masked_binary = []
    for i, bit in enumerate(binary):
        if mask[i] != 'X':
            masked_binary.append(mask[i])
        else:
            masked_binary.append(bit)

    return int("".join(masked_binary), 2)

def parse_instruction(instruction):
    address = instruction[4:instruction.index(']')].strip()
    value = instruction[instruction.index('=') + 1:].strip()
    return [int(address), int(value)]

def create_instruction_groups(input):
    instruction_groups = []
    instruction_group = []
    for instruction in input:
        if instruction[0:4] == "mask":
            instruction_groups.append(instruction_group)
            instruction_group = []
        instruction_group.append(instruction)
    instruction_groups.append(instruction_group)
    return instruction_groups[1:]

def solve_part_1(input):
    PROGRAM = {}
    instruction_groups = create_instruction_groups(input)
    for instruction_group in instruction_groups:
        mask = instruction_group[0]
        instructions = instruction_group[1:]
        for instruction in instructions:
            address, value = parse_instruction(instruction)
            PROGRAM[address] = mask_instruction(value, mask[7:])
    return sum(PROGRAM.values())

def apply_floating_bits(masked_binary, x_count, i):
    for bit in "{0:b}".format(i).zfill(x_count):
        x_index = masked_binary.index('X')
        masked_binary[x_index] = bit
    return int("".join(masked_binary), 2)

def mask_addresses(address, mask):
    binary = "{0:b}".format(address).zfill(36)
    masked_binary = []
    for i, bit in enumerate(binary):
        if mask[i] != '0':
            masked_binary.append(mask[i])
        else:
            masked_binary.append(bit)

    x_count = "".join(masked_binary).count('X')
    return [apply_floating_bits(masked_binary.copy(), x_count, i) for i in range(2 ** x_count)]

def solve_part_2(input):
    PROGRAM = {}
    instruction_groups = create_instruction_groups(input)
    for instruction_group in instruction_groups:
        mask = instruction_group[0]
        instructions = instruction_group[1:]
        for instruction in instructions:
            address, value = parse_instruction(instruction)
            masked_addresses = mask_addresses(address, mask[7:])
            for masked_address in masked_addresses:
                PROGRAM[masked_address] = value
    return sum(PROGRAM.values())

with open("./input.txt") as f:
    input = f.read().splitlines()
    print(solve_part_1(input))
    print(solve_part_2(input))
