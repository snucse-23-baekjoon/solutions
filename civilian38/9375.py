import sys

repeat = int(sys.stdin.readline().rstrip())
for _ in range(repeat):
    number = int(sys.stdin.readline().rstrip())
    wears = dict()
    if number:
        for __ in range(number):
            name, types = sys.stdin.readline().split()
            if wears.get(types):
                wears[types] += 1
            else:
                wears[types] = 1
        numbers = list(zip(*wears.items()))[1]

        m = 1
        for i in numbers:
            m *= i + 1
        m -= 1
        print(m)
    else:
        print(0)