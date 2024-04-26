MAX_LINES = 5
MAX_BET = 200
MIN_BET = 1

def deposit():
    while True:
        amount = input("what would you like to deposit:$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount mustbe greater than 0")
        else:
            print("please enter a number.")
    return amount


def get_num_of_lines():
    while True:
        lines = input("enter the number of lines(1-"+ str(MAX_LINES) + ") ")        
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines.")
        else:
            print("please enter a number.")
    return lines

def get_bet():
    while True:
       amount = input("What would you bet on each line? ")
       if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please entre the currency between ${MIN_BET} - ${MAX_BET}.")
       else:
            print("please enter a number.")
    return amount


def main():
    balance = deposit()
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have that much of amount to bet in your account and your current balance is ${balance}")
        else:
            break
            
    print(f"You are beting is {bet} on {lines} lines and your total bet is {total_bet}")

main()
   