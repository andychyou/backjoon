import sys

sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import copy

answer = 0

def Check(N, k, col):
    flag = True
    for i in range(N):
        if col[i] != 0:
            if col[i] == col[k] or y == x - i + j or y == -(x-i) + j:
                flag = False
                break
    return flag

def Backtrack( col, N, k):
    global answer
    if k == N:
        answer += 1
        return
    if Check(N,k,col):
        for c in range(N):
            temp_col = col[:]
            temp_col[k] = c
            Backtrack(temp_col, N, k+1)






def main():
    global answer
    N = int(input())
    # k 1 - 8
    col = [0]*N
    Backtrack(col,N,0)
    print(answer)






if __name__ == '__main__':
    main()