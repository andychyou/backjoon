import sys

matrix = None

def PrintMatrix():
    global matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j],end='')
        print()


def Do(y_s, y_e, x_s,x_e):
    if y_e - y_s == 0:
        return
    y_a1 = y_s + (y_e-y_s+1) // 3
    y_a2 = y_s + 2*(y_e-y_s+1) // 3
    x_a1 = x_s + (x_e-x_s+1) // 3
    x_a2 = x_s + 2*(x_e-x_s+1) // 3
    global matrix
    for i in range(x_a1, x_a2):
        for j in range(y_a1,y_a2):
            matrix[i][j] = ' '
    Do(y_s,y_a1-1,x_s,x_a1-1)
    Do(y_a1,y_a2-1,x_s,x_a1-1)
    Do(y_a2,y_e,x_s,x_a1-1)
    Do(y_s,y_a1-1,x_a1,x_a2-1)
    Do(y_a2,y_e,x_a1,x_a2-1)
    Do(y_s,y_a1-1,x_a2,x_e)
    Do(y_a1,y_a2-1,x_a2,x_e)
    Do(y_a2,y_e,x_a2,x_e)

    



def main():
    N = int(sys.stdin.readline())
    global matrix
    matrix = [['*']*N for x in range(N)]
    s = 0
    e = N-1

    Do(s,e,s,e)

    PrintMatrix()


if __name__ == '__main__':
    main()