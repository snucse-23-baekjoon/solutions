from sys import stdin
stdin = open("../input.txt", 'r')

string = stdin.readline().rstrip()
n = len(string)

# GENERATE SUFFIX ARRAY
suffix_array = [i for i in range(n)]
group = [ord(c) for c in string]
next_group = [0] * (n + 1)

t = 1
while t < n:
    suffix_array.sort(key=lambda x: (
        group[x], group[x + t] if x + t < n else -1
    ))

    for i in range(n - 1):
        j, k = suffix_array[i:i + 2]
        next_group[k] = next_group[j]
        if (group[j], group[j + t] if j + t < n else -1) < \
                (group[k], group[k + t] if k + t < n else -1):
            next_group[k] += 1

    if next_group[n - 1] == n - 1: break
    group = next_group[:]; t *= 2

# GENERATE LCP ARRAY
lcp_array = [0] * n
inv_suffix_array = [0] * n
for i in range(n):
    inv_suffix_array[suffix_array[i]] = i

i = 0
for j in range(n):
    if inv_suffix_array[j] == 0:
        i = 0; continue
    k = suffix_array[inv_suffix_array[j] - 1]; m = max(j, k)
    while i + m < n and string[i + j] == string[i + k]: i += 1
    lcp_array[inv_suffix_array[j]] = i
    if i > 0: i -= 1

stack = []
max_cost = n
lcp_array.append(0)
for i in range(n + 1):
    while len(stack) > 1 and lcp_array[i] < stack[-1][1]:
        max_cost = max(max_cost, (i - stack[-1][0]) * stack[-1][1])
        if stack[-2][1] >= lcp_array[i]: stack.pop()
        else: stack[-1][1] = lcp_array[i]
    stack.append([i - 1, lcp_array[i]])

print(max_cost)
