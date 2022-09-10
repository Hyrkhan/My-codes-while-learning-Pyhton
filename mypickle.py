#trying to learn pickle to read and save data
#dont name pickle file directly as pickly.py

import pickle #importing means trying to use a library not included to python

fruits = ['orange','kayam','bimbi']
x = 12
y = 2.12
ball = ['baseball', 'basketball','volleyball']
grades = [100,201,24,124,31,231]  
allSet = [fruits,x,y,ball,grades]  #you can initialize all datas into one array for better printing (the array of arrays)

#writing a bunch of data
#wb = means write byte. if you want to write data into a file
#rb  = means read byte, if you want to read the data inside a file

with open('myData.pkl','wb') as f: 
    pickle.dump(fruits,f)  #pickle dump means insert data to the pickle file
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(ball,f)
    pickle.dump(grades,f)
    pickle.dump(1234124,f)  #you can also just write the data here instead of defining it before
    pickle.dump(allSet,f)   #by this time, you wouldnt need to dump all previous data bcause all of it is inside allSet
 
#with open function to open file, (name of file.pkl, what you want to do with the file), asign a variable name
with open('myData.pkl','rb') as f2: 
    a = pickle.load(f2)   #pickle load means load the data inside the pickle file for reading
    b = pickle.load(f2)
    c = pickle.load(f2)
    d = pickle.load(f2)
    e = pickle.load(f2)
    f = pickle.load(f2)
    set = pickle.load(f2) 
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(set)  #you can write the Set as this so that it only shows in 1 line but,

for i in set: 
    print(i) 
#you can also write the Set as this so that it will show all the data inside one by one


#write 2 programs, 1st is gonna ask how many students and what his/her grade,(student name, student grade),
#pickle it, 2nd program will read it and says(pick a student) and it will display that students grade(average)




