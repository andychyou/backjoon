import sys


def main():
    L,U = map(int,input().split())
    answer = 0

    def get_tens(i):
        if i == 1:
            return 45
        
        base = get_tens(i-1)
        return base * 10 + 45 * (10**(i-1))
        
    def get_sum(n):
        if n <=0 :
            return 0
        l = list(str(int(n)))
        l_sum = 0
        for i in range(1,len(l)):
            l_sum += get_tens(i)
        for i in range(len(l)-1):
            l_sum += int(l[i]) * (int(''.join(l[i+1:]))+1)
        l_sum += sum(range(int(l[-1])+1))
        return l_sum
    answer = get_sum(U) - get_sum(L-1)
    print(answer)
    




if __name__ == '__main__':
    main()


    # 0 1 2 3 4 5 6 7 8 9 -> 45
    # 10 11 12 13 14 15 16 17 18 19 -> 45 + 1*10 = 55
    # 20 21 22 23 24 25 26 27 28 29 -> 45 + 2*10 = 65

    # 90                            -> 45 + 9*10 = 135

    # 0 - 99 -> 900          45*10 + 45*10

    # 100                        199 -> 1*100 + 900

    # 900                        999 -> 9*100 + 900

    # 0 - 999 -> 13500          900*10 + 45*100
