import sys

input = sys.stdin.readline

def main():
    N = int(input())
    col = [-1] * N
    cnt = 0

    def check(i, j, col):
        promising = True
        for c in range(len(col)):
            if col[c] != -1:
                if col[c] == j or (abs(col[c] - j) == abs(c - i)):
                    promising = False
                    break
        return promising

    def Backtrack(k, col):
        nonlocal N, cnt
        if k == N:
            cnt += 1
            return
        for i in range(k,N):
            for j in range(N):
                if check(i, j, col):
                    col[i] = j
                    Backtrack(k + 1, col)
                    col[i] = -1

    Backtrack(0, col)
    print(cnt)

if __name__ == '__main__':
    main()
