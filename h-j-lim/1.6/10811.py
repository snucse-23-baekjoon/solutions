N = int(input())
l = list(map(int, input().split()))
print((sum(l) / len(l)) * (100 / max(l)))