#write a functions for each of the logics that we did before, inputing grades in an array,printing,averaging,
#finding highest/lowest


def appending(num,array):
    array = []
    for i in range (0,num,1):
        grade = float(input('Enter a grade: '))
        array.append(grade)
    return array

def averaging(num,array):
    sum = 0
    for i in range (0,num,1):
        sum = sum + array[i]
    return sum

def sortinghigh(num,array):
    highest = 0
    for i in range(0,num,1):
        if highest < array[i]:
            highest = array[i]
    return highest

def sortinglow(num,array):
    lowest = array[1]
    for i in range(0,num,1):
        if lowest > array[i]:
            lowest = array[i]
    return lowest

number = int(input('Enter how many grades: '))
grades = []
grades = appending(number,grades)
print('Your grades are:',grades)

total = averaging(number,grades)
print('The sum of all grades are:',total)

highest = sortinghigh(number,grades)
print('Your highest grade is:',highest)

lowest = sortinglow(number,grades)
print('Your lowest grade is:',lowest)
