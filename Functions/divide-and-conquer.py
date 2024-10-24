def longest_polydivisible_prefix(n):
    n_str = str(n)
    for i in range(1, len(n_str) + 1):
        if not ispolydivisible(int(n_str[:i])):
            return int(n_str[:i - 1])
    return n

def ispolydivisible(n):
    n_str = str(n)
    for i in range(1, len(n_str) + 1):
        if int(n_str[:i]) % i != 0:
            return False
    return True

def polydivisible_extensions(n):
    count = 0
    n_str = str(n)
    for i in range(10):
        if ispolydivisible(int(n_str + str(i))):
            count += 1
    return count