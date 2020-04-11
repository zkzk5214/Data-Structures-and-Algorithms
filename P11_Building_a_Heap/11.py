def heapify(list, n, i):
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
        heapify(list, n, largest)


def buildHeap(list, n):
    # Last non-leaf node
    startIdx = int((n / 2)) - 1
    # each node heapify
    for i in range(startIdx, -1, -1):
        heapify(list, n, i)


def printHeap(list, n):
    for i in range(n):
        print(list[i], end=" ")
    print()


if __name__ == '__main__':
    with open('rosalind_hea.txt', 'r') as f:
        for i in f.readlines():
            input_list = list(map(int, i.split()))

    n = len(input_list)
    buildHeap(input_list, n)
    printHeap(input_list, n)
