import sys

input = sys.stdin.readline


li = []
answer = 0

def main():
    global li,answer
    num = int(input())
    if num > 0:
        li = list(map(int, input().split()))
    li.sort()
    if len(li) % 2 == 0:
       answer = li[0] * li[len(li)-1]
    else:
        middle = len(li) // 2
        answer = li[middle]**2
    print(answer)




if __name__ == '__main__':
    main()