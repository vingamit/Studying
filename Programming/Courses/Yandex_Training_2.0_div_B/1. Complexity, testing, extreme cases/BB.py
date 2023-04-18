x,y,z = map(int, input().split()) 
mod = abs(y-z)
if mod > x/2:
    print(x - mod -1)
else:
    print(mod-1)