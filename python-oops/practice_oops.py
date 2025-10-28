# classes are the blueprints or like constructors that is build based on objects
# attributes = the variables that holds the data of the object in the class
# Parameters = the names which is given the function or classes that accepts the arguments
# Argument = the actual values to be passed to the parameters to the func or class.

class MyCourse():
    x = "hi"


# __init__ constructor of the class it is first executed when the class been initiated

class MyCar():

    # constructor runs automatically when object is created
    # self refers to the current instance of th class and used to access the variables that is belonged to the class. It points to the particular objects and it is the first parameter to the class, we can call it in any name not only with the self.

    def __init__(self, name, amount):
        self.amount = amount
        self.name = name

    # it is used to return the string automatically when the object is created their is no needed to call a method in the class to display the objects result.
    def __str__(self):
        return f"My car is {self.name} and i have paid it {self.amount}"

    def display(self):
        return self.name


if __name__ == "__main__":

    # create an object and print it by accessing it.
    # car = MyCar("ferari", 70)
    # print("before deletion", car)

    # car.name = "bmw"
    # print("modified object", car)

    while True:
        r = input("Enter a string: ")
        print("yes" if r == r[::-1] else "no")

    # print(car.display())
