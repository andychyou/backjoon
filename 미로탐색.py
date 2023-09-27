import sys
sys.stdin = open("test.txt",'r')
from collections import deque

#queue에 여기까지 오는 cnt를 저장해야 한다
#bfs로 최소 거리 구할 수 있음


N = None
M = None

def bfs(matrix, visited, queue):
    cnt = 0

    while queue:
        node = queue.popleft()
        visited[node[0]][node[1]] = True
        cnt += 1

        if node[0] == N-1 and node[1] == M-1:
            return node[2]


        if(node[0]+1 < N and node[0]+1 >= 0):
            if matrix[node[0]+1][node[1]] == 1  and visited[node[0]+1][node[1]] == False:
                queue.append([node[0]+1,node[1],node[2]+1])
                visited[node[0]+1][node[1]] = True
        if(node[0]-1 < N and node[0]-1 >= 0):
            if matrix[node[0]-1][node[1]] == 1  and visited[node[0]-1][node[1]] == False:
                queue.append([node[0]-1,node[1],node[2]+1])
                visited[node[0]-1][node[1]] = True
        if(node[1]+1 < M and node[1]+1 >= 0):
            if matrix[node[0]][node[1]+1] == 1  and visited[node[0]][node[1]+1] == False:
                queue.append([node[0],node[1]+1,node[2]+1])
                visited[node[0]][node[1]+1] = True
        if(node[1]-1 < M and node[1]-1 >= 0):
            if matrix[node[0]][node[1]-1] == 1  and visited[node[0]][node[1]-1] == False:
                queue.append([node[0],node[1]-1,node[2]+1])
                visited[node[0]][node[1]-1] = True


    
    


def main():
    global N,M
    N,M = list(map(int, input().split()))
    matrix = [[0]*M for x in range(N)]
    visited = [[False]*M for x in range(N)]
    queue = deque([[0,0, 1]])
    for row in range(N):
        matrix[row] = list(map(int,list(input())))
    cnt = bfs(matrix, visited,queue)
    print(cnt)

if __name__ == '__main__':
    main()