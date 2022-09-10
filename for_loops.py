#start of for loops

#fruits = ['apple', 'orange', 'green']
#for fruit in fruits: #for 'variable' inside the 'array'
    #print(fruit) #print the 'variable' that is looping on the array to print all the content of the array #the variable name doesnt matter
    #for egg in fruit: #example here, the variable name doesnt matter 
        #print(egg)


#numbers = [1,2,3,4,5]
#for nums in numbers:
    #print(nums)

#for number in range(1,51,5): #in range means loop it according to the inputted numbers, (starting number,how many numbers/ending number,steps to count)
    #print(number) #steps to count means if the steps is in 1, it will count/loop by ones.. if 2, it will count/loop by twos...

#prompt the user for 5 grades using for loop and print them also using for loops


#print('Enter 5 grades: ')

#grades = [] #make the empty array first before appending. kinda like a prototype before creating a function
#for grade in range(1,6,1):
    #num = int(input(''))
    #grades.append(num) #append means inserting an object inside the array
#print('')
#for grade in grades:
    #print(grade)

#ask the user for how many grades he has, input the grades and average them, print all the grades and the average of the grades

#number = int(input('How many grades do you have? '))
#grades = []
#sum = 0
#average = 0
#for i in range (0,number,1):
    #grade = int(input('Enter your grade: '))
    #grades.append(grade)
#for j in range (0,number,1):
    #sum = sum + grades[j] # need to define the sum with 0 value first so this can work
#average = sum/number
#print(average)
    

#input the grades/print/average, tell the user what is her highest and lowest grade

number = int(input('How many grades do you have? '))
grades = []
sum = 0
for i in range (0,number,1):
    grade = int(input('Enter your grade: '))
    grades.append(grade)
for j in range (0,number,1):
    sum = sum + grades[j] # need to define the sum with 0 value first so this can work
average = sum/number
print('Your total average is: ',average)

#highest = 0
#lowest = grades [0] #initialize the lowest first, avoid initializing it to 0 
                    #look into the array and compare the first number to the second number to know the highest.
#for k in range(0,number,1):
    #for n in range (0,number,1): #loop it again 2nc time for the comparison
        #if (grades[k] > grades[n] and grades [k] > highest): # add the second condition so that the highest number will remain inside the variable
            #highest = grades[k]
        #elif (grades[k] < grades[n] and grades[k] < lowest): #same shit but opposite
            #lowest = grades[k]
#print('Your highest grade is: ',highest)
#print('Your lowest grade is: ',lowest)

#this is a more simpler way of doing it
#highest = grades[0]
#lowest = grades[0]
#for k in range (0,number,1):
    #if grades [k] > highest:
        #highest = grades[k]
#for n in range (0,number,1):
    #if grades[n] < lowest:
        #lowest = grades[n]
#print('Your highest grade is: ',highest)
#print('Your lowest grade is: ',lowest)

#average grades again, find lowest and highest again, now sort the grades in the highest to lowest and vice versa

highest = grades[0]
lowest = grades[0]
for k in range (0,number,1):
    if grades [k] > highest:
        highest = grades[k]
for n in range (0,number,1):
    if grades[n] < lowest:
        lowest = grades[n]
print('Your highest grade is: ',highest)
print('Your lowest grade is: ',lowest)

#for m in range (0,number,1):
    #for l in range (0,number,1):
        #if grades[m] > grades [l]:
            #temp = grades[m]
            #grades [m] = grades [l]
            #grades [l] = temp
#print('Highest to lowest: ',grades)

#this is the better way
for i in range (0, number-1,1):
    for i in range(0,number-1,1):
        if grades[i] < grades [i+1]:
            temp = grades[i]
            grades[i] = grades[i+1]
            grades[i+1] = temp

print(grades)
