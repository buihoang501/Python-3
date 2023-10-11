try:
    f = open('text.txt', mode='r')
except:
    print('Something went wrong!')
finally:
    print('Always print this!')


def ask_for_int():
    while True:
        try:
            number = int(input('Please enter a number: '))
        except:
            print('You type an invalid number! Try again')
            continue
        else:

            print("Awesome! This is a integer number: {} ".format(number))
            break


ask_for_int()
