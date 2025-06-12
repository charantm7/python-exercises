import random
user_input=input("Enter your choice: rock, paper, scissor:")
computer_input=random.randint(0,2)
if computer_input==0:
    computer_choice='rock'
elif computer_input==1:
    computer_choice='paper'
else:
    computer_choice='scissor'
print("Computer Chose:",computer_choice)
if user_input == 'rock' and computer_choice  == 'paper':
    print("You lose")
elif user_input == 'rock' and computer_choice == 'scissor':
    print("You win")
elif user_input == 'paper' and  computer_choice== 'scissor':
    print("You lose")
elif user_input=='paper' and computer_choice=='rock':
    print("you win")
elif user_input=='scissor' and computer_choice=='rock':
    print("You lose")
elif user_input=='scissor' and computer_choice=='paper':
    print("You win")
elif computer_choice==user_input:
    print("Its draw")
else:
    print("Invalid user Input")