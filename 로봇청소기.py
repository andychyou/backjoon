import sys
from itertools import combinations, permutations
import heapq
from collections import deque

sys.stdin = open('test.txt','r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def main():
    N,M = map(int,input().split())
    r,c,dir = map(int, input().split())
    matrix = []
    for n in range(N):
        matrix.append(list(map(int,input().split())))
    move_i = [-1,0,1,0]
    move_j = [0,1,0,-1]

    answer = 0
    def RobotMove(i,j,dir):
        nonlocal matrix, answer
        if matrix[i][j] == 0:
            matrix[i][j] = 2
            answer += 1
        
        all_clean = True
        for d in range(4):
            if matrix[i+move_i[d]][j+move_j[d]] == 0:
                all_clean = False
                break
        
        if all_clean:
            back = (dir+2) % 4 
            i = i+move_i[back]
            j = j+move_j[back]
            if  matrix[i][j] == 1:
                return
            else:
                RobotMove(i,j,dir)
        
        else:
            while True:
                dir = (dir+3) % 4
                if matrix[i+move_i[dir]][j+move_j[dir]] == 0:
                    i = i+move_i[dir]
                    j = j+move_j[dir]
                    RobotMove(i,j,dir)
                    break

        

        
    RobotMove(r,c,dir)
    print(answer)


    
if __name__ == '__main__':
    main()