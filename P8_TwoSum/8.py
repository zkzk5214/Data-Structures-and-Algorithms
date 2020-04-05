with open('rosalind_2sum.txt', 'r') as f:
    for i in f.readlines():
        nums = list(map(int, i.split()))
        flag = 0
        for num in nums:
            if - num in nums and num is not - num:
                print([1 + nums.index(num), 1 + nums.index(- num)])
                break
            else:
                flag = -1
        if flag == -1:
            print(flag)
