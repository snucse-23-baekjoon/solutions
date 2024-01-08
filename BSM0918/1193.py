n = int(input())

i = 1
j = 1

while n > j:
    i += 1
    j += i
i += 1
gap = j - n

if i%2 == 0:
    numerator = 1 + gap
    denominator = i - (gap + 1)
else:
    numerator = i - (gap + 1)
    denominator = 1 + gap

print(str(numerator) + "/" + str(denominator))