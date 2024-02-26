x, y, z = map(int, input().split())
if x==y and y==z:
    print(10000+(x*1000))
elif x==y:
    print(1000+(x*100))
elif y==z:
    print(1000+(y*100))
elif z==x:
    print(1000+(z*100))
else:
    print(100*max([x, y, z]))