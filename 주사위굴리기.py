import sys

sys.stdin = open("test.txt",'r')
input = sys.stdin.readline

N,M = 0,0
matrix = None



def Move(c,i,j):
    global matrix, N,M
    n_i,n_j = i,j
    if c == 1:
        n_j = j + 1
    elif c == 2:
        n_j = j - 1
    elif c == 3:
        n_i = i - 1
    elif c == 4:
        n_i = i + 1
    if n_i >= 0 and n_i < N and n_j >=0 and n_j < M:
        return n_i,n_j
    else:
        return i,j

def main():
    global N,M,matrix
    dice = [0]*6
    top,l,r,f,bot,b = 0,1,2,3,4,5
    N,M,i,j,cnt = list(map(int, input().split()))
    matrix = [[0]*M for x in range(N)]
    for x in range(N):
        line = list(map(int, input().split()))
        for y in range(M):
            matrix[x][y] = line[y]
    command = list(map(int, input().split()))
    for c in command:
        n_i,n_j = Move(c,i,j)
        if [i,j] != [n_i,n_j]:
            i = n_i
            j = n_j
            t_top = dice[top]
            t_bot = dice[bot]
            t_f = dice[f]
            t_b = dice[b]
            t_l = dice[l]
            t_r = dice[r]
            if c == 1:
                dice[top] = t_l
                dice[l] = t_bot
                dice[bot] = t_r
                dice[r] = t_top
            elif c == 2:
                dice[top] = t_r
                dice[r] = t_bot
                dice[bot] = t_l
                dice[l] = t_top
            elif c == 3:
                dice[top] = t_b
                dice[f] = t_top
                dice[bot] = t_f
                dice[b] = t_bot
            elif c == 4:
                dice[bot] = t_b
                dice[f] = t_bot
                dice[top] = t_f
                dice[b] = t_top

            if matrix[i][j] == 0:
                matrix[i][j] = dice[bot]
            else:
                dice[bot] = matrix[i][j]
                matrix[i][j] = 0
            
            print(dice[top])

            
        

        
        




if __name__ == '__main__':
    main()


