from collections import deque
import sys
# sys.stdin = open('test.txt', "r")
input = sys.stdin.readline


def bfs(adj_list, queue, visited,s):
    global rank, rank_dict
    queue.append(s)
    visited[s] = True
    rank += 1
    rank_dict[s] = rank
    while queue:
        curr = queue.popleft()
        for neighbor in (adj_list[curr]):
            if visited[neighbor] != True:  
                visited[neighbor] = True
                rank += 1
                rank_dict[neighbor] = rank
                queue.append(neighbor)



vertice , num , s = map(int, input().split())

adj_list = dict()
for i in range(1, vertice+1):
    adj_list[i] = []

for i in range(num):
    line = list(map(int, input().split()))
    adj_list[line[0]].append(line[1])
    adj_list[line[1]].append(line[0])

for i in range(1, vertice+1):
    adj_list[i].sort()



visited = dict()
rank_dict = dict()
for i in range(1, vertice+1):
    visited[i] = False
    rank_dict[i] = 0
rank = 0
queue = deque()
bfs(adj_list, queue, visited, s)

for value in rank_dict.values():
    print(value)


