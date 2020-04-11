# let we have a list or tuple
list_of_numbers = [1, 2, 3]

# if we want to use it's indexes in a problem we will use like
result = list_of_numbers[0] + list_of_numbers[1] + list_of_numbers[2]
# that looks not good
# we will store them n a variable like that
# x = list_of_numbers[0]
# y = list_of_numbers[1]
# z = list_of_numbers[2]

# writing these lines of code python has an unpacking feature
x, y, z = list_of_numbers
print(x)
print(y)
print(z)

# that same thing is for tuple
