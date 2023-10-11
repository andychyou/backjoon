import sys
from collections import deque
from itertools import combinations, permutations
import heapq

sys.stdin = open('test.txt','r')
input = sys.stdin.readline




def main():
    N = int(input())
    X_li = (list(map(int,input().split())))
    Y_li = (list(map(int, input().split())))
    
    answer = 0

    def SUM(X_li, Y_li):
        S = 0
        for i in range(len(X_li)):
            S += X_li[i] * Y_li[i]
        return S


    # for x in range(len(X_li)):
    #     for y in range(len(Y_li)):
    #         S = SUM(X_li, Y_li)
    #         if answer < S:
    #             answer = S
    #             print(X_li, Y_li)
    #         top = Y_li.popleft()
    #         Y_li.append(top)
    #     top = X_li.popleft()
    #     X_li.append(top)

    x_i = 0
    large_x = 0
    for x in range(N):
        if X_li[x] > large_x:
            large_x = X_li[x]
            x_i = x

    
    y_i = 0
    large_y = 0
    for y in range(N):
        if Y_li[y] > large_y:
            large_y = Y_li[y]
            y_i = y

    print(x_i, y_i)
    print(large_x, large_y)
    
    for i in range(N):
        answer += X_li[x_i] + Y_li[y_i]
        x_i = (x_i + 1) % N
        y_i = (y_i + 1) % N




    print(answer)

            




if __name__ == '__main__':
    main()