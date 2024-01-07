num = "0" + input()
cycle = 0
temp = str(num)
while temp.lstrip("0") != num.lstrip("0") or cycle == 0:
    bypass = "0" + str(int(temp[-2]) + int(temp[-1]))
    temp = "0" + temp[-1] + bypass[-1]
    cycle += 1
print(cycle)