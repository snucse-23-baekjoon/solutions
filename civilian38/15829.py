import sys

length = int(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()
hashnum = 0

for i in range(length):
    hashnum += ((31 ** i) * (ord(word[i]) - ord('a') + 1)) % 1234567891

print(hashnum % 1234567891)