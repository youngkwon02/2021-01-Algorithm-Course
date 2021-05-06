def pairSum(list, sum):
    occupied_index = []
    output = []
    for i in range(0, len(list)):
        for k in range(i + 1, len(list)):
            if list[i] + list[k] == sum:
                occupied_index.append((i,k))

    for i in range(0, len(occupied_index)):
        output.append(str(list[occupied_index[i][0]]) + "+" + str(list[occupied_index[i][1]]))
    
    print(output)

pairSum([2,4,3,5,6,-2,4,7,8,9], 7)