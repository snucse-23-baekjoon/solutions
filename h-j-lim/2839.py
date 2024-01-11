N = int(input())
ans = 0
if N == 4 or N == 7:
    print(-1)
else:
    for i in range(N // 5, -1, -1):
        if (N - 5 * i) % 3 == 0:
            ans = i
            break
    ans += (N - 5 * ans) // 3
    print(ans)
