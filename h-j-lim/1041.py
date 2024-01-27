N = int(input())
A, B, C, D, E, F = map(int, input().split())
L_1 = [A, B, C, D, E, F]
L_2 = []
for i in range(6):
    for j in range(i + 1, 6):
        if (i != 0 or j != 5) and (i != 1 or j != 4) and (i != 2 or j != 3):
            L_2.append(L_1[i] + L_1[j])
L_3 = [A + B + C, A + B + D, A + C + E, A + D + E, F + B + C, F + B + D, F + C + E, F + D + E]
if N == 1:
    print(sum(L_1) - max(L_1))
else:
    ans = 4 * min(L_3) + (8 * N - 12) * min(L_2) + (5 * N ** 2 - 16 * N + 12) * min(L_1)
    print(ans)
