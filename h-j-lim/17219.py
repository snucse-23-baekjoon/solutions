import sys

N, M = map(int, sys.stdin.readline().split())
sites_passwords = {}
for _ in range(N):
    site, password = sys.stdin.readline().split()
    sites_passwords[site] = password
for _ in range(M):
    print(sites_passwords[sys.stdin.readline().rstrip()])
