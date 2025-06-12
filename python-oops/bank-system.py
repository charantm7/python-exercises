class Bank:
    def __init__(self, account, balance = 0.0):
        self.__account = account
        self.__balance = balance

    def check(self):
        print(f"{self.__balance} balance amount!")
    
    def deposit(self, amount):
        if amount < 0:
            print("Amount must be positive.")
        else:
            self.__balance += amount
            print(f"The Amount {amount} has been deposited to A/C {self.__account}")

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            print(f"The Amount {amount} has been withdrawn from the A/C {self.__account}")
        else:
            print("Insuffuicent Balance")


bank = Bank(12345678, 1000)
bank.check()
bank.withdraw(250)
bank.check()