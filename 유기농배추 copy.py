import sys
from collections import deque

sys.stdin = open('test.txt','r')
input = sys.stdin.readline


visited = None
adj_dic = None


def bfs(start):
    global adj_dic, visited
    visited.add(start)
    queue = deque([start])
    while queue:
        curr = queue.popleft()
        for bachoo in adj_dic[curr] :
            if bachoo not in visited:
                queue.append(bachoo)
                visited.add(bachoo)
    
    

        
        
        


def main():
    global  visited,adj_dic
    T = int(input())
    for test in range(T):
        visited = set()
        adj_dic = dict()
        M,N,B = list(map(int,input().split()))
        for x in range(B):
            bachoo = tuple(map(int,input().split()))  #dict의 키로 list 못감
            if bachoo not in adj_dic:
                adj_dic[bachoo] = []
            for key in adj_dic.keys():
                if  ((abs(key[0] - bachoo[0]) <= 1 and key[1] == bachoo[1]) or (abs(key[1] - bachoo[1]) <= 1 and key[0] == bachoo[0])):
                    adj_dic[key].append(bachoo)

        answer = 0
        for key in adj_dic.keys():
            if key not in visited:
                bfs(key)
                answer += 1

        print(answer)
            




if __name__ == '__main__':
    main()