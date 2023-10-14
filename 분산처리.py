import sys
# sys.stdin = open('test.txt','r')
input = sys.stdin.readline

def main():
    T = int(input())
    for t in range(T):
        a,b = map(int,input().split())
        N = a**b
        while N >= 10:
            N %= 10
        print(N)

if __name__ == '__main__':
    main()