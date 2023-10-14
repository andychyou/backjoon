import sys
from collections import deque
from itertools import combinations, permutations
import heapq

input = sys.stdin.readline

def main():
    cnt = 1
    while True:
        L,P,V = map(int, input().split())
        if L == 0 and P == 0 and V == 0:
            break
        print(f"Case {cnt}: {(V // P) * L + V % P}")
        cnt += 1
    

if __name__ == '__main__':
    main()