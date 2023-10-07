import sys 
from collections import deque
from itertools import combinations

input = sys.stdin.readline
cache = []

def Fib(n):
    global cache
    if cache[n] == -1:
        cache[n] = Fib(n-1) + Fib(n-2)

    return cache[n]

def main():
    global cache
    N = int(input())
    cache = [-1] * (N+1)
    cache[0] = 0
    cache[1] = 1
    print(Fib(N))




if __name__ == '__main__':
    main()
