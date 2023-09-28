import sys

sys.stdin = open('test.txt','r')
input = sys.stdin.readline

N = 0
K = 0
count = 0
thing = -1

def Merge(arr, p, q, r):
    global K, count, thing

    if count >= K:
        return

    i = p ; j = q+1; t = p;
    temp = []
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
            
        else:
            temp.append(arr[j])
            j += 1
        t += 1
    while i <= q:
        temp.append(arr[i])
        i += 1
        t += 1
    while j <= r:
        temp.append(arr[j])
        j += 1
        t += 1

    i = 0
    for x in range(p, r+1):
        arr[x] = temp[i]
        i += 1
        count += 1
        if count == K:
            thing = arr[x]
            return

    



def MergeSort(arr,  p,r ):
    if p < r and count < K:
        q = (p+r) // 2
        MergeSort(arr,  p, q)
        MergeSort(arr,  q+1, r)
        Merge(arr, p, q, r)
    
    return 



def main():
    global N,K
    N, K = list(map(int,input().split()))
    arr  = list(map(int,input().split()))
    MergeSort(arr,0,N-1)
    print(thing)
    


if __name__ == '__main__':
    main()