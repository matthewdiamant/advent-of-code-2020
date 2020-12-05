use std::collections::HashMap;

static INPUT: &str = include_str!("./input.txt");
fn main() {
    let input: Vec<&str> = INPUT.lines().collect();
    println!("{}", solve_part_1(&input));
}

fn solve_part_1(input: &[&str]) -> usize {
    let passports = create_passports(&input);
    return 0;
}

fn create_passports(passport_lines: &[&str]) {
    let mut current_passport: Vec<&str> = vec![];
    let mut passports: Vec<Vec<&str>> = vec![];
    for passport_line in passport_lines {
        if passport_line != &"" {
            current_passport.push(passport_line);
        } else {
            passports.push(current_passport);
            current_passport = vec![];
        }
    }

    //    for passport in &passports {
    //        create_passport(&passport);
    //    }

    let mut passports_with_props: Vec<HashMap<&str, &str>> = vec![];
    for passport in passports {
        passports_with_props.push(create_passport(passport));
    }
    println!("{:?}", passports_with_props);
    // return passports_with_props;
}

fn create_passport(passport_lines: Vec<&str>) -> HashMap<&str, &str> {
    let mut passport = HashMap::new();
    for passport_line in passport_lines {
        let s: Vec<&str> = passport_line.split(" ").collect();
        for property in s {
            let key_and_value: Vec<&str> = property.split(":").collect();
            passport.insert(key_and_value[0], key_and_value[1]);
        }
    }
    return passport;
}
