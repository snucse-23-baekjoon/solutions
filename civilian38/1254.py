def is_palindrome(string):
    if len(string) % 2:
        if string[:len(string)//2] == string[len(string)//2 + 1:][::-1]:
            return True
        return False
    else:
        if string[:len(string)//2] == string[len(string)//2:][::-1]:
            return True
        return False


string = input()
for i in range(len(string)):
    if is_palindrome(string[i:]):
        print(i + len(string))
        break