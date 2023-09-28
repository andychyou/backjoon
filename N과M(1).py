import sys 

sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline




def Permutation(li, k, current_p, total_p):
    if len(current_p) == k:
        total_p.append(current_p)
        return
    
    for e in li:
        if e not in current_p:
            temp = current_p[:]
            temp.append(e)
            Permutation(li, k, temp, total_p)





def main():
    N,M = list(map(int,input().split()))
    li = list(range(1,N+1))
    total_p = []
    Permutation(li, M, [], total_p)
    for p in total_p:
        for e in p:
            print(e,end=' ')
        print()



if __name__ == '__main__':
    main()