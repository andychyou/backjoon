import sys
from itertools import combinations

sys.stdin = open("test.txt",'r')
input = sys.stdin.readline

N = 0
answer = -1

def selectTeam(matrix, combination):
    global answer 
    for i in range(int(len(combination)/2)):
        a_power = 0
        b_power = 0
        team_a = combination[i]
        team_b = []
        for person in range(N):
            if person not in team_a:
                team_b.append(person)
        for p1 in team_a:
            for p2 in team_a:
                a_power += matrix[p1][p2]
        for p1 in team_b:
            for p2 in team_b:
                b_power += matrix[p1][p2]
        diff = abs(a_power - b_power)
        if answer == -1 or diff < answer:
            answer = diff






def main():
    global N,answer
    N = int(input())
    matrix = [[0]*N for _ in range(N)]
    for row in range(N):
        matrix[row] = list(map(int,input().split()))
    
    team_ppl = int(N / 2)

    combination = list(combinations(range(N),int(N/2)))
    team_a = []
    selectTeam(matrix, combination)
    print(answer)
    

        


if __name__ == '__main__':
    main()