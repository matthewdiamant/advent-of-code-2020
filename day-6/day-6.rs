use std::collections::HashSet;
use std::iter::FromIterator;

static INPUT: &str = include_str!("./input.txt");
static ALL_ANSWERS: &str = "abcdefghijklmnopqrstuvwxyz";

fn main() {
    let input: Vec<Vec<&str>> = INPUT
        .split("\n\n")
        .map(|group| group.trim().split('\n').collect())
        .collect();
    println!("{:?}", solve_part_1(&input));
    println!("{:?}", solve_part_2(&input));
}

fn solve_part_1(answer_groups: &[Vec<&str>]) -> usize {
    answer_groups
        .iter()
        .map(|answer_group| union_count(answer_group))
        .sum()
}

fn solve_part_2(answer_groups: &[Vec<&str>]) -> usize {
    answer_groups
        .iter()
        .map(|answer_group| intersection_count(answer_group))
        .sum()
}

fn union_count(answer_group: &[&str]) -> usize {
    answer_sets(answer_group)
        .iter()
        .fold(HashSet::new(), |union, set| {
            union.union(&set).copied().collect()
        })
        .len()
}

fn intersection_count(answer_group: &[&str]) -> usize {
    answer_sets(answer_group)
        .iter()
        .fold(
            ALL_ANSWERS.chars().collect::<HashSet<_>>(),
            |intersection, set| intersection.intersection(&set).copied().collect(),
        )
        .len()
}

fn answer_sets(answer_group: &[&str]) -> Vec<HashSet<char>> {
    answer_group
        .iter()
        .map(|answers| HashSet::from_iter(answers.chars()))
        .collect()
}
