#learning classes in python

#A class is like a function that has a funtion(method it is called) inside it, and it can be called by different variables or "objects" to use the method(function) inside it
#the class can be called by different objects and it should not interfere with the output of other objects that used it and will use it

class Rectangle: #intializing the name of the class
    def __init__(self,col,leng,wid): #defining this initialization (__init__) is important, (Self) means getting the name of the object that called this class so that you can modify that objects
                                     #data based on the code inside the method
        self.color = col  #this means = object name . whatever = the parameter that you entered
        self.length = leng
        self.width = wid
    def area(self): #if you want to create a method that can only be accessed by the objects that need it(meaing not all objects that went through this class will always execute this method)
                    #unlike the __init__ method. you can create another method and get the object name (self) and then code the logic and return it
        self.area = self.length * self.width
        return self.area #just like when creating a funtion that has caluclations, return the result
    def per(self):
        self.perimiter = 2 * self.length + 2 * self.width
        return self.perimiter
    def volume(self,h): #you can enter a parameter inside a method that can only be used in this specific method
        self.height = h
        self.vol = self.length * self.width * self.height
        return self.vol

#myRect1 = Rectangle('Blue',5,6) #object name = class name(parameters)
#myRect2 = Rectangle('Red',4,3)
#print(myRect1.color)
#print("Rect1 length is:",myRect1.length)
#print("Rect1 area is", myRect1.area()) #syntax when calling other methods inside the class. need the () because it is a different method. no need to enter the l and w because it already has data on it
#print("Rect1 perimiter is:",myRect1.per())
#print("Rec1 volume is:",myRect1.volume(5))
#print(myRect2.color)
#print("Rect2 length is:",myRect2.length)
#print("Rect2 area is:", myRect2.area())
#print("Rect2 perimiter is:",myRect2.per())

myRect1 = Rectangle('Black',5,10)
print("Color is:",myRect1.color)
print("Length is:",myRect1.length)
print("Width is:",myRect1.width)
print("Area is:",myRect1.area())
print("Perimeter is:",myRect1.per())
print("Volume is:",myRect1.volume(10))