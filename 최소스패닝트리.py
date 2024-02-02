import sys
input = sys.stdin.readline
import heapq
from collections import deque

V,E = map(int, input().split())
#adj_matrix를 사용했을 때는 메모리 초과가 났다
adj_list = [[]*(V+1) for x in range(V+1)]
for e in range(E):
    A,B,C = map(int, input().split())
    adj_list[A].append((C,B)) 
    adj_list[B].append((C,A))
# w가 낮은순으로 최소 heap이 만들어짐
# [(w,next_node)]
visited = [False] * (V+1)
ans = 0
heap = [(0,1)]
while heap:
    w, next_node = heapq.heappop(heap)
    if not visited[next_node]:
        visited[next_node] = True
        ans += w
        for v in adj_list[next_node]:
            #v = (w,node)
            if not visited[v[1]]:
                
                heapq.heappush(heap, v)

print(ans)