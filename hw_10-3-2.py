# Author: EBP (AMDG) 12/10/20

def three_letter_words(my_list):
    words = 0
    x = 1
    while x < my_list+1:
        if len(x) == 3:
            words += x
            x += 1
        return words


print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)