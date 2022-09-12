#create a class called students with first name , last name, with method that input grades, methods that print the grades, method that average grades, method that finds high and low grades.
#i need to make an array that can be accessed by an object and not other objects, but still can be used by other methods inside the class

class Students:
    def __init__(self,ln,fn):
        self.lastname = ln
        self.firstname = fn
        grades = []
        self.array = grades
    def inputGrades(self):
        number = int(input('How many grades? '))
        self.numbers = number
        for i in range (0,self.numbers,1):
            grade = float(input('Enter a grade: '))
            self.array.append(grade)
    def printGrades(self):
        print(self.lastname, self.firstname + "'s grades are: ")
        for i in range(0,self.numbers,1):
            print(self.array[i])
        print('')           #you can skip returning values if you just call the method directly
    def averageGrades(self):
        sum = 0
        for i in range(0,self.numbers,1):
            sum = sum + self.array[i]
        average = sum / self.numbers
        return average
    def findHigh(self):
        highest = self.array[0]
        for i in range(0,self.numbers,1):
            if(self.array[i] > highest):
                highest = self.array[i]
        return highest
    def findLow(self):
        lowest = self.array[0]
        for i in range(0,self.numbers,1):
            if(self.array[i] < lowest):
                lowest = self.array[i]
        return lowest

    
        

student1 = Students("Torres","Juan Miguel")
print(student1.lastname,student1.firstname)
student1.inputGrades()
print(student1.array)
student1.printGrades() #you can just call the method instead of printing it.
print('Your average is:',student1.averageGrades())
print('Your highest is:',student1.findHigh())
print('Your lowest is:',student1.findLow())

print('')
print('*************************************************')
print('')

student2 = Students("Akira","Midas")
print(student2.lastname,student2.firstname)
student2.inputGrades()
print(student2.array) 
student2.printGrades()
print('Your average is:',student2.averageGrades())
print('Your highest is:',student2.findHigh())
print('Your lowest is:',student2.findLow())