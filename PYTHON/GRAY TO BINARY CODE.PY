def gray_to_binary(n):
    """Convert Gray codeword to binary and return it."""
    n = int(n, 2) # convert to int
 
    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask
 
    # bin(n) returns n's binary representation with a '0b' prefixed
    # the slice operation is to remove the prefix
    return bin(n)[2:]
 
 
g = input('Enter Gray codeword: ')
b = gray_to_binary(g)
print('In binary:', b)