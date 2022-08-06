class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This is {self.restaurant_name}")
        print(f"This a {self.cuisine_type} restaurant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} are open now")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavor(self):
        for flavor in self.flavors:
            print(flavor)


restaurant = Restaurant('Bakmi GM', 'Noodle')
restaurant2 = IceCreamStand('Campina')
restaurant2.flavors = ['Choco', 'Banana', 'Apple']
print(f"Welcome to {restaurant2.restaurant_name},  we have ice cream flavor : ")
restaurant2.display_flavor()

"""
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"\n{restaurant.restaurant_name} is a {restaurant.cuisine_type} resto")
"""