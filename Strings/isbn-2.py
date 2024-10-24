code = input()
while code != 'stop':
    checkdigit = int(code[0])
    for i in range(2, 10):
        x = int(code[i-1])
        checkdigit += i * x
    checkdigit %= 11

    x10 = code[9]
    if (checkdigit == 10 and x10 == 'X') or x10 == str(checkdigit):
        print ('OK')
    else:
        print('WRONG')

    code = input()
