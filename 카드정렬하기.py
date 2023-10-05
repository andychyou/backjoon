import sys

sys.stdin = open('test.txt','r')
input = sys.stdin.readline


def main():
    N = int(input())
    cards = []
    for x in range(N):
        cards.append(int(input()))
    

if __name__ == '__main__':
    main()