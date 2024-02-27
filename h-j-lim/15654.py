def n_and_m(n, m, permutation, avail, length):
    if length == m:
        ans.append(permutation)
    else:
        for num in avail:
            tmp = avail[:]
            tmp.remove(num)
            n_and_m(n, m, permutation + [num], tmp, length + 1)


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []
n_and_m(N, M, [], nums, 0)
for p in ans:
    print(*p)
