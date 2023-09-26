import sys

sys.stdin = open("test.txt", "r")
input = sys.stdin.readline
clicks = 99999999

def find_value(N, buttons, current):
    global clicks
    for button in buttons:
        temp = current+str(button)
        current_clicks = abs(N-int(temp)) + len(temp)
        if current_clicks < clicks:
            clicks = current_clicks
        if len(temp) < 6:
            find_value(N,buttons, temp)
        


    
def main():
    global clicks
    N = int(input())
    M = int(input())
    no_buttons = []
    if(M>0):
        no_buttons = list(map(int, input().split()))
    buttons = [x for x in range(10)]
    for x in no_buttons:
        if x in buttons:
            buttons.remove(x)
    clicks =  abs(N-100)

    
    find_value(N, buttons, '')
    print(clicks)
    





if __name__ == "__main__":
    main()









# MSB = int(N[0])
# if MSB in buttons: #첫자리가 고장남
#     left = str(N)[0]
#     for x in range(len(str(N))-1):
#         left += '0'
#     left = int(left)
#     right = str(int(str(N)[0])+1)
#     for x in range(len(str(N))-1):
#         right += '0'
#     right = int(right)



