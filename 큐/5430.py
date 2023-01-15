from collections import deque

def Do_Operation(array: deque, command, leng):
    command = list(command)
    sort = True
    for w in command:
        if(w == 'R'):
            sort = not sort
            continue
        elif(w == 'D'):
            if(len(array) == 0):
                return [], "error"
            if(sort):
                array.popleft()
            else:
                array.pop()
            leng -= 1
    if(sort == False):
        array.reverse()
    return array, leng
            
def Print_Result(array: deque, leng):
    if(leng == "error"):
        print("error")
    else:
        if(leng == 0):
            print('[]')
        else:
            print('[', end='')
            for i in range(0,leng-1):
                print(array[i], end=',')
            print(array[leng-1], end=']\n')

test_case = int(input())

for i in range(0, test_case):
    command = input()
    leng = int(input())
    array = input()
    array = array[1:-1].split(',')
    new_array = deque()
    for j in range(0, leng):
        if(array[j] == ''): continue
        new_array.append(int(array[j]))
    result, leng = Do_Operation(new_array, command, leng)
    Print_Result(result, leng)
    
    
