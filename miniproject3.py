name = input("Enter your name: ")
print(f"welcome {name} to the adventure game!")

answer = input("You are on a dirt road! And you can go left or right, type left to go left and type right to go right! ").lower()

if answer == "left":
    answer = input("You are on a left road! And you came near the river! Your gonna swim or walk accorss the river, type swim to swim in the river and type walk towalk accross the river! ").lower()

    if answer == "swim":
        print("you swam into the river and eaten the aligator and you lose the game!")
        
    elif answer == "walk":
        print("You have walken accross the river as much as possible and you gone out of the river, you lose the game!")
       
    else:
        print("Ypu are on the invalid input!") 
elif answer == "right":

    answer = input("Yeah you came near the bridge and ypu wanna cross the bridge or go back to the left road!(cross/back): ").lower()

    if answer == "cross":
        answer = input("You have cross the bridge! and you are gonna meet the stranger type yes to meet him and no to not to meet him(yes/no): ").lower()
        if answer == "yes":
            print("yeah met the stranger and he gave you a gold and you wonn the game!")

        elif answer == "no":
            print("You aint met the stranger and he affended you and you lose the game!")

        else:
            print("You are on the invalid input!!")

    elif answer == "back":
        answer = input("you move away from the bridge and back to left road! and do you wanna start from the first? (yes/no): ")

        if answer == "yes":

            answer = input("You are on a left road! And you came near the river! Your gonna swim or walk accorss the river, type swim to swim in the river and type walk towalk accross the river! ").lower()

            if answer == "swim":
                print("you swam into the river and eaten the aligator and you lose the game!")
        
            elif answer == "walk":
                print("You have walken accross the river as much as possible and you gone out of the river, you lose the game!")
       
            else:
                print("Ypu are on the invalid input!")
        else:
            print("Ypu are anymore playing this game!J")
    else:
        print("You are on the invalid input!")
else:
    print("Yor are on the invalid input!")