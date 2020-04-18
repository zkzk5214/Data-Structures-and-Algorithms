def zip1(x):
    if (x == 0):
        return 1
    if x == 1:
        return 2
    if (x >= 2):
        return 2*zip1(x-1)*zip1(x-2)


print(zip1(3))