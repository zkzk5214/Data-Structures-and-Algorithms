def InvCount(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                count += 1

    return count


if __name__ == '__main__':
    with open('rosalind_inv.txt', 'r') as f:
        for i in f.readlines():
            n = list(map(int, i.split()))
            print(InvCount(n))
