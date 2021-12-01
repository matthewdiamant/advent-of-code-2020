import unittest

class Rule:
    def __init__(self, rule_definition):
        [self.name, self.rules] = rule_definition.split(':')
        self.is_base_rule = '"' in rule_definition
        child_definitions = self.rules.strip().split('|')
        self.child_rule_names = map(lambda r: r.strip().split(' '), child_definitions)
        self.child_rules = []

    def __repr__(self):
        return str(self.child_rule_names)

    def assign_child_rules(self, rule_dictionary):
        if not self.is_base_rule:
            self.child_rules = map(
                lambda cr: map(
                    lambda name: rule_dictionary[name], cr
                ), self.child_rule_names
            )

def parse_input(input):
    [rule_group, message_group] = input.strip().split('\n\n')
    rule_definitions = rule_group.split('\n')
    messages = message_group.split('\n')
    rules = map(Rule, rule_definitions)
    rule_dictionary = {}
    for rule in rules:
        rule_dictionary[rule.name] = rule
    for rule in rules:
        rule.assign_child_rules(rule_dictionary)

    return (rule_dictionary, messages)

def traverse(rule):
    if rule.is_base_rule:
        return rule.rules[2]
    forks = []
    for fork in rule.child_rules:
        perms = []
        for next_rule in fork:
            perms.append(traverse(next_rule))
        things = []
        for x in perms[0]:
            for y in perms[1]:
                things.append(x[0] + y[0])
        forks.append(things)
    return forks

def solve(input):
    rules, messages = parse_input(input)
    rule_zero = rules['0']
    permutations = traverse(rule_zero)[0]
    print(permutations)

# TESTS

sample_1 = """
0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"

aab
aba
"""

sample_2 = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_rule(self):
        self.assertEqual(Rule('0: 1 2').name, '0')
        self.assertEqual(Rule('0: 1 2').is_base_rule, False)
        self.assertEqual(Rule('0: "a"').is_base_rule, True)
        self.assertEqual(Rule('0: 1 2').child_rule_names, [['1', '2']])
        self.assertEqual(Rule('2: 1 3 | 3 1').child_rule_names, [['1', '3'], ['3', '1']])

    def test_parse_input(self):
        self.assertEqual(len(parse_input(sample_1)[0]), 4)
        self.assertEqual(parse_input(sample_1)[1], ['aab', 'aba'])

    def test_solve_part_1_sample_1(self):
        self.assertEqual(solve(sample_1), None)

    def test_solve_part_1_sample_2(self):
        self.assertEqual(solve(sample_2), None)

    def test_solve_part_1_input(self):
        # self.assertEqual(solve(input), 0)
        pass

unittest.main()
