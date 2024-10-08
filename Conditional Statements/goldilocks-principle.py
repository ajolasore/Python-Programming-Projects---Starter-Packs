# Read input values
value = int(input())
lower_boundary = int(input())
upper_boundary = int(input())
quality_low = input()
quality_high = input()

# Check if the value is within the boundaries
if lower_boundary <= value <= upper_boundary:
    print("just right")
elif value < lower_boundary:
    print(f"too {quality_low}")
else:
    print(f"too {quality_high}")
