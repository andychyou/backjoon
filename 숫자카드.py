import sys

from itertools import combinations
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

cnt = 0
li = []

def SUM(li):
    sent = ''
    for s in li:
        sent += s
    return int(sent)



def cut(curr, cuts,  c_i):
    global cnt
    if curr == cuts and cuts != 0:
        if c_i < len(li):
            if SUM(li[c_i:]) <= 34:
                cnt += 1

    elif cuts == 0:
        if SUM(li) <= 34:
            cnt +=1

    else:
        s = c_i
        for x in range(s+1, len(li)):
            if SUM(li[s:x]) > 34:
                break
            else:
                cut(curr+1,cuts,x)



def main():
    global cnt, li
    li = list(input().strip())
    c_index_li = [x for x in range(len(li))]
    cnt = 0

    for cuts in range(0, len(li)):
        c_i = []
        cut(0, cuts, 0)

    
    print(cnt)
            



            
    

if __name__ == '__main__':
    main()

