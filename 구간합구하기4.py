import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque
from itertools import combinations, permutations
import heapq
import functools


def main():
    N,M = map(int, input().split())
    n_list = list(map(int, input().split()))
    # n_acc = [0] + [functools.reduce(lambda x,y: x+y, n_list[:i+1] ) for i in range(len(n_list))]
    n_acc = [0] * (N+1)
    for i in range(1,N+1):
        n_acc[i] = n_list[i-1] + n_acc[i-1]
    for x in range(M):
        i, j = map(int, input().split())
        print(n_acc[j] - n_acc[i-1])



if __name__ == '__main__':
    main()