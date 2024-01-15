L = list(map(int, input().split()))


# chance of p_i winning p_j
def i_against_j(i, j):
    if i < j:
        return L[sum(range(7, 7 - i, -1)) + j - i - 1] / 100
    else:
        return 1 - i_against_j(j, i)


# list of entering second round
L_2 = []
for x in range(8):
    if x % 2 == 0:
        L_2.append(i_against_j(x, x + 1))
    else:
        L_2.append(i_against_j(x, x - 1))
# list of entering third round
L_3 = []
for x in range(8):
    if x // 4 == 0:
        opp = 2 - 2 * (x // 2)
    else:
        opp = 6 - 2 * ((x - 4) // 2)
    L_3.append(sum(list(map(lambda y: L_2[x] * L_2[y] * i_against_j(x, y), range(opp, opp + 2)))))
# list of winning
L_W = []
for x in range(8):
    if x // 4 == 0:
        opp = 4
    else:
        opp = 0
    L_W.append(sum(list(map(lambda y: L_3[x] * L_3[y] * i_against_j(x, y), range(opp, opp + 4)))))
print(*L_W)
