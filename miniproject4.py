from cryptography.fernet import Fernet

master_password = input("Please enter your password: ")

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User: "+user+"|"+"password: "+passw)

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