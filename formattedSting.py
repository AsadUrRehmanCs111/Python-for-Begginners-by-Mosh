# string formatting
first_name = "Asad Ur Rehman "
# message = '[' + first_name + last_name +'] is a coder'
last_name = "Mr.Asad"
msg = f'{first_name}[ {last_name} ] is a coder' # f'' is used for formatting
# print(message)
print(msg)

# --------String methods---------#

course = 'python IS for Everyone'
print(len(course))
print(course.capitalize())
print(course.casefold())
print(course.center(3))
print(course.count('o'))
print(course.find('IS'))
print(course.lower())
print(course.upper())
print(course.replace('IS','IS NOT'))

