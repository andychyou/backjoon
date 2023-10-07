import sys

input = sys.stdin.readline


def bicheck(c, sanggun, low, high, mid):
    if low <= high:
        if sanggun[mid] > c:
            high = mid - 1
        else:
            low = mid + 1
        mid = (low + high) // 2
        return bicheck(c,sanggun,low,high,mid)
    else:
        if sanggun[mid] == c:
            return 1
        else:
            return 0
def main():
    N = int(input())
    sanggun = sorted(list(map(int, input().split())))
    N = int(input())
    check = map(int, input().split())


    low = 0
    high = len(sanggun)-1
    mid = (len(sanggun)-1) // 2

    for c in check:
        print(bicheck(c, sanggun, low, high, mid), end = ' ')

if __name__ == '__main__':
    main()