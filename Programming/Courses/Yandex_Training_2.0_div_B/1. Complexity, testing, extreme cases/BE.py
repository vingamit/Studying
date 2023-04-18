n = int(input())
x,y = map(int,input().split())
def dist (x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)
def distTria(cordTria, poi1,poi2):
    x1,y1 = 0,0
    x2,y2 = cordTria, 0
    x3,y3 = 0,cordTria
    x0,y0 = poi1,poi2
    fi = dist(x1,y1,x0,y0)
    se = dist(x2,y2,x0,y0)
    th = dist(x3,y3,x0,y0)
    a = (x1-x0)*(y2-y1) - (x2-x1)*(y1-y0)
    b = ((x2-x0)*(y3-y2) - (x3-x2)*(y2-y0))
    c = ((x3-x0)*(y1-y3) - (x1-x3)*(y3-y0))
    if (a<=0 and b<=0 and c<=0):
        return 0
    elif(a>=0 and b>=0 and c>=0):
        return 0
    elif(a==0 or b==0 or c==0):
        return 0
    elif fi == se and th>se:
        return 1
    elif se == th and fi>se:
        return 2
    elif th == fi and se > fi:
        return 1
    elif fi < se <= th:
        return 1
    elif fi < th <= se:
        return 1
    elif se < fi <= th:
        return 2
    elif se < th <= fi:
        return 2
    elif th < se <=fi:
        return 3
    elif th < fi <=se:
        return 3
print(distTria(n,x,y))