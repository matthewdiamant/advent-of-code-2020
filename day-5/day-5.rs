static INPUT: &str = include_str!("input.txt");

fn main() {
    let input: Vec<&str> = INPUT.lines().collect();
    println!("{}", solve_part_1(&input));
    println!("{}", solve_part_2(&input));
}

fn solve_part_1(seats: &[&str]) -> usize {
    *seat_ids(seats).iter().max().unwrap()
}

fn solve_part_2(seats: &[&str]) -> usize {
    let ids = seat_ids(seats);
    missing_seat(&ids, &all_seat_ids(&ids))
}

fn seat_ids(seats: &[&str]) -> Vec<usize> {
    seats
        .iter()
        .map(|seat| seat_id(row(seat), column(seat)))
        .collect()
}

fn seat_id(row: usize, column: usize) -> usize {
    row * 8 + column
}

fn row(seat: &str) -> usize {
    let row_binary_string = &seat[0..7].replace('F', "0").replace('B', "1");
    usize::from_str_radix(row_binary_string, 2).unwrap()
}

fn column(seat: &str) -> usize {
    let column_binary_string = &seat[7..10].replace('L', "0").replace('R', "1");
    usize::from_str_radix(column_binary_string, 2).unwrap()
}

fn all_seat_ids(seats: &[usize]) -> Vec<usize> {
    let min = *seats.iter().min().unwrap();
    let max = *seats.iter().max().unwrap() + 1;
    (min..max).collect()
}

fn missing_seat(seats: &[usize], all_seat_ids: &[usize]) -> usize {
    *all_seat_ids
        .iter()
        .find(|seat| !seats.contains(seat))
        .unwrap()
}
