class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This is {self.restaurant_name}")
        print(f"This a {self.cuisine_type} restaurant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} are open now")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, num_increment):
        self.number_served += num_increment

restaurant = Restaurant('Bakmi GM', 'Noodle')
restaurant2 = Restaurant('Bandar Djakarta', 'Seafood')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# print(f"\n{restaurant.restaurant_name} is a {restaurant.cuisine_type} resto")
print(f"{restaurant2.restaurant_name} has number {restaurant2.number_served} to be served")
# direct update
restaurant2.number_served = 2
print(f"{restaurant2.restaurant_name} has number {restaurant2.number_served} to be served")

# via method update
restaurant2.set_number_served(11)
print(f"{restaurant2.restaurant_name} has number {restaurant2.number_served} to be served")

# via method update increment
restaurant2.increment_number_served(20)
print(f"{restaurant2.restaurant_name} has number {restaurant2.number_served} to be served")


