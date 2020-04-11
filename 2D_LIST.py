# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # printing lists in a list
# print(matrix[0])
# print(matrix[1])
# print(matrix[2])
#
#
# # now what if we want to access a middle value in each list of list
# print(matrix[0][1])
# print(matrix[1][1])
# print(matrix[2][1])
#
#
# # now what if we want to update a middle value in each list of list
# matrix[0][1] = 20
# matrix[1][1] = 10
# matrix[2][1] = 30
# # let's see updated value
# print(matrix[0][1])
# print(matrix[1][1])
# print(matrix[2][1])
#
# print('''###############
#      END
# ###############''')
# # what if we want to access each element of the list (definitely we will loop it)
#
# for row in matrix:
#     for column in row:
#         print(column)
#     print("---------------")
#
# print('''###############
#      END
# ###############''')
#
# # list Methods or functions (to perform different operation)
#
list_of_numbers = [2, 5, 6, 7, 3, 4, 5, 9, 0, 1, 2]
#
# # if you want to add a new item in the existing list
# # list_of_numbers.append(100)
#
# print(list_of_numbers)
#
# append add a new item at the end of the list... what if we want to add a new item at the start or somewhere we want to
#  add ........? for that we will use insert() method
#  first pass index then the value
# list_of_numbers.insert(0, 12)
# print(list_of_numbers)
#
# print('-----------------------')
#
#  Remove method
#  to remove an item from list we will use remove() method
#
# list_of_numbers.remove(2)
# print(list_of_numbers)
#
# print('------------------')
#
#  to delete all element in a list clear() method is used
# list_of_numbers.clear()
# print(list_of_numbers)
#
# print('----------------')
#
#  pop() function in list
#
print(list_of_numbers)
# pop last element
# list_of_numbers.pop()
# print(list_of_numbers)
# pop the element on 7th index
list_of_numbers.pop(7)
print(list_of_numbers)

# find the index of the element in the list
get_index = list_of_numbers.index(5)
# that will return the index of first occurrence of that element
print(get_index)

# what if we want to check the existence of an item in list
# for that we will use 'in' operator
# that will return a boolean value
print(20 in list_of_numbers)

# count
# count is used to count an element occurrence in a list
count = list_of_numbers.count(2)
print(count)

# Sort()
# used to sort a list
list_of_numbers.sort()
print(list_of_numbers)

# reverse()
# used to reverse  a list
list_of_numbers.reverse()
print(list_of_numbers)
print("-----------------------")

# copy()
# used to copy one list data
new_list_of_numbers = list_of_numbers.copy()
print(list_of_numbers)
print(new_list_of_numbers)
print('''---------------
----------------
''')
# Question: Remove duplicated value in a list
list_of_numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 5, 4, 3, 2, 4, 5, 7, 8, 0]
list_of_numbers2 = []
print(list_of_numbers1)
for element in list_of_numbers1:
    if element not in list_of_numbers2:
        list_of_numbers2.append(element)
print(list_of_numbers2)
