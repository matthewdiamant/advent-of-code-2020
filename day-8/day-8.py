from copy import deepcopy

ITERATION_LIMIT = 200

class BootCode:

    def __init__(self, ops):
        self.acc = 0
        self.ops = ops
        self.program_counter = 0
        self.seen_instructions = set()
        self.iterations = 0

    def OPS(self):
        return {
            "acc": self.execute_acc,
            "jmp": self.execute_jmp,
            "nop": self.execute_nop,
        }

    def run(self):
        while(self.iterations < ITERATION_LIMIT):
            self.execute(self.ops[self.program_counter])
            self.iterations += 1
            if (self.program_counter == len(self.ops)):
                return 0
        return 1

    def run_until_repeat_instruction(self):
        while(self.program_counter not in self.seen_instructions):
            self.seen_instructions.update([self.program_counter])
            self.execute(self.ops[self.program_counter])

    def execute(self, op):
        self.OPS()[op["op"]](op["value"])

    def execute_acc(self, value):
        self.acc += value
        self.program_counter += 1

    def execute_jmp(self, value):
        self.program_counter += value

    def execute_nop(self, value):
        self.program_counter += 1

def parse_ops(ops):
    return [parse_op(op_text) for op_text in ops]

def parse_op(op):
    return {
        "op": op.split(" ")[0],
        "value": int(op.split(" ")[1]),
    }

def solve_part_1(ops_text):
    boot_code = BootCode(parse_ops(ops_text))
    boot_code.run_until_repeat_instruction()
    return boot_code.acc

def solve_part_2(ops_text):
    ops = parse_ops(ops_text)

    for op in range(len(ops)):
        mod_ops = deepcopy(ops)
        if mod_ops[op]["op"] == "nop":
            mod_ops[op]["op"] = "jmp"
        elif mod_ops[op]["op"] == "jmp":
            mod_ops[op]["op"] = "nop"
        else:
            continue

        boot_code = BootCode(mod_ops)
        if boot_code.run() == 0:
            return boot_code.acc

with open("./input.txt") as f:
    input = f.read().splitlines()
    print(solve_part_1(input))
    print(solve_part_2(input))
