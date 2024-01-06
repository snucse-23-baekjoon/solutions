num = input()

while num != "0":
    length = 0
    for letter in num:
        length += 1
        if letter == "1":
            length += 2
        elif letter == "0":
            length += 4
        else:
            length += 3
    print(length + 1)
    num = input()