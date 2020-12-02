import System.IO

main = do
    contents <- readFile "input.txt"
    let input = map read (lines contents)
    putStrLn (show (solve_part_1(input)))
    putStrLn (show (solve_part_2(input)))

solve_part_1 :: [Int] -> Int
solve_part_1 numbers = head (filter (/=0) (find_two_answers numbers))

find_two_answers numbers = map (\candidate -> twoCompare2020 candidate (tail numbers)) numbers

twoCompare2020 :: Int -> [Int] -> Int
twoCompare2020 number [] = 0
twoCompare2020 number (x:xs) =
  if number + x == 2020
    then number * x
    else twoCompare2020 number xs

solve_part_2 :: [Int] -> Int
solve_part_2 numbers = head (filter (>0) (find_three_answers numbers))

find_three_answers numbers = map (\candidate -> threeCompare2020 candidate (tail numbers)) numbers

threeCompare2020 :: Int -> [Int] -> Int
threeCompare2020 _ [] = 0
threeCompare2020 number candidates =
  if number + (head candidates) == 2020
    then number * (head candidates)
    else threeCompare2020 number (tail candidates)
