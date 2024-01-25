N = int(input())
l = [[0] * 3 for _ in range(1516)]  # mod 5, 10, 15
l[1] = [1, 0, 0]
i = 2
while i < N + 1:
    l[i][0] = l[i - 1][1] + l[i - 1][2]
    l[i][1] = l[i - 1][0] + l[i - 1][2]
    l[i][2] = l[i - 1][0] + l[i - 1][1]
    i += 1
print(l[N][2] % 1000000007)
