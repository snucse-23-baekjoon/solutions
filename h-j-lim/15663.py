def n_and_m(n, m, permutation, avail, length):
    if length == m:
        ans.append(permutation)
    else:
        for j in range(n):
            tmp = avail[:]
            if tmp[j]:
                tmp[j] -= 1
                n_and_m(n, m, permutation + [j], tmp, length + 1)


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
nums_refined = [1]
nums_set = [nums[0]]
for i in range(1, N):
    if nums[i - 1] == nums[i]:
        nums_refined[-1] += 1
    else:
        nums_refined.append(1)
        nums_set.append(nums[i])
N_refined = len(nums_refined)
ans = []
n_and_m(N_refined, M, [], nums_refined, 0)
for p in ans:
    print(*list(map(lambda x: nums_set[x], p)))
