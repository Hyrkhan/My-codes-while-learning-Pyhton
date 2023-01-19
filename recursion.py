def sum(numbers):
    """
    Recursion sort calls itself until it reaches a base case "return 0" otherwise it loops indefinetely
    """
    if not numbers: #base case if numbers is empty return 0
        return 0
    remaining_sum = sum(numbers[1:]) # creating a variable remaining_sum by calling the function again and slicing the list from 1st element
    return numbers[0] + remaining_sum # returning the sum of first element of the input list and remaining_sum

print(sum([1,2,7,9]))

"""
This is how this works

Calling sum([2, 7, 9])
Calling sum([7, 9])
Calling sum([9])
Calling sum([])
---the list gets called repeatedly until the base case is reached, then only it will reach the rest of the code---
Call to sum([9]) returning 9 + 0
Call to sum([7, 9]) returning 7 + 9
Call to sum([2, 7, 9]) returning 2 + 16
Call to sum([1, 2, 7, 9]) returning 1 + 18
19
"""