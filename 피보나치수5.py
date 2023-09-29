import sys 
from collections import deque
from itertools import combinations

input = sys.stdin.readline


def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)


def main():
    N = int(input())
    print(Fib(N))




if __name__ == '__main__':
    main()
