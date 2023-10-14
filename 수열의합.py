import sys
from collections import deque
input = sys.stdin.readline

def main():
    N, L = map(int,input().split())
    answer = -1
    
    while True:
        rest  = (N - (L-1)*L // 2) % L
        a  = (N - (L-1)*L // 2) // L
        if (rest != 0 or a < 0) and L <= 100:
            L += 1
            continue
        
        if L <= 100:
            for x in range(L):
                print(a, end=' ')
                a += 1
            break
        else:
            print(-1)
            break
            
    




        

        


    

if __name__ == '__main__':
    main()