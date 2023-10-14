import sys
from collections import deque
import math

input = sys.stdin.readline


def main():
    MIN, MAX = map(int,input().split())
    a= math.ceil(math.sqrt(MIN))
    if a == 1:
        a=2
    b= (math.trunc(math.sqrt(MAX)))
    squared = 0
    if (b-a) < 0:
        squared = 0
    else:
        squared = b-a+1
    numbers = MAX-MIN+1
    squares = [x**2 for x in range(a,b+1)]
    for n in range(MIN,MAX+1):
        for s in squares:
            if n % s == 0:
                numbers -= 1
                break
    print(numbers)




if __name__ == '__main__':
    main()