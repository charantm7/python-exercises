master_password = input("Please enter your password: ")

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            print(line.rstrip())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('password.txt','a') as f:
        f.write(name + "|" + pwd + "\n")


while True:

    mode = input("Would you like to add a new password or to view the exciting ones (view,add) or press q to quit the mode: ").lower()

    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invald input")
        continue