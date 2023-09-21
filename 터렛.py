import sys
import math

# sys.stdin = open("test.txt", "r")


test_case = int(input())


def CalcDist(x1,y1,x2,y2):
    x = abs(x1-x2)
    y = abs(y1-y2)
    return math.sqrt(x**2 + y**2)


for x in range(test_case):
    line = input()
    x1,y1,r1,x2,y2,r2 = map(int, line.split())

    longer_r = r1 if r1 > r2 else r2
    shorter_r = r1 if r1 < r2 else r2

    dist = CalcDist(x1,y1,x2,y2)
    answer = 0
    if(x1 == x2 and y1 == y2 and r1 == r2): answer = -1
    elif(dist > r1 + r2):
        answer = 0
    elif(dist == r1 + r2):
        answer = 1
    elif(dist < r1 + r2 and dist > longer_r - shorter_r):
        answer = 2
    elif(dist == longer_r - shorter_r):
        answer = 1
    else:
        answer = 0
    

    print(answer)

    
