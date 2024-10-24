def isISBN(code):

    """
    Returns True is the argument is a string that contains a valid ISBN-10 code,
    False otherwise.

    >>> isISBN('9971502100')
    True
    >>> isISBN('9971502108')
    False
    >>> isISBN('53WKEFF2C')
    False
    >>> isISBN(4378580136)
    False
    """
    
def isISBN(code):
    if not isinstance(code, str):
        return False
    if len(code) != 10:
        return False
    if not code[1:9].isdigit():
        return False
    checkdigit = int(code[0])
    for i in range(2, 10):
        x = int(code[i-1])
        checkdigit += i * x
    checkdigit %= 11
    x10 = code[9]
    return (checkdigit == 10 and x10 == 'X') or x10 == str(checkdigit)
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
