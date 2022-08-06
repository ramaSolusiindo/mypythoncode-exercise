class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describer_user(self):
        print(f"User profile ")
        print(f"\tFirstname: {self.first_name.title()}")
        print(f"\tLastname: {self.last_name.title()}")

    def greet_user(self):
        print(f"Hi {self.first_name.title()} !")


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print("- " + privilege)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


ainun = Admin("ainun", "gesit")
ainun.describer_user()
ainun_privileges = [
    "can add post",
    "can delete post",
    "can ban user",
]
ainun.privileges.privileges = ainun_privileges
print(f"Hi {ainun.first_name.title()}, you have priviledges :")
ainun.privileges.show_privileges()


