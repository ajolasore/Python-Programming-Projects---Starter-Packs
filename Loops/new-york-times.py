# Read the increment
increment = int(input())

# Initialize variables to keep track of the previous and current numbers
previous = None

# Read the first line of input
line = input()

# Continue processing until 'NYT' is encountered
while line != 'NYT':
    current = int(line)

    # Check if the current number follows the expected increment
    if previous is not None and current != previous + increment:
        difference = current - previous
        print(f"{previous} -> {current} ({'+' if difference >= 0 else ''}{difference})")

    previous = current

    # Read the next line of input
    line = input()

