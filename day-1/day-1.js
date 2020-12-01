const fs = require('fs')

const solve_part_1 = (numbers) => {
  for (let a = 0; a < numbers.length; a++) {
    for (let b = 0; b < numbers.length; b++) {
      if (numbers[a] + numbers[b] === 2020)
        return numbers[a] * numbers[b]
    }
  }
}

const solve_part_2 = (numbers) => {
  for (let a = 0; a < numbers.length; a++) {
    for (let b = 0; b < numbers.length; b++) {
      for (let c = 0; c < numbers.length; c++) {
        if (numbers[a] + numbers[b] + numbers[c] === 2020)
          return numbers[a] * numbers[b] * numbers[c]
      }
    }
  }
}

const numbers = fs
  .readFileSync('input.txt', 'utf8')
  .split('\n')
  .filter(n => Number.isInteger(parseInt(n, 10)))
  .map(n => parseInt(n, 10))

console.log(solve_part_1(numbers))
console.log(solve_part_2(numbers))
