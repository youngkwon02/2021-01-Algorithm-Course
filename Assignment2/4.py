def binary_search(arr, target, min, max):
    minimum_index = min
    maximum_index = max
    middle_index = (minimum_index + maximum_index) // 2

    if minimum_index > maximum_index:
        return -1
    elif minimum_index == maximum_index:
        if arr[middle_index] != target:
            return -1

    if arr[middle_index] == target:
        return middle_index
    elif arr[middle_index] < target:
        return binary_search(arr, target, middle_index + 1, maximum_index)
    else:
        return binary_search(arr, target, minimum_index, middle_index)


SampleArr = [12, 34, 37, 45, 57, 82, 99, 120, 134]
result = binary_search(SampleArr, 120, 0, len(SampleArr) - 1)

if result == -1:
    print("120 is not in the list")
else:
    print("The index of 120 in the list is", result)