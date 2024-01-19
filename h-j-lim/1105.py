L, R = map(int, input().split())
L_list = list(str(L))
R_list = list(str(R))
if L == R:
    print(L_list.count('8'))
else:
    if L_list.count('8') * R_list.count('8') == 0 or len(L_list) != len(R_list):
        print(0)
    else:
        i, count = 0, 0
        while L_list[i] == R_list[i]:
            if L_list[i] == '8':
                count += 1
            i += 1
        print(count)
