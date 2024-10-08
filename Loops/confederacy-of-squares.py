name = input()
birth_year = int(input())

from datetime import date
current_year = date.today().year

ag = birth_year ** (1/2)
age = round(ag) +1

if age**2 == birth_year + age and age**2 < current_year:
    print(f'{name} was {age} in {age**2}.')
elif age**2 == birth_year + age and age**2 > current_year:
    print(f'{name} turns {age} in {age**2}.')
else:
    print(f'{name} is not a member of the Confederacy of Squares.')
