def f(i, j, n):
    if n == 3:
        stars[i][j] = '*'
        stars[i+1][j-1] = '*'
        stars[i+1][j+1] = '*'
        for k in range(-2, 3):
            stars[i+2][j+k] = '*'
    else:
        m = n//2
        f(i, j, m)
        f(i+m, j-m, m)
        f(i+m, j+m, m)
    
n = int(input())
stars = [[' ']*n*2 for i in range(n)]
f(0, n-1, n)
for i in stars:
    print(''.join(i))