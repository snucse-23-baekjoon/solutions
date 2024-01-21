def pals(letters, pin):
    if pin == 26:
        return ""
    container = chr(pin + ord('A')) * (letters[pin] // 2)
    return container + pals(letters, pin + 1) + container

name = input()
letters = [0] * 26

for letter in name:
    letters[ord(letter) - ord('A')] += 1

count = -2
for i in letters:
    if i % 2:
        if count == -2:
            count = letters.index(i)
        else:
            print("I'm Sorry Hansoo")
            count = -1
            break

if not count == -1:
    if count != -2:
        pal = pals(letters, 0)
        print(pal[:len(pal)//2] + chr(count + ord('A')) + pal[len(pal)//2:])
    else:
        print(pals(letters, 0))