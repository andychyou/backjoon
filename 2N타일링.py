import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
cache = []

def f(n):
    global cache

    for x in range(3, n+1):
        cache[x] = cache[x-1] + cache[x-2]

    return cache[n]

    

def main():
    global cache
    n = int(input())
    cache = [0] * (n+1)
    if n >= 1:
        cache[1] = 1
    if n >= 2:
        cache[2] = 2
    print(f(n) % 10007)
    

if __name__ == '__main__':
    main()