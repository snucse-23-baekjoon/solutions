D = {0: 1, 1: 1}


def fact(n):
    if n in D.keys():
        return D[n]
    else:
        return fact(n - 1) * n


N = int(input())
L = list(map(int, input().split()))
num_list = list(range(1, N + 1))
if L[0] == 1:
    ans_list = []
    target = L[1] - 1
    i = N - 1
    while target:
        ans_list.append(num_list.pop(target // fact(i)))
        target %= fact(i)
        i -= 1
    ans_list.extend(num_list)
    print(*ans_list)
else:
    ans = 1
    target = L[1:]
    i = 0
    while num_list:
        ans += num_list.index(target[i]) * fact(N - 1 - i)
        num_list.pop(num_list.index(target[i]))
        i += 1
    print(ans)
