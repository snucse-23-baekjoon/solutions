import sys


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cloth_type_list = []
    cloth_num_list = []
    for _ in range(N):
        cloth, cloth_type = sys.stdin.readline().rstrip().split()
        if cloth_type not in cloth_type_list:
            cloth_type_list.append(cloth_type)
            cloth_num_list.append(1)
        else:
            cloth_num_list[cloth_type_list.index(cloth_type)] += 1
    ans = 1
    for i in range(len(cloth_num_list)):
        ans *= cloth_num_list[i] + 1
    print(ans - 1)

