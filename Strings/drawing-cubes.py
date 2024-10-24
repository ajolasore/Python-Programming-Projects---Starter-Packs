# Read input dimensions
width = int(input())
height = int(input())
depth = int(input())

# Define characters for different faces
front_face = '#'
side_face = '+'
top_face = ':'
corner = '/'

# Draw the bottom face (all colons)
for _ in range(depth):
    space = depth - _
    for _ in range(space):
        print(" ", end='')
    for _ in range(width-1):
        print(top_face, end='')
    print(corner, end = '')
    if (depth - space) >= height: # Print side_face in increasing order
        print(side_face*(height-1), end='')
    else:
        for _ in range(depth - space):
            print(side_face , end = '')
    print()

#Create the cuboid
for i in range(height):
    for j in range(width):
        if j < width:
            print(front_face, end='')

    if height - i > depth:
        print(side_face * depth, end='')
    elif height - i <= depth:
        print(side_face * (height - i -1), end ='')# Check if height remains the number of depth
    print()
