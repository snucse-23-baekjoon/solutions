num = (int(input())//100)*100
div = int(input())

for i in range(100):
    if (num + i) % div == 0:
        if i < 10:
            print("0" + str(i))
        else:
            print(i)
        break