def PartialSort(nums, k):
    return sorted(nums)[:k]


INFILE = 'rosalind_ps.txt'

with open(INFILE) as f:
    for i in f.readlines():
        input_list = list(map(int, i.split()))
        input_list = (PartialSort(input_list, 846))
        print(' '.join(map(str, input_list)))
