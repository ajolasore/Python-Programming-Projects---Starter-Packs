def forward_sequence(word_sequence):
    words = word_sequence.split(", ")
    forward = ''.join(word.lower() for word in words)
    return forward

def backward_sequence(word_sequence):
    forward = forward_sequence(word_sequence)
    backward = forward[::-1]
    return backward

def common_sequence(word_sequence):
    forward = forward_sequence(word_sequence)
    backward = backward_sequence(word_sequence)
    
    for i in range(len(forward)):
        test1, test2 = forward[i:], backward[:len(forward) - i]
        if test1 == test2:
            return test1
    return None
    
def missing_word(word_sequence):
    common = common_sequence(word_sequence)
    missing = backward_sequence(word_sequence)[len(common):]
    return missing.capitalize()