# creating coordinates
# for x in range(3):
#     for y in range(3):
#         print(f'({x} , {y})')

# Question

numbers = [5, 2, 5, 2, 2]
for i in numbers:
    print('X' * i)

# Solve the Above Question By Nested Loop

number1 = [5, 2, 5, 2, 2]
for x_count in numbers:
    out_put = ''
    for count in range(x_count):
        out_put += 'X'
    print(out_put)
