static INPUT: &str = include_str!("./input.txt");

fn main() {
    let input: Vec<usize> = INPUT.split('\n').map(|joltage| joltage.parse().unwrap()).collect();
    println!("{}", solve_day_1(input));
}

fn solve_day_1(adapters: Vec<usize>) -> usize {
    let sorted = sorted_adapters(adapters);
    return 0;
}
fn sorted_adapters(mut adapters: Vec<usize>) -> Vec<usize> {
    adapters.sort();
    let mut a: Vec<usize> = vec![0];
    let b: Vec<usize> = vec![adapters.last().unwrap() + 3];
    a.extend(&adapters);
    a.extend(&b);
    return a;
}
