# dictionaries are like key value pairs.. duplicate key is not allowed..But the value can be any thing.. a number,
# a string, boolean value , a list or tuple in simple words anything.

customer = {
    'name': "Asad Ur Rehman",
    'Age': 22,
    'is_student': True
}
# we can access value by it's key
print(customer['name'])
print(customer['Age'])
# By writing customer['name'] that will return value associated to that key

# what if a key does not exist we will get error.. but if we use the get()
# function it will return none instead of error which mean no such key exit..
print(customer.get('Age'))
# the advantage of using get method is we can print some default value or some error message
print(customer.get('RegNumber', 'No such a data exit'))
customer['birthday'] = '10 january,1998'
print(customer['birthday'])
print(customer)

# Question user write number your program write it in English

phone_number = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
}
user_input = input("Enter phone Number: ")
out_put = ""
for ch in user_input:
    out_put += phone_number.get(ch, "!") + " "
print(out_put)