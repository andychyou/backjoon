import sys
sys.stdin = open('test.txt','r')
input = sys.stdin.readline


def main():
    M,N = map(int,input().split())
    matrix = [['0'] * N for x in range(M)]
    for r in range(M):
        matrix[r] = list(input().rstrip())
    
    cnt = -1

    for y in range(M-8+1):
        for x in range(N-8+1):
            cnt1 = 0
            cnt2 = 0
            #color black
            c = 'B'
            for i in range(y,8+y):
                for j in range(x,8+x):
                    if matrix[i][j] != c:
                        cnt1 += 1
                    if c == 'B':
                        c = 'W'
                    else:
                        c = 'B'
                
                if (i-y) % 2 == 0:
                    c = 'W'
                else:
                    c = 'B'
            
            c = 'W'
            for i in range(y,8+y):
                for j in range(x,8+x):
                    if matrix[i][j] != c:
                        cnt2 += 1
                    if c == 'W':
                        c = 'B'
                    else:
                        c = 'W'
                if (i-y) % 2 == 0:
                    c = 'B'
                else:
                    c = 'W'
            if cnt == -1 or min(cnt1,cnt2) < cnt:
                cnt = min(cnt1,cnt2)

            
    print(cnt)

if __name__ == '__main__':
    main()