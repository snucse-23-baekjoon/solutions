import sys

dict_len, question_num = map(int, sys.stdin.readline().split())
my_dict = dict()
dict_inverse = dict()
for i in range(1, 1 + dict_len):
    name = sys.stdin.readline().rstrip()
    my_dict[i] = name;
    dict_inverse[name] = i

for _ in range(question_num):
    query = sys.stdin.readline().rstrip()
    if ord('0') <= ord(query[0]) <= ord('9'):
        print(my_dict[int(query)])
    else:
        print(dict_inverse[query])