class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This is {self.restaurant_name}")
        print(f"This a {self.cuisine_type} restaurant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} are open now")

restaurant = Restaurant('Bakmi GM', 'Noodle')
restaurant2 = Restaurant('Bandar Djakart', 'Seafood')
restaurant3 = Restaurant('Bebek Bentu', 'Duck')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"{restaurant.restaurant_name} is a {restaurant.cuisine_type} resto")
print()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
print(f"{restaurant2.restaurant_name} is a {restaurant2.cuisine_type} resto")
print()
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
print(f"{restaurant3.restaurant_name} is a {restaurant3.cuisine_type} resto")
