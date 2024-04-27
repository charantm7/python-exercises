import random

top_of_range = input("Enter the number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter the number greater than 0 next time.")
        quit()

else:
    print("Please enter the number.")
    quit()

random_number = random.randint(0,top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess of a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter the number next time.")
        continue

    if user_guess == random_number:
        print("Yeah you got it :) ")
        break
    else:
        if user_guess > random_number:
            print("The number is above from your guess!")
        else:
            print("The nuber is below from your guess!")
        
print(f"You got in {guesses} guesses")