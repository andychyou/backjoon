N, k = input().split()
N = int(N)
k = int(k)

arr = input().split()
for i in range(0,len(arr)):
    arr[i] = int(arr[i])
arr.sort(reverse=True)
print(arr[k-1])