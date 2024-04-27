print("Welcome to my computer quiz game!")

playing = input("Do you want to play the game? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play the game!")

score = 0

answer = input("What does cpu stands for? ").lower()
if answer == "central processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = input("What does Gpu stands for? ").lower()
if answer == "graphic processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = input("How many keys are there in keyboard in your computer? ").lower()
if answer == "104":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = input("what does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = input("What does psu stands for? ").lower()
if answer == "power supply unit":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = input("which part is the brain of the computer? ").lower()
if answer == "cpu":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = input("which is national bird of india? ").lower()
if answer == "peacock":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = input("which is the national animal of india? ").lower()
if answer == "tiger":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = input("which is the national game of india? ").lower()
if answer == "hockey":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

answer = input("which is the easiest language in coding? ").lower()
if answer == "python":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect answer!")

print(f"Your Total Score is {str(score)} out of 10 questions")
print(f"Your Total percentage is {str(((score / 10) * 100))}%")