import sys

N = None

line = []
cnt = 0
def Hanoi(curr,s,e,temp):
    global line,cnt
    if curr == 1:
        line.append([s,e])
        cnt+=1
        return 
    Hanoi(curr-1,s,temp,e)
    line.append([s,e])
    cnt+=1
    Hanoi(curr-1,temp,e,s)



def main():
    global N
    N = int(sys.stdin.readline())
    Hanoi(N,1,3,2)
    print(cnt)
    for x in line:
        print(x[0],x[1])

if __name__ == '__main__':
    main()