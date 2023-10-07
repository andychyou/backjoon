import sys

from itertools import combinations

input = sys.stdin.readline


def SUM(li):
    sent = ''
    for s in li:
        sent += s
    return int(sent)



def main():
    li = list(input().strip())
    cut_li_index = [x for x in range(len(li)-1)]

    cnt = 0

    for cut in range(len(li)):
        combination = list(map(list,combinations(cut_li_index, cut)))
        for c in combination:
            if len(c) == 0:
                if SUM(li) <= 34:
                    cnt += 1
            else:
                s = 0
                something_bigger = False

                for i in range(len(c)):
                    if SUM(li[s:c[i]+1]) > 34:
                        something_bigger = True
                        break
                    s = c[i]+1
                if c[-1]+1 != len(li):
                    if SUM(li[c[-1]+1:]) > 34:
                        something_bigger = True
                if something_bigger == False:
                    cnt += 1
    
    print(cnt)
            



            
    

if __name__ == '__main__':
    main()

