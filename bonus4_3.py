from random import randint
# 1. print welcome msg
print "Welcome to the guessing game!"
# 2. ask for max number
max_number = int(raw_input('What should the maximum number be? '))
print "Okay, I've thought of a number between 1 and %d!" % max_number

# 3. think of a random number


computer_number = randint(1, max_number)
num_guesses = 0
user_guess = int(raw_input('What is yr guess? '))
num_guesses += 1

while user_guess != computer_number:
    # 4. keep asking the user for a guess till they get it right
    if user_guess < computer_number:
        print 'Nope! My number is higher. Try again.'
    elif user_guess > computer_number:
        print 'Nope! My number is lower. Try again.'

    num_guesses += 1
    user_guess = int(raw_input('What is yr nxt guess? '))

print "You got it!\nYou took %d guesses to find my number." % (num_guesses)
