weight = input('enter your weight: ')
option = input("press K for kilo / press L for pounds: ")
if option == 'L' or option == 'l':
    weight_in_kg = float(weight) * 0.45359237
    print("wight in Kilogram is: ['+ weight_in_kg +']")
elif option == 'K' or option == 'k':
    weight_in_lbs = float(weight) * 2.20462
print(weight_in_lbs)

# Solution another
weight = int(input("Weight: "))
unit = input('(L)lbs and (K) kg: ')
if unit.upper() == 'L':
    converter = weight * 0.45
    print(f'You are {converter} Kilos')
elif unit.upper() == 'K':
    converter = weight // 0.45
    print(f'You are {converter} Pounds')
else:
    print('Incorrect Choice')