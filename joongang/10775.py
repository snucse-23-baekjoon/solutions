from sys import stdin
g = int(stdin.readline())
p = int(stdin.readline())
gates = [0]*(g+1)
record = [i+1 for i in range(g+1)]
cnt = 0
for i in range(p):
    gate = int(stdin.readline())
    tmp = record[gate] - 1
    while tmp > 0 and gates[tmp]:
        tmp -= 1
    if tmp:
        gates[tmp] = 1
        record[gate] = tmp
        cnt += 1
    else:
        break
print(cnt)