x1 = input()
while x1 != 'stop':
    checkdigit = int(x1)
    for i in range(2,10):
        x = int(input())
        checkdigit += i * x
    checkdigit %= 11

    x10 = int(input())

    if x10 == checkdigit:
        print("OK")
    else:
        print("WRONG")
    x1 = input()