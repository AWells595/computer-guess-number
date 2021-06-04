# this script will seek to have the computer guess a number selected by the user between 1 - 100

# the user will be prompted to anwser 'too high' or 'too low' when the computer guesses wrong
# or 'correct' when the computer guesses correctly

# it will then count how many guesses it took to get the correct number

import random

def user_response(computer_guess):
    user_input = input('Is {} your number?'.format(computer_guess))
    user_input = user_input.title()
    return user_input


def too_high(lower=1, upper=100):
    computer_guess = random.randint(lower, upper)
    return computer_guess


def too_low(lower=1, upper=100):
    computer_guess = random.randint(lower, upper)
    return computer_guess


play_game = True
num_guesses = 1  # starts at 1 so if first guess is correct it displays correctly
lower_limit = 0
upper_limit = 100
computer_choice = random.randint(lower_limit, upper_limit)

print('Welcome! Please think of a number between 1 and 100 and I will try to guess what it is! ')
user_anwser = user_response(computer_choice)

while play_game is True:
    if user_anwser == 'Yes':
        print("I guessed correctly, it only took me {} tries!".format(num_guesses))
        exit()
    elif user_anwser == 'No':
        too_high_or_too_low = input("Was my guess too high or too low? ")
        if too_high_or_too_low == 'too low':
            lower_limit = computer_choice + 1
            computer_choice = too_low(lower_limit, upper_limit)
            num_guesses += 1
            user_anwser = user_response(computer_choice)
            continue
        elif too_high_or_too_low == 'too high':
            upper_limit = computer_choice - 1
            computer_choice = too_high(lower_limit, upper_limit)
            num_guesses += 1
            user_anwser = user_response(computer_choice)
            continue

    else:
        while user_anwser != 'yes' and user_anwser != 'no':
            print('Invalid input please try again! ')
            user_anwser = user_response(computer_choice)


