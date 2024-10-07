import math
from math import sin, cos, asin, acos, radians

# Given values as input from the user (convert to float)
x1 = radians(float(input("Enter latitude (x1) in degrees: ")))
y1 = radians(float(input("Enter longitude (y1) in degrees: ")))
x2 = radians(float(input("Enter latitude (x2) in degrees: ")))
y2 = radians(float(input("Enter longitude (y2) in degrees: ")))

r = 6371  # Radius of the Earth in kilometers

# Calculate the formula
d = r * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))


# Print the result
print(f"The great-circle distance is {round(d)} km.")