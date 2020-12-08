static INPUT: &str = include_str!("./input.txt");

#[derive(Debug)]
struct Bag {
    name: String,
    subbags: Vec<Subbag>,
}

#[derive(Debug)]
struct Subbag {
    name: String,
    count: usize,
}

fn main() {
    let input: Vec<&str> = INPUT.lines().collect();
    println!("{:?}", solve_part_1(&input));
}

fn solve_part_1(definitions: &[&str]) {
    let rules = parse_rules(definitions);
    println!("{:#?}", rules);
}

fn parse_rules(definitions: &[&str]) -> Vec<Bag> {
    definitions
        .iter()
        .map(|rule| parse_rule(rule.split(" contain ").collect()))
        .collect()
}

fn parse_rule(rule: Vec<&str>) -> Bag {
    Bag {
        name: parse_bag_name(rule[0]),
        subbags: parse_subbags(rule[1]),
    }
}

fn parse_bag_name(bag_name: &str) -> String {
    bag_name.split(' ').collect::<Vec<&str>>()[0..2].join(" ")
}

fn parse_subbags(subbags: &str) -> Vec<Subbag> {
    if subbags == "no other bags." {
        vec![]
    } else {
        subbags[0..subbags.len() - 1]
            .split(',')
            .map(|subbag| parse_subbag(subbag))
            .collect::<Vec<Subbag>>()
    }
}

fn parse_subbag(subbag: &str) -> Subbag {
    Subbag {
        name: parse_subbag_name(subbag),
        count: parse_bag_count(subbag),
    }
}

fn parse_subbag_name(bag: &str) -> String {
    bag.trim()[2..bag.trim().len()]
        .split(' ')
        .collect::<Vec<&str>>()[0..2]
        .join(" ")
}

fn parse_bag_count(bag: &str) -> usize {
    bag.trim()[0..1].to_string().parse::<usize>().unwrap()
}
