target, word = input().split()

least = len(target)
for i in range(len(word) - len(target) + 1):
    count = 0
    for j in range(len(target)):
        if target[j] != word[i + j]:
            count += 1
    if count < least:
        least = count

print(least)