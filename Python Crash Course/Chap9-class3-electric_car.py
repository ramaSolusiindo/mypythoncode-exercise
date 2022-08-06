class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer !")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        # self.battery_size = 75

    # def describe_battery(self):
    #    print(f"This car has a {self.battery_size}-kWh battery. ")

    def fill_gas_tank(self):
        # Electric cars don't have gas tank
        print("This car doesn't need a gas tank !")


my_tesla = ElectricCar('tesla', 'model s', 2022)
print(my_tesla.get_descriptive_name())
# This command below need update
# my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()

"""
my_new_car = Car('Audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# direct update
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# via method update
my_new_car.update_odometer(50)
my_new_car.read_odometer()
# set condition cannot roll back
my_new_car.update_odometer(41)

my_new_car.update_odometer(23_500)
my_new_car.read_odometer()
# incrementing an attribute valuse through method
my_new_car.increment_odometer(100)
my_new_car.read_odometer() 
"""
