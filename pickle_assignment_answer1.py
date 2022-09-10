import pickle  #initialize the datas first and store it to the pickle file

number = int(input('Enter how many numbs: '))
students = []
grades = []
for i in range(0,number,1):
    student = input("Enter student's name: ")
    students.append(student)
    grade = float(input('Enter '+student+ "'s grade: "))
    grades.append(grade)

with open('myData2.pkl','wb') as f:
    pickle.dump(students,f)
    pickle.dump(grades,f)
    pickle.dump(number,f)
