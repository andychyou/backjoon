import sys

sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

def main():
    N, L = map(int, input().split())
    holes = []
    if N > 0 :
        holes = list(map(int, input().split()))
    
    holes.sort()
    i = 0
    cnt = 0
    while i < N:
        j = i + 1
        while j < N and holes[j] - holes[i] + 1 <= L:
            j += 1
        cnt += 1
        i = j
    print(cnt)





if __name__ == '__main__':
    main()