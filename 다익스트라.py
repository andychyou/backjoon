import sys
sys.setrecursionlimit(10**6)
from collections import deque
from itertools import combination, permutation
import heapq

sys.stdin = open('test.txt','r')
input = sys.stdin.readline

def main():
    N = int(input())
    matrix = [[0]*N for x in range(N)]
    for line in range(N):
        matrix[line] = list(map(int, input().split()))
    dist = matrix[0]


    pq = []
    heapq.heappush(pq, (0,0))

    while pq:
        curr,d = heapq.heappop(pq)
        if dist[curr] < d:
            continue
        for i in range(N):
            next = matrix[curr][i][0]
            next_d = d + matrix[curr][i][1]
            if next_d < dist[next]:
                dist[next] = next_d
                pq.heappush((next,next_d))

    
    
if __name__ == '__main__':
    main()
