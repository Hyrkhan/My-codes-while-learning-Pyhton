new_list = [1 , 2, 3]
result = new_list[0]

if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)

        break

numbers = []
numbers.append(1) # appends the item at the end of the array
numbers.extend([1,2,3]) # adds an array to an existing array list
numbers.extend(new_list) # it can also work like this