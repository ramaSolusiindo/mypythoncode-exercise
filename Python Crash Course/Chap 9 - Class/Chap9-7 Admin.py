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


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.priviledges = []

    def show_privileges(self):
        for privilege in self.priviledges:
            print("- " + privilege)

ainun = Admin("ainun", "gesit")
ainun.priviledges = [
    "can add post",
    "can delete post",
    "can ban user",
                        ]
print(f"Hi {ainun.first_name.title()}, you have priviledges :")
ainun.show_privileges()


user = User("danish", "umar")
user2 = User("Dastan", "kastanyo")
