list_of_names = ['ASAD', 'ALI', 'HASEEB', 'USAMA']
print(list_of_names)
# getting indexing of lists

# getting indexes from 1st to last
print(list_of_names[0])
print(list_of_names[1])
print(list_of_names[2])
print(list_of_names[3])

# getting indexing from last to 1st
print(list_of_names[-1])
print(list_of_names[-2])
print(list_of_names[-3])
print(list_of_names[-4])

# getting range of items in a list
print(list_of_names[:])
print(list_of_names[1:])
print(list_of_names[-1:])
print(list_of_names[1:-1])

# updating any index Value
list_of_names[0] = "ALI"
list_of_names[1] = "ASAD"
print(list_of_names)

# Find A Largest number in a List

list_of_numbers = [2, 5, 6, 8, 9, 1, 4, 3, 2, 7, 11]

# By using Build in function
# max_number = max(list_of_numbers)
# print(max_number)

# Doing the same problem without built_in function
max_number = list_of_numbers[0]
for number in list_of_numbers:
    if number > max_number:
        max_number = number
print(max_number)

