
import sys
sys.stdin = open("test.txt", "r")

def turn_what(gear_list, index, gears):
    turn_list = [index]

    for x in range(index, 0, -1):
        if(gear_list[x-1][2] != gear_list[x][6]):
            turn_list.append(x-1)
        else:
            break
    
    for x in range(index, gears-1):
        if(gear_list[x][2] != gear_list[x+1][6]):
            turn_list.append(x+1)
        else:
            break
    turn_list.sort()
    return turn_list

def turn(li: list, dir, index):
    if dir == 1:
        first = li.pop()
        li.insert(0, first)
    elif dir == -1:
        last = li.pop(0)
        li.append(last)


def turn_all(turn_list, gear_list, index, dir):
    left = []
    for x in turn_list:
        if x < index : left.append(x)
    right = []
    for x in turn_list:
        if x > index : right.append(x)

    #첫 돌림
    turn(gear_list[index], dir, index)


    cur_dir = dir
    for x in left[::-1]:
        cur_dir = 1 if cur_dir == -1 else -1
        turn(gear_list[x], cur_dir, x)
    
    cur_dir = dir
    for x in right:
        cur_dir = 1 if cur_dir == -1 else -1
        turn(gear_list[x], cur_dir, x)

       

gear_list = []
gear_list.append(list(input()))
gear_list.append(list(input()))
gear_list.append(list(input()))
gear_list.append(list(input()))

num = int(input())
gears = len(gear_list)


for x in range(num):
    input_ = input().split()
    index = int(input_[0]) -1
    dir = int(input_[1])
    turn_list = turn_what(gear_list, index, gears)
    turn_all(turn_list, gear_list, index, dir)
    # print('gear_list', gear_list)

answer = 0


for x in range(gears):
    if(gear_list[x][0] == '1'):
        answer += 2 ** x
print(answer)

    

 
