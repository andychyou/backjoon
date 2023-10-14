import sys

sys.setrecursionlimit(10**6)
sys.stdin = open('test.txt','r')
input = sys.stdin.readline

N = M = 0
matrix = []
check = []

def dfs(curr):
    global matrix,check,M
    for next in range(1,N+1):
        if matrix[curr][next] == 1 and check[next] == 0:
            check[next] = 1
            dfs(next)



def main():
    global N,M,matrix,check
    N, M = map(int, input().split())
    matrix = [[0]*(N+1) for _ in range(N+1)]
    check = [0] * (N+1)

    for x in range(M):
        u,v = map(int,input().split())
        matrix[u][v] = 1
        matrix[v][u] = 1
    
    cnt = 0
    for x in range(1,N+1):
        if check[x] == 0:
            check[x] = 1
            dfs(x)
            cnt += 1

    print(cnt)
        



if __name__ == '__main__':
    main()