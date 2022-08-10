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

    def get_range(self):
        if self.battery_size == 75:
            range = 200
        elif self.battery_size == 100:
            range = 315
        else:
            range = 100
        print(f"This car can go about {range} miles on full charge.")

    def upgrade_battery(self):
        if self.battery_size <= 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh")
        else:
            print("The battery is already upgraded")


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
my_tesla.battery.battery_size = 50
print(my_tesla.get_descriptive_name())
# This command below need update
# my_tesla.describe_battery()
# my_tesla.battery.describe_battery()
print("Upgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

