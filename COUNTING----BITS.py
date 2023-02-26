#COUNTING BITS

def countBits(num):
    counter = [0]
    if num >= 1:
        while len(counter) <= num:
            counter = counter + [i + 1 for i in counter]
        return counter[;num+1]
    else:
        return 0
print(countBits(5))
