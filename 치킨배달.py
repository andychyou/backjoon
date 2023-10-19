import sys
from itertools import combinations
sys.setrecursionlimit(10**6)

sys.stdin = open('test.txt','r')
input = sys.stdin.readline


def main():
    N, M = map(int,input().split())
    matrix=[]
    chicks = []
    houses = []
    for n in range(N):
        matrix.append(list(map(int,input().split())))
        for j in range(N):
            if matrix[n][j] == 2:
                chicks.append((n,j))
            elif matrix[n][j] == 1:
                houses.append((n,j))
            
    answer = -1
    

    for selected in combinations(chicks, M):
        print(selected)
        total = 0
        for h in houses:
            smallest = -1
            for c in selected:
                dist = abs(c[0]-h[0]) + abs(c[1]-h[1])
                if smallest == -1 or smallest > dist:
                    smallest = dist
            total += smallest
        if answer == -1 or total < answer:
            answer = total


    
    print(answer)

if __name__=='__main__':
    main()