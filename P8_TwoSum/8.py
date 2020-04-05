def list_duplicates(input):
    x = -1
    y = -1
    for i, nums in enumerate(input):
        for j, item in enumerate(input[i + 1:]):
            if nums == -item:
                x = i
                y = j + i + 1
    if y == -1 and x == -1:
        return [-1]
    listToStr = ' '.join(map(str, [x + 1, y + 1]))
    return listToStr


with open('rosalind_2sum.txt', 'r') as f:
    for i in f.readlines():
        nums = list(map(int, i.split()))
        s = list_duplicates(nums)
        print(s)
