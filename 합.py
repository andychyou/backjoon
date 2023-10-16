import sys


def main():
    L,U = map(int,input().split())
    answer = 0

        
    def get_sum(n):
        if n <=0:
            return 0
        
        re = 0
        n_li = list(str(n))

        def get_tens(i):
            if i <= 0:
                return 0
            elif i == 1:
                return 45
            
            base = get_tens(i-1)
            return base * 10 + 45 * (10**(i-1))



        for i in range(len(n_li)):
            prev = list(map(int,n_li[:i+1]))
            z = len(n_li) - i - 1
            temp = sum(prev[:-1])
            lowest_prev = prev[-1]
       
            re += lowest_prev*get_tens(z)
            if len(prev) > 1:
                re += temp*lowest_prev*(10**z) + sum(range(lowest_prev+1))*10**z

            

        return re

            
    
    print(get_sum(L))
    


    # answer = get_sum(U) - get_sum(L-1)
    # print(answer)
    # print(get_sum(L))






if __name__ == '__main__':
    main()


    # 0 - 423
    # (0 - 3) * 10**2 + 4 * (23+1)
    # (0 - 3) * 45 * 10**1 + (0-1) * 10 + 2 * 3 *10**0
    # (0-41) * 45 + (0-3)



    # 10 11 12 13 14 15 16 17 18 19

