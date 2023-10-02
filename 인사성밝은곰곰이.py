import sys
input = sys.stdin.readline


def main():
    N = int(input())
    cnt = 0
    while line := input().strip():
        if line == 'ENTER':
            user = set()
            continue
        else:
            if line not in user:
                user.add(line)
                cnt += 1
            

    print(cnt)




if __name__ == '__main__':
    main()