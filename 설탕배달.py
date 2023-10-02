import sys

input = sys.stdin.readline



def main():
    N = int(input())
    three,five = 0,0
    cnt = -1
    while 3*three + 5*five <= N: # == N일 때 안의 if문을 실행시켜야 하니까 <=로 조건을 검
        while 3*three + 5*five < N:
            three += 1
        if 3*three + 5*five == N:
            if cnt == -1 or cnt > three+five:
                cnt = three + five
        five += 1
        three = 0

    print(cnt)
    


if __name__=='__main__':
    main()