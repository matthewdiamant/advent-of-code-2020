static INPUT: &str = include_str!("input.txt");
static SLOPES: [[i32; 2]; 5] = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
];

fn solve_part_1(forest: &Vec<String>, slope: &[i32]) -> i32 {
    let mut trees = 0;
    let mut x = slope[0] * -1;
    for (index, row) in forest.iter().enumerate() {
        if index as i32 % slope[1] == 0 {
            x += slope[0];
            if row.chars().nth(x as usize % row.len()) == Some('#') {
                trees += 1;
            }
        }
    }
    return trees;
}

fn solve_part_2(forest: &Vec<String>) -> usize {
    let trees_per_slope = SLOPES.iter().map(|slope| solve_part_1(forest, slope) as usize);
    return trees_per_slope.product();
}

fn main() {
    let input: Vec<String> = INPUT.lines().map(|x| x.parse().unwrap()).collect();
    println!("{}", solve_part_1(&input, &[3, 1]));
    println!("{}", solve_part_2(&input));
}
