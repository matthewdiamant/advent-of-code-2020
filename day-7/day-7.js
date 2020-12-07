c = txt => console.log(txt)
let fs = require("fs");

let f = fs.readFileSync("./input.txt", "utf-8");
let input = f.split("\n").filter(Boolean)

const bag_rules = text =>
  text.split(" ").splice(0, 2).join(" ")

const subbag_rules = text =>
  text.split(",").map(sub => sub.trim().split(' ').splice(1, 2).join(" "))

const rules = input => input.map(rule => {
  let [bag, subbags] = rule.split('contain')
  return {
    bag: bag_rules(bag),
    subbags: subbag_rules(subbags)
  }
})

const solve_part_1 = input => {
  c(rules(input))
}

console.log(solve_part_1(input))
