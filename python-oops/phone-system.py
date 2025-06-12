class Phone:

    def __init__(self, owner):
        print(f"Hello {owner} welcome back (:")
        self.owner = owner
        self.data = {}

    def show(self):
        print("\nAll contacts")
        for key, value in self.data.items():
            print(f"{key} -> {value}")

    def add_contact(self, name, number):
        self.data[name] = number
        print(f"{name} -> {number} added succesfully!")

    def call(self, name):
        if name in self.data:
            print(f"Calling {name} at {self.data[name]}...")
        else:
            print(f"No contact saved as {name}.")


    def picture(self):
        print("Taking picture")


p = Phone("Charan T M")
p.add_contact("shamanth", 9538336112)
p.show()
p.call("shamanth")

