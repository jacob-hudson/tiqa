# Time Complexity - O(n)

#  1.  Get the sum of numbers, eg:  total = n*(n+1)/2
#  2.  Subtract all the numbers from sum and you will get the missing number

def get_missing_number(list):
    n = len(list)
    total = (n+1)*(n+2)/2
    sum_of_list = sum(list)
    return total - sum_of_list

list = [1, 2, 4, 5, 6]
missing_number = get_missing_number(list)
print(missing_number)
