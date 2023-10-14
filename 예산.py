import sys

sys.stdin = open('test.txt','r')
input = sys.stdin.readline

yesans = None

def isValid(mid):
    return sum([min(x, mid) for x in yesans]) <= cap



def main():
    global yesans,cap
    N = int(input())
    yesans = list(map(int, input().split()))
    yesans.sort()
    cap = int(input())

    low = 0
    high = yesans[-1]
    mid = (low+high) // 2
    ans = high
    while low <= high:
        if isValid(mid):
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
        mid = (low+high) // 2
            
    
    
    print(ans)

    

if __name__ == '__main__':
    main()