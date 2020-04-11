is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day ")
    print('Drink plenty of a Water')
elif is_cold:
    print("It's cold Day")
    print('Wear warm clothes')
else:
    print("It's Lovely Day")

# Question
has_good_credit = True
price = 1000000
if has_good_credit:
    new_price = price - price * (10 / 100)
    print(new_price)
else:
    new_price = price - price * (20 / 100)
    print(new_price)
# Question
has_good_credit = True
has_good_income = True
if has_good_credit and has_good_income:
    print("This user is eligible for loan")
else:
    print("That user is not eligible for loan")

# Question

has_good_credit = False
has_good_income = True
if has_good_credit or has_good_income:
    print("This user is eligible for loan")
else:
    print("That user is not eligible for loan")

# Question
has_criminal_record = False
if not has_criminal_record:
    print("Eligible")
else:
    print("Not Eligible")