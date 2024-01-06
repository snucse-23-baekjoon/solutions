from sys import stdin
while 1:
    lst = list(map(int, stdin.readline().split()))
    if lst == [0, 0, 0]:
        break
    lst.sort()
    if lst[2]**2 == lst[0]**2 + lst[1]**2:
        print('right')
    else:
        print('wrong')