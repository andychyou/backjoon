import sys
from collections import deque
from itertools import combinations, permutations
import heapq
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def main():
    N = int(input())
    time = list(map(int,input().split()))
    time.sort(key = lambda x : x)
    
    total = 0
    before = 0
    for x in time:
        before += x
        total += before
    print(total)

    




if __name__ == '__main__':
    main()