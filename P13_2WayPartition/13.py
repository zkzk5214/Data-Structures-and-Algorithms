def two_way_partition(nums):
    pivot = nums[0]
    left = []
    right = []
    for num in nums[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    return left + [pivot] + right


if __name__ == '__main__':
    with open('rosalind_par.txt', 'r') as f:
        for i in f.readlines():
            data = list(map(int, i.split()))
            partition = two_way_partition(data)
            print(' '.join(map(str, partition)))





