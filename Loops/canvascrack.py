tables = int(input())
table_value= int(input())
double_table = int(input())
outcome = str(input())

total_amount = 0

for i in range(1,tables+1):

    if i != tables or (i == tables and outcome == 'stopped'):
        total = i * table_value
        total += total_amount

        if i% double_table == 0:
            total = (total) *2
            print(f'table #{i} (x2): €{total}')
        else:
            print(f'table #{i}: €{total}')

        total_amount = (total)

    else:
        total_amount = total_amount / 2
        total_amount = int(total_amount)
        print(f'table #{i}: €{total_amount}')