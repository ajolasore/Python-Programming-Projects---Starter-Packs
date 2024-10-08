t = float(input("give the temperature in kelvin:"))
l = float(input("give the relaive intensity:"))

if 0 <= t <= 30000 and l >= 10000:
    print ("supergiants (a)")
elif  0 <= t <= 30000 and 10000 >= l >= 1000:
    print ("supergiants (b)")
elif  0 <= t <= 7500 and 1000 >= l >= 100:
    print ("bright giants")
elif  0 <= t <= 6000 and 100 >= l >= 10:
    print ("giants")
elif  5000 <= t <= 30000 and  0.01 >= l >= 0.0001:
    print ("white dwarfs")
elif 3000 <= t <= 30000 and l <= 0.0001:
    print ("white dwarfs")
else:
    print ("main sequence")
