# comparison operator
tempereture = 9
if tempereture > 30:
    print("it's hot day")
elif tempereture < 10:
    print("it's cold day")
else:
    print("it's neither cold nor hot day...mean it's Lovely and Awesome day")

# Question
name = input("Enter you Name: ")
if len(name) < 3:
    print("Name should be Greater than 3 character")
elif len(name) > 50:
    print("Name should be less than 50 characters")
else:
    print("Name looks Good!!!!!!!!!!")