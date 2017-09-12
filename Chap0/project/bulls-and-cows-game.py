# IDEA: This verion for the fundamental task, then try advanced task.

import random

right_answer = random.randint(0,20)

print("Hello, welcome, Bulls and Cows.")
print("Please input a number between 0 and 20\n")

attempt_times = 1

while attempt_times <= 10:

    user_input = input("Please input your number!\n")

# REVIEW:  This if condition need to refactor
    if user_input.isdigit() and int(user_input) <= 20 :
        user_answer = int(user_input)
        print("You have %d remaining attempts." % (10 - attempt_times))

        attempt_times += 1
        if attempt_times <= 10:
            if user_answer > right_answer:
                print("You number is greater than the answer.\n")
            elif user_answer < right_answer:
                print("You number is lesser than the answer.\n")
            else:
                print("Congratulations, you win!")
                exit(0)
        else:
            print("What a pity, you do not guess the number, come on, babay, re-challenge the game.")

    else:
        print("Sorry, please input a number and between 0 and 20.\n")
