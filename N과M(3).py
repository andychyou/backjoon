import sys

sys.stdin = open('test.txt','r')
input = sys.stdin.readline


def Fombination(li, k, current_c, total_c):
    if len(current_c) == k:
        total_c.append(current_c[:])
        return
    
    for i in range(0, len(li)):
        if len(current_c) > 0:
            if li[i] >= current_c[len(current_c)-1]:
                temp = current_c[:]
                temp.append(li[i])
                Fombination(li, k, temp, total_c)
        else:
            temp = current_c[:]
            temp.append(li[i])
            Fombination(li, k, temp, total_c)


def main():
    N,M = list(map(int, input().split()))
    li = list(range(1, N+1))
    total_c = []
    Fombination(li, M, [], total_c)
    for c in total_c:
        for e in c:
            print(e, end=' ')
        print()




if __name__ == '__main__':
    main()