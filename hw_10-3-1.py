# Author: EBP (AMDG) 12/10/20

def fname(x, a):
    total = 0
    while a < x + 1:
        if a == x:
            total += 1
    return total


print(fname("cat", "t") == 1)
print(fname("apple", "p") == 2)
print(fname("supercalifragilisticexpialidocious", "i") == 7)