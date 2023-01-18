import sys
from load import load_numbers   # I created a function that can load the numbers inside a txt file for easier implementation

numbers = load_numbers(sys.argv[1]) # load the txt file on the terminal (python selection_sort.py -file.txt-)

def selection_sort(values): # this is the main selection sort function
    sorted_list = []    # create an empty list that will house the minimum value of every loop, creating the sorted list
    for i in range( 0, len(values)):    # loop through the unsorted list
        indextomove = indexofmin(values)    # get the index of the minimum number caught by the indexofmin function
        sorted_list.append(values.pop(indextomove)) # remove the minimum value on the list using .pop, then append it to the sorted_list using the append function
    return sorted_list  # return the sorted list

def indexofmin(values): # this function will get the index of the minimum value inside the list
    minindex = 0    # variable to store the index
    for i in range (1, len(values)):    # loop through the list
        if values[i] < values[minindex]:    # if the current value is less than the past minimum value
            minindex = i    # set the index of the current value as the minindex
    return minindex 

print(selection_sort(numbers))