import sys
import heapq
import bisect

sys.stdin = open('test.txt','r')
input = sys.stdin.readline

def Print(string, li):
    print(string, sorted(li, reverse=True))

def main():
    N,P = map(int, input().split())
    guitar = [[] for string in range(7)]

    cnt = 0
    
    for m in range(N):
        string, fret = map(int, input().split())
        fret = -fret

        #기타 안에 찾고자 하는 element가 없는 경우
        #없는 경우에는 bisect_left가 list len을 반환하기 때문에 list 마지막 원소가 element와 같은지 확인해야 한다
        # if bisect.bisect_left(guitar[string], fret) == len(guitar[string]) and guitar[string][-1] != fret:

        #없는 경우

        if len(guitar[string]) == 0:
            heapq.heappush(guitar[string], fret)
            cnt += 1
            continue

    

        if fret < guitar[string][0]:
            heapq.heappush(guitar[string], fret)
            cnt += 1
      
        elif fret > guitar[string][0]:
            while len(guitar[string]) >0 and guitar[string][0] < fret:
                top = heapq.heappop(guitar[string])
                cnt += 1   
            if len(guitar[string]) == 0:
                heapq.heappush(guitar[string], fret)
                cnt += 1 

            elif fret < guitar[string][0]:
                heapq.heappush(guitar[string], fret)
                cnt += 1
                


    print(cnt)
    


if __name__ == '__main__':
    main()