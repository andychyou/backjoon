from collections import deque
import sys
# sys.stdin = open('test.txt', "r")
input = sys.stdin.readline


def bfs(adj_matrix, queue, visited):
    global rank, rank_dict

    if not queue:
        return

    while queue:
        curr = queue.popleft()
        visited[curr] = True
        rank += 1
        rank_dict[curr] = rank
        li = []
        for i in range(1, len(adj_matrix[curr])):
            if visited[i] != True and adj_matrix[curr][i] == 1:  
                visited[i] = True
                li.append(i)
        for x in sorted(li):
            queue.append(x)



vertice , num , s = map(int, input().split())

adj_matrix = [[0] * (num+1) for _ in range(num+1)]

for i in range(num):
    line = list(map(int, input().split()))
    adj_matrix[line[0]][line[1]] = 1
    adj_matrix[line[1]][line[0]] = 1



print(adj_matrix)


visited = dict()
rank_dict = dict()
for i in range(1, num+1):
    visited[i] = False
    rank_dict[i] = 0
rank = 0
queue = deque()
queue.append(s)
bfs(adj_matrix, queue, visited)

for value in rank_dict.values():
    print(value)


