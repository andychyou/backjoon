import sys

input = sys.stdin.readline


def find_value(N, i, remote_value, buttons):
    if i > len(N):
        return remote_value
    MSB = int(str(N)[i])
    temp = ''
    for x in range(i, N-1):
            temp += '0'
    if MSB in buttons:
        remote_value = int(str(MSB)+temp)
    else:
        distance = 999
        candidates = []
        for button in buttons:
            if abs(button - MSB) < distance:
                distance = abs(button - MSB)
                candidates = []
                candidates.append(button)
            elif abs(button - MSB) == distance:
                candidates.append(button) 
        if len(candidates) == 1:
            remote_value = int(str(candidates[0])+temp)
        else:
            if i+1 <= len(N):
                a = int(candidates[0]+'0')
                b = int(candidates[1]+'0')
                c = int(N[i:i+1])
                if abs(a-c) < abs(b-c):
                    remote_value = int(str(candidates[0])+temp)
                else:
                    remote_value = int(str(candidates[0])+temp)
            else:
                remote_value = int(str(candidates[0])+temp)
        find_value(N, i+1, remote_value, buttons)

def main():
    N = int(input())
    M = int(input())
    no_buttons = list(map(int, input().split()))
    buttons = [x for x in range(M)]
    for x in no_buttons:
        if x in buttons:
            buttons.remove(x)
    i = 0
    





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



