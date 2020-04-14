def MaxHeapify(list, n, i):
    largest = i
    left = 2 * i + 1  # left
    right = 2 * i + 2  # right

    # Left child
    if left < n and list[left] > list[largest]:
        largest = left
    # Right child
    if right < n and list[right] > list[largest]:
        largest = right
    # Root is the largest
    if largest != i:
        temp = list[i]
        list[i] = list[largest]
        list[largest] = temp

        # Recursively
        MaxHeapify(list, n, largest)


def heapSort(list):
    n = len(list)

    # Build_Max_Heap
    for i in range(n, -1, -1):  # n to 0, step -1
        MaxHeapify(list, n, i)

    # Swap the first and the last, size--
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        MaxHeapify(list, i, 0)


if __name__ == '__main__':
    with open('rosalind_hs.txt', 'r') as f:
        for i in f.readlines():
            input_list = list(map(int, i.split()))
            heapSort(input_list)
            print(' '.join(map(str, input_list)))
