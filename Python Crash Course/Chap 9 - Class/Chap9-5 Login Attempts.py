class User:
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describer_user(self):
        print(f"User profile ")
        print(f"\tFirstname: {self.first_name.title()}")
        print(f"\tLastname: {self.last_name.title()}")

    def greet_user(self):
        print(f"Hi {self.first_name.title()} !")

    def increment_login_attempts(self, num):
        self.login_attempts += num
        return

    def reset_login_attempts(self):
        self.login_attempts = 0
        return

user = User("danish", "umar", 0)
user2 = User("Dastan", "kastanyo", 1)
user.increment_login_attempts(1)
user.increment_login_attempts(2)
user.increment_login_attempts(3)
user.increment_login_attempts(3)
print(f"{user.first_name} has been login {user.login_attempts} times")
# reset
user.reset_login_attempts()
print(f"{user.first_name} has been login {user.login_attempts} times")
"""
user.describer_user()
user.greet_user()
print(f"Welcome {user.first_name.title()} to my Python code")
print()
user2.describer_user()
user2.greet_user()
print(f"Welcome {user2.first_name.title()} to my Python code")
"""