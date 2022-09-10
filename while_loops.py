#start of while loops

#j = 1.0
#while (j <=5):
    #print(j)
    #j+=.1
    #j = round(j,1) #to print an exact decimal, u need to round it by .1

#write a program with while to input list of grades, then print the grades using while loop again.

number = int(input('Enter how many grades: '))
i = 0
j = 0
grades = []
while i < number:
    grade = float(input('Enter your grade: '))
    grades.append(grade)
    i +=1
print('Your grades are: ')

while j < number:
    print(grades[j])
    j+=1
