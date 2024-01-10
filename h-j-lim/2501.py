n = int(input())
lst_of_factors = []
while n != -1:
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            lst_of_factors.append(i)
    if sum(lst_of_factors) == n:
        lst_of_factors = list(map(str, lst_of_factors))
        print(str(n) + ' = ' + ' + '.join(lst_of_factors))
    else:
        print(str(n) + ' is NOT perfect.')
    n = int(input())
    lst_of_factors = []
