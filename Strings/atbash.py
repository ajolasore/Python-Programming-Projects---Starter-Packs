sentence =  input('Enter the sentence to be decoded or encoded: ')

uppercase = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "ZYXWVUTSRQPONMLKJIHGFEDCBA"
)
lowercase = str.maketrans(
    "abcdefghijklmnopqrstuvwxyz",
    "zyxwvutsrqponmlkjihgfedcba"
)

# Initialize the result string.
result = ""

# Iterate through each character in the input text.
for char in sentence:
    if char.isupper():
        # If the character is uppercase, use the uppercase mapping.
        result += char.translate(uppercase)
    elif char.islower():
        # If the character is lowercase, use the lowercase mapping.
        result += char.translate(lowercase)
    else:
        # If the character is not a letter, keep it unchanged.
        result += char
print(result)