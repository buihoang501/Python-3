from random import shuffle
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers_shuffle = shuffle(numbers)
print(numbers_shuffle)
print(numbers)

init_list = ['', 'W', '']


def shuffle_list(list):
    return shuffle(list)


shuffle_list(init_list)


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Enter a number 0 / 1 / 2 ')
    return int(guess)


my_index = player_guess()


def check_guess(init_list, guess):
    if (init_list[guess] == 'W'):
        print('Win the game')
    else:
        print('Wrong')
        print(init_list)


check_guess(init_list, my_index)
