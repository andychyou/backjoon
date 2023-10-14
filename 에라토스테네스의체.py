import sys
from collections import deque

input = sys.stdin.readline


def main():
    N,K = map(int,input().split())
    li = [x for x in range(2,N+1)]
    a = 0
    cnt = 0
    found = False
    while not found:
        i = 0
        a = li[0]
        while i < len(li):
            if li[i] % a == 0:
                answer = li.pop(i)
                cnt += 1
                if cnt == K:
                    found = True
                    break
            else:
                i += 1
        


        
    print(answer)



if __name__ == '__main__':
    main()