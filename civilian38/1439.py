bits = input()
arr = [bits[i] for i in range(len(bits))]
for i in range(len(bits) - 1, 0, -1):
    if arr[i] == arr[i - 1]:
        arr.pop(i)

print(min((arr.count('0'), arr.count('1'))))