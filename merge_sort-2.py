import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def merge_sort(values):
    if len(values) <= 1:    # this is the base case
        return values
    middle_index = len(values) // 2 # get the midpoint by using floor division on the length of the list
    left_values = merge_sort(values[:middle_index]) # using slice, sort the left half of the list
    right_values = merge_sort(values[middle_index:])    # using slice, sort the right half of the list
    sorted_values = []  # placeholder list that will house the sorted values
    left_index = 0  # index counter
    right_index = 0
    while left_index < len(left_values) and right_index < len(right_values):    # check the indexes to avoid out of bounds error while looping
        if left_values[left_index] < right_values[right_index]: # check if the value inside the left list is bigger than the value on the right list
            sorted_values.append(left_values[left_index])   # append the value to the placeholder list 
            left_index += 1 # increment index to continue traversing the list
        else:   # if the value on the right list is less than the value on the left list
            sorted_values.append(right_values[right_index]) 
            right_index += 1    # same logic as the left
    sorted_values += left_values[left_index:]   # if theres remaining values inside the list, append it all to the sorted list
    sorted_values += right_values[right_index:]
    return sorted_values    # return the placeholder sorted list that contains the sorted values

sorted_numbers = merge_sort(numbers)
print(sorted_numbers)