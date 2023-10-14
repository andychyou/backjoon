import sys

sys.stdin = open('test.txt','r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline






def main():
    N,M = map(int,input().split())
    matrix=  [[]for n in range(N)]
    for n in range(N):
        matrix[n] = list(map(str, list(input().strip())))
    K = int(input())


    answer = 0
    
    dic = {}
    for n in range(N):
        if ''.join(matrix[n]) not in dic:
            dic[''.join(matrix[n])] = 1
        else:
            dic[''.join(matrix[n])] += 1
    dic = dict(sorted(dic.items(), key=lambda item:item[1], reverse=True))
    for r in dic:
        r_li = list(r)
        zero_num = 0
        for i in range(len(r_li)):
            if r_li[i] == '0':
                zero_num += 1
        if zero_num % 2 == 1:
            if K % 2 == 1 and zero_num <= K:
                answer = dic[r]
                
                break
        else:
            if K % 2 == 0 and zero_num <= K:
                answer = dic[r]
                
                break

    

    


    print(answer)


if __name__ == '__main__':
    main()