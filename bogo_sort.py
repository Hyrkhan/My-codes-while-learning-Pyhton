"""
This is bogo sort, the worst sorting algorithm
Sorting time is a matter of luck because it randomize the value everytime it tries to sort
"""

import random
import sys
from load import load_numbers # I created a function that can load the numbers inside a txt file for easier implementation

numbers = load_numbers(sys.argv[1]) # load the txt file on the terminal (python bogo_sort.py -file.txt-)

def is_sorted(values):  # this will check if the list has been sorted or not
    for index in range (len(values) - 1):   # loop through the list, get the length of the list - 1 to get how many loops to do
        if values[index] > values[index + 1]:   # if first value is greater than 2nd value, it means its not sorted yet, return False
            return False
    return True # if the condition is met, it will exit the loop and we can return True

def bogo_sort(values):  
    steps = 0   
    while not is_sorted(values):    # call the is_sorted funtion and check if it is False
        print(steps)
        random.shuffle(values)  # randomize shuffle the values inside the list and hope it gets sorted
        steps += 1
    return values   # if the is_sorted function returns True, the while loop is terminated and now we can return the list

print(bogo_sort(numbers))

