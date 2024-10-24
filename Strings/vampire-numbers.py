vamp = input("Enter a vampire number: ")
l = len(vamp)

vampirenumber = False

if l %2 == 0:
    l//=2
    for x in range(10 ** (l-1), 10 ** l):
        if int(vamp) % x == 0:
            y = int(vamp)//x
            if  ((x % 10 != 0) or (y % 10 != 0)) and (sorted(str(x) + str(y)) == sorted(vamp)):
                vampirenumber = True
                
if vampirenumber:
    print(f'{vamp} is a vampire number.')
else:
    print(f'{vamp} is not a vampire number.')
