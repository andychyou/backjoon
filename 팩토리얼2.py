import sys

sys.stdin = open('test.txt','r')
input = sys.stdin.readline


def Fact(num, answer):
    return num * answer




def main():
    N = int(input())
    answer = 1
    for x in range(1,N+1):
        answer = Fact(x, answer)
    print(answer)



if __name__ == '__main__':
    main()
