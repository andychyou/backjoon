from collections import deque
import sys

# sys.stdin = open("test.txt", "r")

input = sys.stdin.readline

num = int(input())

class DataStructure:
    def __init__(self, data, type):
        self.type = type
        self.data = deque([data])
    def pop(self):
        if(self.type == 0):
            return self.data.popleft()
        else:
            return self.data.pop()
    def append(self, x):
        self.data.append(x)


line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))

queue_list = deque()
for x in range(num):
    if line1[x] == 0:
        queue_list.append(line2[x])
  
arr_len = int(input())
arr = list(map(int, input().split()))

answer = deque()

if(len(queue_list) == 0):
    answer = arr

else:
    for i in range(arr_len):
        queue_list.appendleft(arr[i])
        answer.append(queue_list.pop())
        # pop = queue_list.popleft()
        # queue_list.appendleft(arr[i])
        # answer.append(queue_list.pop())
        # queue_list.append(pop)




for x in answer:
    print(x, end=' ')