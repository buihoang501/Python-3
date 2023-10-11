def user_choice():
    choice = 'Wrong'
    accept_range = range(0, 10)
    in_range = False

    while choice.isdigit() == False or in_range == False:
        choice = input('Please enter a number in range (0-10): ')
        if choice.isdigit() == False:
            print('Choice is not a digit!')
        else:
            if int(choice) in accept_range:
                in_range = True
            else:
                print('You should enter a number in range (0-10)')
                in_range = False
    return int(choice)


result = user_choice()
print(result)
