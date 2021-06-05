# this script will seek to have the computer guess a number selected by the user between 1 - 100

# the user will be prompted to anwser 'too high' or 'too low' when the computer guesses wrong
# or 'correct' when the computer guesses correctly

# it will then count how many guesses it took to get the correct number


import random


def user_response(computer_guess):
    """This function is called by the main function to show the guess to the user, it takes the randomized
    number from the computer, and returns the user's input"""
    user_input = input('Is {} your number?'.format(computer_guess))
    user_input = user_input.title()
    return user_input


def high_or_low(lower=1, upper=100):
    """This function takes two inputs from main, the upper or lower bound of a random number based on user input,
    it defaults to a number between 1 and 100, and it returns a random number within the given range"""
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
    while user_anwser != 'Yes' and user_anwser != 'No':
        print('Invalid input please try again! ')
        user_anwser = user_response(computer_choice)

    if user_anwser == 'Yes':
        if num_guesses == 1:
            print('I guessed correctly on my first try! ')
            exit()
        elif num_guesses <= 5:
            print("I guessed correctly, it only took me {} tries!".format(num_guesses))
            exit()
        elif num_guesses <= 10:
            print("I guessed correctly, it took me {} tries!".format(num_guesses))
            exit()
        else:  # more than 10 guesses
            print("I guessed correctly, this was tough! It took me {} guesses".format(num_guesses))
            exit()

    elif user_anwser == 'No':
        too_high_or_too_low = input("Was my guess too high or too low? ")
        too_high_or_too_low = too_high_or_too_low.title()

        while too_high_or_too_low != 'Too High' and too_high_or_too_low != 'Too Low':
            too_high_or_too_low = input('Invalid input please try again! ')
            too_high_or_too_low = too_high_or_too_low.title()

        if too_high_or_too_low == 'Too Low':
            lower_limit = computer_choice + 1
            computer_choice = high_or_low(lower_limit, upper_limit)
            num_guesses += 1
            user_anwser = user_response(computer_choice)

        elif too_high_or_too_low == 'Too High':
            upper_limit = computer_choice - 1
            computer_choice = high_or_low(lower_limit, upper_limit)
            num_guesses += 1
            user_anwser = user_response(computer_choice)
