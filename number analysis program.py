input_string = input("Enter numbers separated by a space ")
list  = input_string.split()

print('\n Determing lowest number')
list.sort()
print("Lowest number = ",*list[:1])

print('\n Determining highest number')
list.sort()
print('Highest number = ',list[-1])

print('\n Calculating sum of numbers')
sum = 0
print("Sum = ",sum)
