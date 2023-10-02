import sys

input = sys.stdin.readline





def main():
    N = int(input())
    cnt = 0
    current = 666
    while cnt < N:
        if '666' in str(current):
            cnt += 1
        if  cnt == N:
            break
        current += 1
    print(current)





if __name__ == '__main__':
    main()