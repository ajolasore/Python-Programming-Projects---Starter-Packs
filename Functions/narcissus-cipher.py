import string
def jump(letter, n):
    if not isinstance(letter, str) or len(letter) != 1 or not letter.isalpha():
        raise AssertionError(f'invalid letter: {letter}')
    
    is_upper = letter.isupper()
    letter = letter.lower()
    shift = (ord(letter) - ord('a') + n) % 26
    result = chr(ord('a') + shift)
    
    if is_upper:
        result = result.upper()
    
    return result

def reflection(letter, n):
    if not isinstance(letter, str) or len(letter) != 1 or not letter.isalpha():
        raise AssertionError(f'invalid letter: {letter}')
    
    letter = jump(letter, -n)
    return letter + jump(letter, n*2)

def fixation(pair, n):
    if not isinstance(pair, str) or len(pair) != 2 or not pair.isalpha() or not pair.isupper() and not pair.islower():
        raise AssertionError(f'invalid pair: {pair}')
    
    first = jump(pair[0], n)
    second = jump(pair[1], -n)
    char1, char2 = pair[0], pair[1]
    # Check if both characters are in the same case
    if first != second or char1.isupper() != char2.isupper() or char1.islower() != char2.islower():
        raise AssertionError(f'invalid pair: {pair}')
    
    return jump(pair[0], n)

def encode(sentence):
    ciphertext = ""
    wordcount = 1
    wordseparation = string.whitespace + string.punctuation

    for character in sentence:
        if character.isalpha():
            ciphertext += reflection(character, wordcount)
            word = True
        else:
            if word & (character in wordseparation):
                wordcount += 1
                word = False
            ciphertext += character

    return ciphertext

def decode(ciphertext):
    plaintext = ""
    wordcount = 1
    code = ""
    wordseparation = string.whitespace + string.punctuation

    for character in ciphertext:
        if character.isalpha():
            code += character
            word = True
            if len(code) == 2:
                plaintext += fixation(code, wordcount)
                code = ""
        else:
            if word & (character in wordseparation):
                wordcount += 1
                word = False
                code = ""
            plaintext += character

    return plaintext
