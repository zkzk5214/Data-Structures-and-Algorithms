if __name__ == "__main__":
    with open('rosalind_qs.txt', 'r') as f:
        for i in f.readlines():
            input_list = list(map(int, i.split()))
            s = sorted(input_list)
            print(' '.join(map(str, s)))
