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
ds_list = deque()
for x in range(num):
    ds_list.append(DataStructure(line2[x], line1[x]))

arr_len = int(input())
arr = list(map(int, input().split()))

answer = []

for x in (arr):
    append = x
    for i in range(num):
        ds_list[i].append(append)
        append = ds_list[i].pop()
        # if(i < num-1):
        #     ds_list[i+1].append(pop)
        # else:
        #     answer.append(pop)
    answer.append(append)


for x in answer:
    print(x, end=' ')