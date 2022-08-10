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
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"\n{restaurant.restaurant_name} is a {restaurant.cuisine_type} resto")
