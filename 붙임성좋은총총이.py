import sys


input = sys.stdin.readline


def main():
    N = int(input())
    ppl = {'ChongChong'}
    for x in range(N):
        line = input().strip().split()
        for p in line:
            if p in ppl:
                for p in line:
                    if p not in ppl:
                        ppl.add(p)
                break
    print(len(ppl))
        



if __name__ == '__main__':
    main()