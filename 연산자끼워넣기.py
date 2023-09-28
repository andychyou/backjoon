import sys
from collections import deque
from itertools import permutations
import math
import copy
sys.stdin = open("test.txt","r")
input = sys.stdin.readline


N = 0
Largest = -1
Smallest = -1



def Calc(num1,num2,var):
    if var == '+':
        ret_val = num1+num2
    elif var == '-':
        ret_val = num1-num2
    elif var == '*':
        ret_val = num1*num2
    elif var == '/':
        if num1 < 0:
            ret_val = - math.trunc(abs(num1) / num2)
        else:
            ret_val = math.trunc(num1/num2)
    return ret_val




def Find(nums, var_permutation):
    global Largest, Smallest
    if len(nums) == 1:
        if Largest == -1 or Largest < nums[0]:
            Largest = nums[0]
        if Smallest == -1 or Smallest > nums[0]:
            Smallest = nums[0]
        return

    new_num = Calc(nums[0],nums[1],var_permutation[0])
    temp_nums = copy.deepcopy(nums)
    temp_var_permutation = copy.deepcopy(var_permutation)
    temp_nums.popleft()
    temp_nums.popleft()
    temp_nums.appendleft(new_num)
    temp_var_permutation.popleft()
    Find(temp_nums, temp_var_permutation)







def main():
    global N
    N = int(input())
    nums = deque(map(int,input().split()))
    vars_list = deque(map(int,input().split()))
    vars = deque()
    for x in range(vars_list[0]):
        vars.append('+')
    for x in range(vars_list[1]):
        vars.append('-')
    for x in range(vars_list[2]):
        vars.append('*')
    for x in range(vars_list[3]):
        vars.append('/')
    var_permutation = list(set(permutations(vars, N-1)))
    for p in var_permutation:
        Find(nums, deque(p))
    print(Largest)
    print(Smallest)




if __name__ == '__main__':
    main()