# Time Complexity - O(n)

#  1. XOR all the array elements, let the result of XOR be `x`.
#  2. XOR all numbers from 1 to n, let XOR be `y`.
#  3. XOR of `x` and `y` gives the missing number.

def get_missing_number(list):
    n = len(list)
    x = list[0] # For xor of all the elements in array
    y = 1 # For xor of all the elements from 1 to n+1
    for i in range(n):
        x ^= list[i]
    for i in range(n+2):
        y ^= i
    return x^y

list = [1, 2, 4, 5, 6]
missing_number = get_missing_number(list)
print(missing_number)
