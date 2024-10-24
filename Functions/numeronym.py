import re

def numeronym(word):
    if len(word) < 4:
        return word
    return word[0] + str(len(word) - 2) + word[-1]

def template(word):

    return re.sub(r'\d+', lambda x: '.' * int(x.group()), word)

def isnumeronym(n, w):
    # Convert both input words to lowercase to ignore case distinctions
    n = n.lower()
    w = w.lower()
    
    i = 0  # Index for the word 'w'
    j = 0  # Index for the word 'n'
    
    while i < len(w) and j < len(n):
        if n[j].isdigit():
            # Form the integer from consecutive digits
            num_letters = ""
            while j < len(n) and n[j].isdigit():
                num_letters += n[j]
                j += 1
            num_letters = int(num_letters)
            i += num_letters
        elif n[j] == w[i]:
            j += 1
            i += 1
        else:
            return False
    
    # If both indices reach the end, it's a numeronym
    return i == len(w) and j == len(n)

