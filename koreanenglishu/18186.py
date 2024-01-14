from sys import stdin
stdin = open("../input.txt", 'r')

n, b, c = map(int, stdin.readline().split())
arr = map(int, stdin.readline().split())
ans = 0

if b > c:
    a1, a2 = next(arr), next(arr)
    if a1 > a2:
        ans += (a1 - a2) * b
        a1 = a2

    for a3 in arr:
        if a2 > a3:
            if a1 >= a2 - a3:
                ans += b * a1 + c * (2 * a1 - a2 + a3)
                a1, a2 = a2 - a1, a2 - a1
            else:
                ans += b * (a2 - a3) + c * a1
                a1, a2 = a3, a3
        else:
            ans += (b + 2 * c) * a1
            a1, a2 = a2 - a1, a3 - a1

    ans += b * a2 + c * a1

else:
    ans += sum(arr) * b

print(ans)
