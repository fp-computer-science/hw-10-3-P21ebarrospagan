# Author: EBP (AMDG) 12/10/20

def sum_odds(my_list):
    numbers = 0
    x = 0
    while x < my_list:
        if x % 2 > 0:
            numbers += x
    return numbers

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)