with open("./input.txt") as f:
    input = [int(n) for n in f.read().splitlines()]
    n = 0

    solution = True
    while (solution):
        window = input[n:(n + 25)]
        challenger = input[n + 25]
        solve = False
        for i in window:
            for j in window:
                if i != j:
                    if i + j == challenger:
                        solve = True
        if solve == False:
            solution = False
            answer = challenger
        else:
            n += 1

    print(answer)

    solution = False
    for i in range(len(input)):
        if solution:
            break;
        sum = 0
        j = 0
        s = set()
        while sum < answer:
            s.add(input[j + i])
            sum += input[j + i]
            j += 1
        if sum == answer and j > 0:
            answer2 = sum
            answer2_s = s
            solution = True

    print(min(answer2_s) + max(answer2_s))
