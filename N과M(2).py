import sys

sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline


def Combination(li, k, start, current_c, total_c):
    if len(current_c) == k:
        total_c.append(current_c[:])
        return
    
    for i in range(start, len(li)):
        if li[i] not in current_c:
            temp = current_c[:]
            temp.append(li[i])
            Combination(li, k, i+1, temp, total_c)



def main():
    N, M = list(map(int, input().split()))
    li = list(range(1,N+1))
    total_c = []
    Combination(li,M,0,[],total_c)
    for c in total_c:
        for e in c:
            print(e,end=' ')
        print()


if __name__ == '__main__':
    main()