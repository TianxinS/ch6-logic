# This script contains a program for a simple guessing game!

# Define a function `print_hot_or_cold()` that takes in two arguments (the 
# `target` and the `guess`), and prints out an appropriate message based on 
# how close the guess is to the target:
#
# Distance    Message
# -------------------
# The same    "got it!"
# Within 1	  "scalding hot"
# Within 3	  "very warm"
# Within 5	  "warm"
# Within 8	  "cold"
# Within 13	  "very cold"
# > 13 away	  "icy freezing miserably cold"
#
# Be sure to consider both positive AND negative distances!
# BONUS: Also print out whether the guess is high or low

def print_hot_or_cold(target, guess):
    difference = abs(target - guess)
    if difference == 0: 
        print("got it!")
    elif difference <= 1 and difference > 0:
        print("scalding hot")
    elif difference <= 3:
        print("very warm")
    elif difference <= 5:
        print("warm")
    elif difference <= 8:
        print("cold")
    elif difference <= 13:
        print("very cold")
    else: #difference > 13:
        print("icy freezing miserably cold")
   



#print_hot_or_cold(10, 8)
#print_hot_or_cold(10, 9)
#print_hot_or_cold(10, 10)



# Define a function `guess_number()` that takes a single argument (a target number)
# and prompts the user for a guess using the `input()` method. Your function should
# then print how close the user's guess is to that target (use your previous 
# function!). Note that you will need to convert the input into a number.
#
# Once you have a single guess working, modify your function so that the user can
# make MULTIPLE guesses. You can either do this using a loop (see the next chapter)
# or by simply calling your `guess_number() method again IF the user didn't get
# the answer right. The later is an example of **recursion**.

def guess_number(target_number):
    response = int(input("Guess a number:"))
    print_hot_or_cold(target_number, response)

#if the answer is not correct, 
    if response != target_number:
        #ask again
        guess_number(target_number)


#guess_number(10)

# If the file is run as a top-level script, your script should pick a random number
# between 1 and 50 as the target and then start the game. You should inform the
# user of the range of numbers before asking them for a guess.

if __name__ == "__main__":
    import random
    random_number = random.randint(1,50)
    print("Guess the number between 1 and 50")
    guess_number(random_number)

