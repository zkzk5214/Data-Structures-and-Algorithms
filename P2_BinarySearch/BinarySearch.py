def BS(arrays, keys):
    res = []
    for j in range(len(keys)):
        for i in range(len(arrays)):
            if array[i] == key[j]:
                res.append(i + 1)
                break
            elif i == len(arrays)-1:
                res.append(-1)
    return res


if __name__ == "__main__":
    with open('rosalind_bins.txt', 'r') as f:
        i = f.readline()
        array = list(map(int, i.split()))
        j = f.readline()
        key = list(map(int, j.split()))
        print(' '.join(map(str, BS(array, key))))
