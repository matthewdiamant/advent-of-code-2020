def sorted_adapters(adapters):
    sorted_adapters = sorted(adapters)
    return [0] + sorted_adapters + [sorted_adapters[-1] + 3]

def solve_day_2(adapters):
    sorted_adapters = sorted_adapters(adapters)

    DP = {}

    def dp(i):
        if i == len(sorted_adapters) - 1:
            return 1
        if i in DP:
            return DP[i]
        answer = 0
        for j in range(i + 1, len(sorted_adapters)):
            if sorted_adapters[j] - sorted_adapters[i] <= 3:
                answer += dp(j)
        DP[i] = answer
        return answer

    return dp(0)

def solve_day_1(adapters):
    sorted_adapters = sorted_adapters(adapters)
    count = [0, 0, 0]
    for i in range(1, len(sorted_adapters)):
        difference = sorted_adapters[i] - sorted_adapters[i - 1] - 1
        count[difference] += 1
    return count[0] * (count[2])

with open("input.txt") as f:
    input = [int(i) for i in f.read().splitlines()]
    print(solve_day_1(input))
    print(solve_day_2(input))
