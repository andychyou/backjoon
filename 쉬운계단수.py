import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def solution(n):
    cache = [[0] * 10 for x in range(n+1)]
    if n >= 1:
        cache[1] = [1]*10
        cache[1][0] = 0
    if n>= 2:
        cache[2] = [2] * 10
        cache[2][0] = 1
        cache[2][1] = 1
        cache[2][9] = 1
    def f(N):
        nonlocal cache
        for n in range(3, N+1):
            for x in range(10):
                if x == 0:
                    cache[n][x] = cache[n-1][1]
                elif x == 9:
                    cache[n][x] = cache[n-1][8]
                else:
                    cache[n][x] = cache[n-1][x-1] + cache[n-1][x+1]
        return sum(cache[N])

    print(f(n) % 10**9)
                



def main():
    N = int(input())
    solution(N)
    



if __name__ == '__main__':
    main()