def RosalindMedian(nums, k):
    if nums == [] or k > len(nums):
        return None
    nums.sort()
    return nums[k - 1]


if __name__ == "__main__":
    with open('rosalind_med.txt', 'r') as f:
        for i in f.readlines():
            input_list = list(map(int, i.split()))
            # print(input_list)

print(RosalindMedian(input_list, 74921))
