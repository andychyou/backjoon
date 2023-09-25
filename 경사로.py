from collections import deque
import sys 

sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

N, L = map(int, input().split())

matrix = [[0] * N for x in range(N)]
slop_matrix = [[0] * N for x in range(N)]

for x in range(N):
    matrix[x] = list(map(int,input().strip().split()))

answer = 0

#행
for x in range(N):
    line_set = set(matrix[x])
    if len(line_set) == 1:
        answer += 1
        continue
    flag = True
    for y in range(N-1):
        #오른쪽 경사로
        if matrix[x][y] - matrix[x][y+1] == 1:
            if not (y+L <= N-1 and len(set(matrix[x][y+1:y+1+L])) == 1):
                flag = False
                break
            for i in range(y+1, y+1+L):
                if(slop_matrix[x][i] == 1):
                    flag = False
                    break
            if flag==True:
                for i in range(y+1, y+1+L):
                    slop_matrix[x][i] = 1

        #왼쪽 경사로
        elif matrix[x][y] - matrix[x][y+1] == -1 :
            if not (y-L+1 >= 0 and len(set(matrix[x][y-L+1:y+1])) == 1):
                flag = False
                break
            for i in range(y-L+1, y+1):
                if(slop_matrix[x][i] == 1):
                    flag = False
                    break
            if flag==True:
                for i in range(y-L+1, y+1):
                    slop_matrix[x][i] = 1
        elif abs(matrix[x][y] - matrix[x][y+1]) > 1:
            flag = False
            break
    if flag == True:
        answer += 1
    else:
        slop_matrix[x] = [0]*N

matrix_flipped = []
slop_matrix_flipped = [[0] * N for x in range(N)]
for x in range(N):
    matrix_line = []
    for y in range(N):
        matrix_line.append(matrix[y][x])
    matrix_flipped.append(matrix_line)

for x in range(N):
    line_set = set(matrix_flipped[x])
    if len(line_set) == 1:
        answer += 1
        continue
    flag = True
    for y in range(N-1):
        #오른쪽 경사로
        if matrix_flipped[x][y] - matrix_flipped[x][y+1] == 1:
            if not (y+L <= N-1 and len(set(matrix_flipped[x][y+1:y+1+L])) == 1):
                flag = False
                break
            for i in range(y+1, y+1+L):
                if(slop_matrix_flipped[x][i] == 1):
                    flag = False
                    break
            if flag==True:
                for i in range(y+1, y+1+L):
                    slop_matrix_flipped[x][i] = 1
            
        #왼쪽 경사로
        elif matrix_flipped[x][y] - matrix_flipped[x][y+1] == -1 :
            if not (y-L+1 >= 0 and len(set(matrix_flipped[x][y-L+1:y+1])) == 1):
                flag = False
                break
            for i in range(y-L+1, y+1):
                if(slop_matrix_flipped[x][i] == 1):
                    flag = False
                    break
            if flag==True:
                for i in range(y-L+1, y+1):
                    slop_matrix_flipped[x][i] = 1
        elif abs(matrix_flipped[x][y] - matrix_flipped[x][y+1]) > 1:
            flag = False
            break
    if flag == True:
        answer += 1
    else:
        slop_matrix_flipped[x] = [0]*N


print(answer)