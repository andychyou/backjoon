import sys

sys.stdin = open("test.txt", "r")
input = sys.stdin.readline


def build(building, prepare_dict, costs):
    global total, history
    if building not in prepare_dict:
        if history[building] == 0:
            history[building] = 1
            total += costs[building]
        return

    c_list = []
    for before in prepare_dict[building]:
        if history[before] == 0:
            c_list.append(costs[before])
            history[before] = 1
    if c_list:
        total += max(c_list)
    for before in prepare_dict[building]:
        build(before, prepare_dict, costs)



test_case = int(input())

for x in range(test_case):
    total_buildings, order_buildings = map(int, input().split())
    costs = list(map(int, input().split()))
    costs = [0] + costs 

    prepare_dict = dict()

    for i in range(0 , order_buildings):
        a,b = map(int,input().split())
        if b not in prepare_dict:
            prepare_dict[b] = [a]
        else:
            prepare_dict[b].append(a)
    
    print(prepare_dict)
    build_this = int(input())
    total = costs[build_this]
    history = [0] * (total_buildings+1)
    build(build_this, prepare_dict, costs)
    print(total)

    



    
    
    
