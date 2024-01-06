n = int(input())
five = n // 5
three = 0
chk = 0
while five >= 0:
    while 1:
        s = five*5 + three*3
        if s == n:
            chk = 1
            break
        elif s > n:
            break
        else:
            three += 1
    if chk:
        break
    five -= 1
if five == -1:
    three = 0
print(five + three)