import pickle #after initialization, you can now access the data inside the pickle file

with open ('myData2.pkl','rb') as f:
    setA = pickle.load(f)
    setB = pickle.load(f)
    numbers = pickle.load(f)

print('')
print ('Here are the list of students',setA)

while (1==1):
    qer = input('Which student are you interested in? ')
    for j in range(0,numbers,1):
        if qer == setA[j]:
            print(setA[j]+"'s grade is",setB[j])
        
    




    
