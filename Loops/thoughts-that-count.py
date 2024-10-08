
red_white = int(input())
white_blue = int(input())
character = input()

x = red_white + white_blue
if character == '<' and white_blue != 4:
    white = (x-(white_blue-1))/2
    white = round(white)
    if red_white > white_blue and white_blue %2 != 0 and (red_white-white_blue)%2 != 0:
        white = (x - (white_blue - 1)) /2
        white = round(white) +1
elif white_blue == 4:
    white = 2
else:
    white = (x - (white_blue + 1)) / 2
    white = round(white)

red = red_white - white
blue = white_blue - white

print(blue)
print(white)
print(red)
