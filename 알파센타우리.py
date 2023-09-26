import sys
sys.stdin = open("test.txt","r")

import math







def main():
    T = int(input())
    for testcase in range(T):
        x,y = map(int,input().split())
        dist = abs(x-y)
        n = math.sqrt(dist)
        n_ = int(math.trunc(n))
        if n.is_integer():
            n = int(n)
            answer=3+2*(n-2)
        else:
            if dist < int((n_**2+1+(n_+1)**2)/2):
                answer=3+2*(n_-2)+1
            else:
                answer=3+2*(n_-2)+2
            
        print(answer)


if __name__ == "__main__":
    main()