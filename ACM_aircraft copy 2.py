import sys

sys.stdin = open("test.txt", "r")

def build(current_building, adj_list, time, building_cost, target_building):
    global global_time
    global li
    if current_building == target_building:
        li.append(time)
        max = 0 
        for i in li:
            max = i if max < i else max
        global_time = max
        return
    
    for building in adj_list[current_building]:
        build(building, adj_list, time+building_cost[building], building_cost, target_building)
    


test_case = int(sys.stdin.readline())

for x in range(test_case):
    total_buildings, order_buildings = map(int, sys.stdin.readline().split())
    line = list(map(int, sys.stdin.readline().split()))


    #init building_cost
    building_cost = dict()
    for i in range(0, total_buildings):
        building_cost[i+1] = line[i]
    
    li = []
    for i in range(0 , order_buildings):
        li.append(list(map(int, sys.stdin.readline().split())))


    #init adj_list
    adj_list = dict()
    for i in range(0, order_buildings):
        if li[i][1] not in adj_list:
            adj_list[li[i][1]] = [li[i][0]]
        else:
            adj_list[li[i][1]].append(li[i][0])

    target_building = int(sys.stdin.readline())

    current_building = target_building
    time = building_cost[target_building]
    global_time = 999999
    li = []

    # print(building_cost)
    # print(adj_list)
    build(current_building, adj_list, time, building_cost, 1)
    


    print(global_time)

        
    
    
    
