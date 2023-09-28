import sys

sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline


answer = 0

def Backtrack(matrix, N, k, r_start):
    global answer
    if k == N:
        answer += 1
        return

    for i in range(r_start, N):
        for j in range(N):
            if matrix[i][j] == 0:

                temp_matrix = [row[:] for row in matrix]
                Queen(temp_matrix, N, i,j)
                Backtrack(temp_matrix, N, k+1, r_start+1)

def Queen(matrix, N, i, j):
    matrix[i] = [1]*N
    for r in range(N):
        matrix[r][j] = 1
    #y = x - i + j
    for x in range(N):
        for y in range(N):
            if y == x - i + j: 
                matrix[x][y] = 1
            if y == -(x - i) + j: 
                matrix[x][y] = 1

    #y = -(x - i) + j






def main():
    global answer
    N = int(input())
    matrix = [[0]*N for x in range(N)]
    # k 1 - 8
    Backtrack(matrix,N,0,0)
    print(answer)






if __name__ == '__main__':
    main()