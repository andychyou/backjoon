import sys
from collections import deque

sys.stdin = open('test.txt','r')
input = sys.stdin.readline

matrix = None
visited = None
adj_dic = None
def bfs(start):
    global adj_dic, visited
    queue = deque([start])

    while queue:
        curr = queue.popleft()
        visited[curr[1]][curr[0]] = 1
        for bachoo in adj_dic[curr] :
            if visited[bachoo[1]][bachoo[0]] == 0:
                queue.append(bachoo)
    
    

        
        
        


def main():
    global matrix, visited,adj_dic
    T = int(input())
    for test in range(T):
        M,N,B = list(map(int,input().split()))
        visited = [[0]*M for x in range(N)]
        adj_dic = dict()
        for x in range(B):
            bachoo = tuple(map(int,input().split()))  #dict의 키로 list 못감
            if bachoo not in adj_dic:
                adj_dic[bachoo] = []
            for key in adj_dic.keys():
                if key != bachoo and ((abs(key[0] - bachoo[0]) <= 1 and key[1] == bachoo[1]) or (abs(key[1] - bachoo[1]) <= 1 and key[0] == bachoo[0])):
                    adj_dic[key].append(bachoo)

        answer = 0
        for key in adj_dic.keys():
            if visited[key[1]][key[0]] == 0:
                bfs(key)
                answer += 1

        print(answer)
            




if __name__ == '__main__':
    main()