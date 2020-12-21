import re

def strip_whitespace(text):
    return "".join(text.split())
def solve_part_1(equations):
    equations = [strip_whitespace(equation) for equation in equations]
    equation = equations[0]
    output = []
    operator = []
    for token in equation:
        if re.match(r"[0-9]", token):
            output.append(int(token))
        elif re.match(r"\(", token):
            operator.append(token)
        elif re.match(r"\)", token):
            pass
        else:
            while len(operator):

            operator.append(token)

with open("./input.txt") as f:
    input = f.read().splitlines()
    print(solve_part_1(input))
