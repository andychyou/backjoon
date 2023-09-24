import sys

sys.stdin = open("test.txt", "r")

def build(current_building, adj_list, time, building_cost, target_building):
    global global_time
    if current_building == target_building:
        if global_time > time:
            global_time = time
        return
    for building in adj_list[current_building]:
        time += building_cost[building]
        build(building, adj_list, time, building_cost, target_building)



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
        if li[i][0] not in adj_list:
            adj_list[li[i][0]] = [li[i][1]]
        else:
            adj_list[li[i][0]].append(li[i][1])

    target_building = int(sys.stdin.readline())

    current_building = 1
    time = building_cost[1]
    global_time = 999999

    build(1, adj_list, time, building_cost, target_building)
    


    print(global_time)

        
    
    
    
