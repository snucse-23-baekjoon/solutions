def reverse_str(word):
    if not word:
        return ""
    return word[-1] + reverse_str(word[:-1])

word = input()
length = len(word)
out = str()
for i in range(1, length):
    for j in range(i + 1, length):
        if not out:
            out = reverse_str(word[:i]) + reverse_str(word[i:j]) + reverse_str(word[j:])
        elif reverse_str(word[:i]) + reverse_str(word[i:j]) + reverse_str(word[j:]) < out:
            out = reverse_str(word[:i]) + reverse_str(word[i:j]) + reverse_str(word[j:])
print(out)