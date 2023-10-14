import sys
from collections import deque

sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline



def bfs(bachoo, matrix, visited,N,M):
    i,j = bachoo
    if visited[i][j] == True:
        return 
    
    visited[i][j] = True
    queue = deque([bachoo])
    
    while queue:
        curr = queue.popleft()
        c_i,c_j = curr
        if 0 <= c_i - 1 and matrix[c_i-1][c_j] == 1 and not visited[c_i-1][c_j]:
            visited[c_i-1][j] = True
            queue.append([c_i-1,c_j])
        if N > c_i + 1 and matrix[c_i+1][c_j] == 1 and not visited[c_i+1][c_j]:
            visited[c_i+1][j] = True
            queue.append([c_i+1,c_j])
        if 0 <= c_j - 1 and matrix[c_i][c_j-1] == 1 and not visited[c_i][c_j-1]:
            visited[c_i][c_j-1] = True
            queue.append([c_i,c_j-1])
        if M > c_j + 1 and matrix[c_i][c_j+1] == 1 and not visited[c_i][c_j+1]:
            visited[c_i][c_j+1] = True
            queue.append([c_i,c_j+1])

        


def main():
    T = int(input())
    for test in range(T):
        M,N,K = list(map(int,input().split()))
        matrix = [[0]*M for x in range(N)]
        visited = [[False]*M for x in range(N)]
        bachoo_list = deque([])
        for b in range(K):
            j,i = list(map(int,input().split()))
            matrix[i][j] = 1
            bachoo_list.append([i,j])
        
        cnt = 0
        for bachoo in bachoo_list:
            i,j = bachoo
            if not visited[i][j]:
                bfs(bachoo, matrix, visited, N,M)
                cnt += 1

        print(cnt)
if __name__ == "__main__":
    main()