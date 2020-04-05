def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)     # add the biggest value in the merged list
    return merged   # return to the last right or left


with open('rosalind_ms.txt', 'r') as f:
    for i in f.readlines():
        input_list = list(map(int, i.split()))

s = mergeSort(input_list)

listToStr = ' '.join(map(str, s))
print(listToStr)
