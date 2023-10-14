import sys
sys.setrecursionlimit(10**6)

sys.stdin = open('test.txt','r')
input = sys.stdin.readline


def main():
    N,M = map(int,input().split())
    matrix = []
    for n in range(N):
        matrix.append(list(map(int,list(input().strip()))))

    if len(matrix) < len(matrix[0]):
        shorter = len(matrix)
    else:
        shorter = len(matrix[0])
    
    size = 0
    answer = 0
    while size < shorter:
        for i in range(N-size):
            for j in range(M-size):
                a = matrix[i][j]
                li = [matrix[i+size][j], matrix[i][j+size], matrix[i+size][j+size]]
                found = True
                for b in li:
                    if a != b:
                        found = False
                        break
                if found:
                    answer = (size+1)**2
        size += 1

    print(answer)
if __name__ == '__main__':
    main()