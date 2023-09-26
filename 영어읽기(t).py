import sys 
from collections import Counter

sys.stdin = open("test.txt", "r")
input = sys.stdin.readline


N = int(input())
vocas = []

for i in range(N):
    vocas.append(input().strip())

M = int(input())
for i in range(M):
    answer = 1
    sentence = input().strip().split()
    for word in sentence:
        one_word = 0
        start = word[0]
        end = word[-1]
        between = word[1:-1]
        between = Counter(between)
        for voca in vocas:
            v_start = voca[0]
            v_end = voca[-1]
            v_between = voca[1:-1]
            v_between = Counter(v_between)
            
            if(start == v_start and end == v_end and between == v_between):
                one_word += 1
        answer *= one_word
    print(answer)



