class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describer_user(self):
        print(f"User profile ")
        print(f"\tFirstname: {self.first_name.title()}")
        print(f"\tLastname: {self.last_name.title()}")

    def greet_user(self):
        print(f"Hi {self.first_name.title()} !")

user = User("danish", "umar")
user2 = User("Dastan", "kastanyo")
user.describer_user()
user.greet_user()
print(f"Welcome {user.first_name.title()} to my Python code")
print()
user2.describer_user()
user2.greet_user()
print(f"Welcome {user2.first_name.title()} to my Python code")
