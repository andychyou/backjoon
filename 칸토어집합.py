import sys 

sys.stdin = open('test.txt','r')
input = sys.stdin.readline


def Do(sentence, s, e):
    if len(sentence[s:e+1]) == 1:
        return
    a1 =  s + (e+1-s) // 3
    a2 =  s + 2*(e+1-s) // 3
    Do(sentence, s, a1-1)
    for i in range(a1, a2):
        sentence[i] = ' '
    Do(sentence, a2, e)


def main():
    # while N := input():
    #     sentence = list('-'*(3**int(N)))
    #     Do(sentence, 0, len(sentence)-1)
    #     for s in sentence:
    #         print(s,end='')
    #     print()
    lines = sys.stdin.readlines()
    for line in lines:
        sentence = list('-'*(3**int(line)))
        Do(sentence, 0, len(sentence)-1)
        for s in sentence:
            print(s,end='')
        print()


if __name__ == '__main__':
    main()