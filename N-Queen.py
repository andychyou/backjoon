from collections import deque
import sys

def PlaceQueen(i,j, N, board):
    for x in range(0, N):
        board[i][x] = 1
        board[x][j] = 1
        y1 = j + x - i
        y2 = j - (x - i)
        if(y1 >= 0 and y1 < N):
            board[x][y1] = 1
        if(y2 >= 0 and y2 < N):
            board[x][y2] = 1


def Count(N, board):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                cnt += 1
    return cnt

input = sys.stdin.readline

N = int(input())


cnt = 0
queen_cnt = 0
board = [[0]*N for _ in range(N)]

for x in range(N):
    for i in range(N):
        for j in range(N):
            if(board[i][j] == 0):
                PlaceQueen(i,j,N,board)
                queen_cnt += 1
if(queen_cnt == N):
    cnt += queen_cnt




# for x in range(N):
#     board = [[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             PlaceQueen(i,j,N,board)
#     cnt += Count(N, board)
    
print(cnt)