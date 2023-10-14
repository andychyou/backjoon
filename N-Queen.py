import sys

input = sys.stdin.readline

def main():
    N = int(input())
    col = [-1] * N
    cnt = 0

    def check(k, col):
        promising = True
        for c in range(k):
            if col[c] == col[k] or (abs(col[c] - col[k]) == abs(c - k)):
                promising = False
                break
        return promising
        # for i in range(k):
        #     if col[k] == col[i] or abs(col[k] - col[i]) == abs(k - i):
        #         return False

        # return True
    
     


    def Backtrack(k, col):
        nonlocal N, cnt
        if k == N:
            cnt += 1
            return
        for i in range(N):
            col[k] = i
            if check(k, col):
                Backtrack(k + 1, col)

    Backtrack(0, col)
    print(cnt)

if __name__ == '__main__':
    main()
