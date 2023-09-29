import sys
from collections import deque

sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
N = 0

def NewDir(current_dir, turn):
    if turn == 'L':
        new_dir = (current_dir - 1 + 4) % 4
    else:
        new_dir = (current_dir + 1 + 4) % 4

    return new_dir

def CheckDead(snake, head_x, head_y):
    global N
    if head_x >= N or 0 > head_x:
        return False
    elif head_y >= N or 0 > head_y:
        return False
    else:
        if [head_x,head_y] in snake:
            return False
        return True


    

def main():
    global N
    N = int(input())
    K = int(input())
    apples = deque()
    for x in range(K):
        apples.append(list(map(int, input().split())))
    for x in range(len(apples)):
        apples[x][0] -= 1
        apples[x][1] -= 1
    L = int(input())
    moves = deque()
    for x in range(L):
        moves.append(list(input().split()))
    
    snake = deque([[0,0]])
    head_x = 0
    head_y = 0
    dir = 1 #0->북 1->동 2->남 3->서
    clock = 0
    is_alive = True
    while is_alive:
        clock += 1
        if dir == 0:
            head_x -= 1
        elif dir == 1:
            head_y += 1
        elif dir == 2:
            head_x += 1
        elif dir == 3:
            head_y -= 1
        is_alive = CheckDead(snake,head_x,head_y)
        snake.append([head_x, head_y])
        if [head_x, head_y] not in apples:
            snake.popleft()
        else:
            apples.remove([head_x,head_y])
        if len(moves) !=0 and int(moves[0][0]) == clock:
            dir = NewDir(dir, moves[0][1])
            moves.popleft()
       

        

    print(clock)





if __name__ == '__main__':
    main()