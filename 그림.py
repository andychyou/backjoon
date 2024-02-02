import sys
from collections import deque
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)


row,col = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]
# matrix = []
# for r in range(row):
#     matrix.append(list(map(int, input().split())))
visited = [[False] * col for n in range(row)]

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def bfs(r,c):
    size=1
    queue = deque()
    queue.append((r,c))
    while queue:
        r,c = queue.popleft()
        
        for i in range(4):
            mr = r+dr[i]
            mc = c+dc[i]
            if 0 <= mr < row and 0 <= mc < col:
                if matrix[mr][mc] == 1 and not visited[mr][mc]:
                    size += 1
                    visited[mr][mc] = True
                    queue.append((mr,mc))
    return size


cnt = 0
size = 0
for r in range(row):
    for c in range(col):
        if matrix[r][c] == 1 and not visited[r][c]:
            visited[r][c] = True
            cnt +=1
            size = max(size, bfs(r,c))
print(cnt)
print(size)

