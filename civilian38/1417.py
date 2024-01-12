import sys

number = int(sys.stdin.readline().rstrip())
myvote = int(sys.stdin.readline().rstrip())
votes = []
for _ in range(number - 1):
    votes.append(int(sys.stdin.readline().rstrip()))

if not votes:
    print(0)

else:
    count = 0
    while(max(votes) >= myvote):
        votes[votes.index(max(votes))] -= 1
        myvote += 1
        count += 1
    print(count)