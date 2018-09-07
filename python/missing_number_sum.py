# Time Complexity - O(n)

def get_missing_number(list):
    n = len(list)
    total = (n+1)*(n+2)/2
    sum_of_list = sum(list)
    return total - sum_of_list

list = [1, 2, 4, 5, 6]
missing_number = get_missing_number(list)
print(missing_number)
