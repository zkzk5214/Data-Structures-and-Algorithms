s = []
with open('rosalind_mer.txt', 'r') as f:
    for line in f:
        nums = list(map(int, line.split(' ')))
        s = s + nums
print(" ".join(str(i) for i in sorted(s)))

