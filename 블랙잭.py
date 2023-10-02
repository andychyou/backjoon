import sys


input = sys.stdin.readline

N,M = 0,0
def main():
    global N,M
    N,M = list(map(int, input().split()))
    answer = -1
    if N > 0:
        cards = list(map(int, input().split()))
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            for k in range(j+1, len(cards)):
                if cards[i] + cards[j] + cards[k] <= M and answer < cards[i] + cards[j] + cards[k]:
                    answer = cards[i] + cards[j] + cards[k] 
    print(answer)

        


if __name__ == '__main__':
    main()