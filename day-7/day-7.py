def parse_bag_count(bag):
    return int(bag.strip()[0])

def parse_subbag_name(bag):
    return " ".join(bag.strip()[2:].split(" ")[:2])

def parse_bag_name(bag):
    return " ".join(bag.strip().split(" ")[:2])

def parse_subbag(subbag):
    return {"name": parse_subbag_name(subbag), "count": parse_bag_count(subbag)}

def parse_subbags(subbags):
    if subbags == "no other bags.":
        return []
    else:
        return [parse_subbag(subbag) for subbag in subbags[:-1].split(",")]

def parse_bag(rule):
    return {"bag": parse_bag_name(rule[0]), "subbags": parse_subbags(rule[1])}

def parse_rules(definitions):
    return [parse_bag(rule.split(" contain ")) for rule in definitions]

class BagFinder():
    def __init__(self, rules):
        self.rules = rules
        self.valid_bags = {}

    def can_contain_bag(self, bag_name):
        container_bags = []
        for bag in self.rules:
            if (any(subbag["name"] == bag_name for subbag in bag["subbags"])):
                    container_bags.append(bag)
        return container_bags

    def find_new_bags(self, bags_to_check):
        new_bags = set()

        for bag in bags_to_check:
            new_bags |= set(subbag["bag"] for subbag in self.can_contain_bag(bag))

        new_bags_to_check = new_bags - self.valid_bags
        self.valid_bags |= new_bags

        return new_bags_to_check

    def get_possible_containing_bags(self):
        self.valid_bags = {bag["bag"] for bag in self.can_contain_bag("shiny gold")}

        bags_to_check = self.valid_bags
        while (len(bags_to_check)):
            bags_to_check = self.find_new_bags(bags_to_check)

        return len(self.valid_bags)

def find_bag(bag_name, rules):
    bag = None
    for bag_rule in rules:
        if bag_rule["bag"] == bag_name:
            bag = bag_rule
            break
    return bag

def count_subbags(bag_name, count, rules):
    bag = find_bag(bag_name, rules)
    if len(bag["subbags"]) == 0: return count
    sum_of_subbags = sum([count_subbags(subbag["name"], subbag["count"], rules) for subbag in bag["subbags"]])
    return count * sum_of_subbags + count

def solve_part_1(definitions):
    rules = parse_rules(definitions)
    bag_finder = BagFinder(rules)
    return bag_finder.get_possible_containing_bags()

def solve_part_2(definitions):
    rules = parse_rules(definitions)
    return count_subbags("shiny gold", 1, rules) - 1

with open("./input.txt") as f:
    input = f.read().splitlines()
    print(solve_part_1(input))
    print(solve_part_2(input))
