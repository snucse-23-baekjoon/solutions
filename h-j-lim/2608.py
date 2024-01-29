def rom_to_arab(x):
    i = 0
    num = 0
    while i < len(x):
        if x[i: i + 2] in D2.keys():
            num += D2[x[i: i + 2]]
            i += 2
        else:
            num += D1[x[i]]
            i += 1
    return num


def arab_to_rom(num):
    x = ''
    while num:
        tmp = list(filter(lambda y: num >= D3[y], D3.keys()))
        to_add = max(tmp, key=(lambda y: D3[y]))
        x += to_add
        num -= D3[to_add]
    return x


rom1 = input()
rom2 = input()
D1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
D2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
D3 = D1 | D2
num1 = rom_to_arab(rom1)
num2 = rom_to_arab(rom2)
print(num1 + num2)
print(arab_to_rom(num1 + num2))
