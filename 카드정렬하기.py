import sys
from collections import deque
from heapq import *

sys.stdin = open('test.txt','r')
input = sys.stdin.readline

N = 0



def main():
    global N
    N = int(input())
    cards = []
    for x in range(N):
        heappush(cards, int(input()))
    answer = 0
    while 1 < len(cards):
        a = heappop(cards)
        b = heappop(cards)
        new = a + b
        answer += new
        heappush(cards, new)
    print(answer)

    
    
    

if __name__ == '__main__':
    main()