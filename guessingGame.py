print("""Welcome to Guess World....
            You Have Only Three Chance to Guess the Secret Number (1-10)""")
secretNumber = 9
i = 0
while i < 3:
    inputNumber = int(input('Guess: '))
    if inputNumber == secretNumber:
        print("You Win!")
        break
    i = i + 1
else:
    print("You Lost")
