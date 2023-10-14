import sys
from collections import deque
from itertools import combinations, permutations
import heapq
import re


sys.stdin = open('test.txt','r')
input = sys.stdin.readline


def main():
    T = int(int(input()))
    for t in range(T):
        sent = input().rstrip()
        p = re.compile('(100+1+|01)+')
        if p.fullmatch(sent):
            print('YES')
        else:
            print("NO")
            




if __name__=='__main__':
    main()