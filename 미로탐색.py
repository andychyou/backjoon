import sys
from collections import deque

#bfs는 해당 노드를 처음 방문했을 때 최소 거리를 보장한다 
#최소 거리 문제 == bfs

sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

N = None
M = None
cnt = 0

def bfs(matrix, visited, queue):
    global cnt

    while queue:
        node = queue.popleft()
        if node[0] == N-1 and node[1] == M-1:
            cnt = node[2]+1
            break

        if(node[0]+1 < N and node[0]+1 >= 0):
            if matrix[node[0]+1][node[1]] == 1  and visited[node[0]+1][node[1]] == False:
                visited[node[0]+1][node[1]] = True
                queue.append([node[0]+1,node[1],node[2]+1])
        if(node[0]-1 < N and node[0]-1 >= 0):
            if matrix[node[0]-1][node[1]] == 1  and visited[node[0]-1][node[1]] == False:
                visited[node[0]-1][node[1]] = True
                queue.append([node[0]-1,node[1],node[2]+1])
        if(node[1]+1 < M and node[1]+1 >= 0):
            if matrix[node[0]][node[1]+1] == 1  and visited[node[0]][node[1]+1] == False:
                visited[node[0]][node[1]+1] = True
                queue.append([node[0],node[1]+1,node[2]+1])
        if(node[1]-1 < M and node[1]-1 >= 0):
            if matrix[node[0]][node[1]-1] == 1  and visited[node[0]][node[1]-1] == False:
                visited[node[0]][node[1]-1] = True
                queue.append([node[0],node[1]-1,node[2]+1])


    
    


def main():
    global N,M,cnt
    N,M = list(map(int, input().split()))
    matrix = [[0]*M for x in range(N)]
    visited = [[False]*M for x in range(N)]
    visited[0][0] = True
    queue = deque([[0,0,0]])
    for row in range(N):
        matrix[row] = list(map(int,list(input().strip())))

    bfs(matrix, visited,queue)
    print(cnt)

if __name__ == '__main__':
    main()