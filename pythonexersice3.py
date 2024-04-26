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
        lines = input("enter the nmber of lines(1-"+ str(MAX_LINES) + ") ")        
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
       currency = input(f"Enter the amount of bet between ${MIN_BET} - ${MAX_BET}? ")
       if currency.isdigit():
            currency = int(currency)
            if MIN_BET <= currency <= MAX_BET:
                break
            else:
                print(f"Please entre the currency between ${MIN_BET} - ${MAX_BET}.")
       else:
            print("please enter a number.")
    return currency


def main():
    balance = deposit()
    lines = get_num_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are beting is {bet} on {lines} lines and your total bet is {total_bet}")
    print(f"Your balance amount in your account is {balance}")
main()
   