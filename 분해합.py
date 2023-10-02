import sys
from collections import deque

input = sys.stdin.readline


def main():
    N = int(input())
    lowest = 0
    for x in range(N):
        whole = x
        singles = deque()
        while x > 0:
            mod = x % 10
            x = x // 10
            singles.append(mod)
        if whole + sum(singles) == N:
            if lowest == 0 or whole < lowest:
                lowest = whole
    print(lowest)




if __name__ == '__main__':
    main()