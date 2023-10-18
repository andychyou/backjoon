import sys




def main():
    L,U = map(int,input().split())
    answer = 0
    for a in range(L,U+1):
        a = list(map(int,list(str(a))))
        for b in a:
            answer += b
    print(answer)


if __name__ == '__main__':
    main()d