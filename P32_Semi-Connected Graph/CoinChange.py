def count(X, n, v):
    """
    Dynamic Programming  of Coin Change problem
    :param X: list
    :param n: int
    :param v: int
    :return: boolean
    """
    # table[i] will be storing the number of solutions for value i.
    table = [0 for k in range(v + 1)]
    table[0] = 1

    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the picked coin
    for i in range(0, n):
        for j in range(X[i], v + 1):
            table[j] += table[j - X[i]]

    return True if table[v] != 0 else False


if __name__ == '__main__':
    nums = [5, 10]
    m = len(nums)
    n = 12
    x = count(nums, m, n)
    print(x)
