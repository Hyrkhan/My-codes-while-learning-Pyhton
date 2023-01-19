import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1]) # loads the numbers inside a text file

def quicksort(values):
    if len(values) <= 1:    # this is the base case
        return values
    less_than = []  # an empty list to house the values that are less than the pivot value
    greater_than = []  # an empty list to house the values that are greater than the pivot value 
    pivot = values[0]   # the first value inside the entered list will be chosen as the pivot
    for value in values[1:]:    # traverse through the list to find numbers less than or greater than the pivot which is values[0]
        if value <= pivot:  # the current value in the loop is less than the pivot, append it to the less than list
            less_than.append(value)
        else:   # the current value in the loop is greater than the pivot, append it to the greater than list
            greater_than.append(value)
    return quicksort(less_than) + [pivot] + quicksort(greater_than) # recursively do the sorting of the less than first
    # after sorting all the less than values inside the less than list, add it to the pivot value, then recursively sort the greater than list next

    
sorted_numbers = quicksort(numbers)
print(sorted_numbers)