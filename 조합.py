N = 8


total_comb = []

def getPermutation(li, k, current_comb, total_comb):
    if len(current_comb) == k:
        total_comb.append(current_comb[:])
        return
    for x in li:
        if x not in current_comb:
            temp = current_comb[:]
            temp.append(x)
            getPermutation(li, k, temp)

def getCombination(li, k, start, current_comb,total_comb):
    if len(current_comb) == k:
        total_comb.append(current_comb[:])
        return
    for i in range(start, len(li)):
        if li[i] not in current_comb:
            temp = current_comb[:]
            temp.append(li[i])
            getCombination(li, k, i+1, temp,total_comb)

li = list(range(4))
total_comb = []
getCombination(li, 2, 0, [],total_comb)
print(total_comb)
print(len(total_comb))















