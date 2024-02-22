def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
    if tmp>0:
        return 1
    elif tmp<0:
        return -1
    else:
        return 0
    
def cross(x1, y1, x2, y2, x3, y3, x4, y4):
    if ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4)==0 and ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x1, y1)==0:
        if min(x1, x2)<=max(x3, x4) and max(x1, x2)>=min(x3, x4) and min(y1, y2)<=max(y3, y4) and max(y1, y2)>=min(y3, y4):
            return 1
    elif ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4)<=0 and ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2)<=0:
        return 1
    return 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
print(cross(x1, y1, x2, y2, x3, y3, x4, y4))