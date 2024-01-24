t1 = input()
t2 = input()
l1, l2 = len(t1), len(t2)
lst = [[0]*(l2+1) for i in range(l1+1)]
for i in range(1, l1+1):
    for j in range(1, l2+1):
        if t1[i-1] == t2[j-1]:
            lst[i][j] = lst[i-1][j-1] + 1
        else:
            lst[i][j] = max(lst[i-1][j], lst[i][j-1])
    
print(lst[-1][-1])