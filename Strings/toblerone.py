brandname = input()
city = input()

output = ''
index=0
indexcity = 0

while index < len(brandname) and indexcity < len(city):
    if brandname[index].lower() == city[indexcity].lower():
        output = output + '['+ brandname[index] + ']'
        index = index +1
        indexcity = indexcity +1
    else:
        output = output + brandname[index]
        index = index +1

output = output + brandname[index:]
output = output.replace('][','')
print(output)
