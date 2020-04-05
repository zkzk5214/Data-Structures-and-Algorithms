from collections import Counter


def majority(arr):
    freqDict = Counter(arr)
    size = len(arr)
    for (key, val) in freqDict.items():
        if val > (size / 2):
            print(key)
            return
    print('-1')


if __name__ == "__main__":
    with open('rosalind_maj.txt', 'r') as f:
        for i in f.readlines():
            input_list = list(map(int, i.split()))
            # print(input_list)
            majority(input_list)
