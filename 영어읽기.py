import sys 
from collections import Counter

sys.stdin = open("test.txt", "r")
input = sys.stdin.readline


N = int(input())
vocas = []

for i in range(N):
    vocas.append(input().strip())

voca_dic = dict()
for voca in vocas:
    if(len(voca) == 1):
        voca_dic[voca] = ['']
        continue


    v_start = voca[0]
    v_end = voca[-1]
    v_between = str(sorted(list(voca[1:-1])))
    # v_between = Counter(v_between)
    if(v_start+v_end not in voca_dic):
        voca_dic[v_start+v_end] = [v_between]
    else:
        voca_dic[v_start+v_end].append(v_between)
    

M = int(input())
for i in range(M):
    answer = 1
    sentence = input().strip().split()
    for word in sentence:
        one_word = 0

        start = word[0]
        end = word[-1]
        between = str(sorted(list(word[1:-1])))
        a = start+end
        if len(word) == 1:
            a = word
            between = ''
        if(a in voca_dic):
            for voca_between in voca_dic[a]:
                if(between == voca_between):
                    one_word += 1
            
        answer *= one_word
    print(answer)



