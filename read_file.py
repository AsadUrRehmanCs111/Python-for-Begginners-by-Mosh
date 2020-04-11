# open() function used to open a file.. 1st parameter is the name of the file and the second parameter will be the
# mode of the file.. there are different mode
# r ------ read only
# w ------ write only
# a ------ only append data
# r+ ----- read and write data
employee_file = open("file.txt", "r")
# for checking either file is readable or not we will use readable() function
print(employee_file.readable())

# readline() function is  used for read a line from a file
# print(employee_file.readline())

# now read data from file
# print(employee_file.read())

# readlines() function will read all lines and put them into a list
print(employee_file.readlines())

# for employee in employee_file:
#    print(employee)

employee_file.close()