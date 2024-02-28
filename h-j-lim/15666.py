def n_and_m(n, m, possible_answers, length):
    if length == m:
        return possible_answers
    else:
        next_level = []
        for x in possible_answers:
            for num in range(x[-1], n):
                next_level.append(x + [num])
        return n_and_m(n, m, next_level, length + 1)


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()
N_refined = len(nums)
start = [[i] for i in range(N_refined)]
ans = n_and_m(N_refined, M, start, 1)
for p in ans:
    print(*list(map(lambda x: nums[x], p)))
