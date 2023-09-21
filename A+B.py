import sys

a,b,c,d,e,f = map(int, sys.stdin.readline().strip().split())

x = 1000
y = 1000

if((a*e - b*d) != 0):
    x = int(round((c*e - b*f) / (a*e - b*d),0))
if((b*d - a*e) != 0):
    y = int(round((c*d - a*f) / (b*d - a*e), 0))

if(x == 1000):
    if(a != 0):
        x = int(round((c - b*y) / a, 0))
    else:
        x = int(round((f - e*y) / d, 0))

if(y == 1000):
    if(b != 0):
        y = int(round((c-a*x)/b,0))
        y = int(round((f-d*x)/b,0))


print(x, y)
