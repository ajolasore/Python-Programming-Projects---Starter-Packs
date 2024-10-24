def even_odd(number):

    """
    >>> even_odd(886328712442992)
    (10, 5)
    >>> even_odd(10515)
    (1, 4)
    >>> even_odd(145)
    (1, 2)
    """

def step(number):

    """
    >>> step(886328712442992)
    10515
    >>> step(10515)
    145
    >>> step(145)
    123
    """

def steps(number):

    """
    >>> steps(886328712442992)
    3
    >>> steps(1217637626188463187643618416764317864)
    4
    >>> steps(0)
    2
    >>> steps(1)
    5
    >>> steps(2)
    2
    >>> steps(3)
    5
    """
def even_odd(n):
    even_count = odd_count = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

def step(n):
    even, odd = even_odd(n)
    return int(str(even) + str(odd) + str(odd+even))

def steps(n):
    count = 0
    while n != 123:
        n = step(n)
        count += 1
    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()
