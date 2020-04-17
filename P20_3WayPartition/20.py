def ThreeWayPartition(nums):
    pivot = nums[0]
    small, equal, large = [], [], []

    for num in nums:
        if num < pivot:
            small.append(num)
        elif num > pivot:
            large.append(num)
        else:
            equal.append(num)

    return small + equal + large


if __name__ == '__main__':
    with open('rosalind_par3.txt', 'r') as f:
        for i in f.readlines():
            data = list(map(int, i.split()))
            partition = ThreeWayPartition(data)
            print(' '.join(map(str, partition)))
