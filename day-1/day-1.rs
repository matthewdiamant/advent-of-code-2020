fn solve_part_1(numbers: &Vec<i64>) -> i64 {
    for a in numbers {
        for b in numbers {
            if a + b == 2020 {
                return a * b;
            }
        }
    }
    return 0;
}

fn solve_part_2(numbers: &Vec<i64>) -> i64 {
    for a in numbers {
        for b in numbers {
            for c in numbers {
                if a + b + c == 2020 {
                    return a * b * c;
                }
            }
        }
    }
    return 0;
}

static INPUT: &str = include_str!("input.txt");
fn main() {
    let input: Vec<i64> = INPUT.lines().map(|x| x.parse().unwrap()).collect();
    println!("{}", solve_part_1(&input));
    println!("{}", solve_part_2(&input));
}
