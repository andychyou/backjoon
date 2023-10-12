import sys

sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import copy

answer = 0



def main():
    global answer
    N = int(input())
    # k 1 - 8
    col = [-1]*N

    def check(i,j,col):
        for c in range(len(col)):
            if col[c]

    
    def Backtrack(k, col):
        nonlocal N
        if k == N:
            return
        for i in range(N):
            for j in range(N):
                col_temp = col[:]
                col_temp[i] = j
                Backtrack(k+1, col_temp)
    Backtrack(col,N,0)
    print(answer)






if __name__ == '__main__':
    main()