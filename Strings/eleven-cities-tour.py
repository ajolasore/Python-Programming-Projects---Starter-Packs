map = input()
stamps = 0
holes = 0
citiesholes = ''

while map != 'finish':
    if '🔘' in map:
        holes = holes + map.count('🔘')
        citiesholes += map.replace('🔘','') + ', '
    else:
        holes == holes

    stamps += 1
    map = input()

print(f'# stamps: {stamps}')

if holes != 0:
    print(f'# holes: {holes} ({citiesholes[:-2]})')
else:
    print(f'# holes: {holes}')

if (stamps == 11) and (holes == 3):
    print(f'cross earned: yes')
else:
    print(f'cross earned: no')