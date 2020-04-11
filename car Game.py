started = False
while True:
    command = input("> ").upper()
    if command == 'START':
        if not started:
            print('The Car Has Been Started')
            started = True
        else:
            print('Car is already Started')
    elif command == 'STOP':
        if started:
            print('The Car Has Been Stopped')
            started = False
        else:
            print("car is Already stopped")
    elif command == 'HELP':
        print("""
Start --- To Start the Car
Stop --- To Stop the Car
Quit --- to Exit The Program """)
    elif command == 'QUIT':
        exit()
    else:
        print("I don't Understand it")
