    
     #ask the user to input a number and tell if your number is an even positive number, odd pos number, even negative number, 
     # odd negative number, if person enter 0 you just say your number is zero
     
num2 = float(input('Enter a number: '))

if (num2 == 0):
    print('Your number is 0')
elif(num2 > 0 and num2 % 2 == 0):
    print('Your number is an even positive number')
elif(num2 > 0 and num2 % 2 > 0):
    print('Your number is an odd positive number')
elif(num2 < 0 and num2 % 2 == 0):
    print('Your number is an even negative number')
elif(num2 < 0 and num2 % 2 > 0):
    print('Your number is an odd negative number')
else:
    print('None')
