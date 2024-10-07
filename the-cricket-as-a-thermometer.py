N60 = int(input("the number of observed chirps per minute:"))

TF = 50 + ((N60 - 40)/4)
TC = 10 + ((N60 - 40)/7)

print("temperature (Fahrenheit):", TF)
print("temperature (Celsius):", TC)