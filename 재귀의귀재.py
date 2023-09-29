import sys

sys.stdin = open('test.txt','r')
input = sys.stdin.readline



def is_P(sentence, l, r, cnt):
    cnt += 1
    if l >= r:
        return [1, cnt]
    elif sentence[l] != sentence[r]:
        return [0, cnt]
    else:
        return is_P(sentence,l+1,r-1,cnt)



def main():
    T = int(input())
    for test in range(T):
        sentence = input().strip() #readline은 \n도 가져온다
        ans1, ans2 = is_P(sentence,0,len(sentence)-1,0)
        print(ans1, ans2)


if __name__=='__main__':
    main()