#Assignment 1
class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.__battery_level = battery_level  # Private attribute (encapsulation)

    def charge(self, amount):
        """Charge the phone by a given percentage."""
        self.__battery_level = min(100, self.__battery_level + amount)
        print(f"{self.model} charged to {self.__battery_level}%.")

    def get_battery_level(self):
        """Getter for battery level (encapsulation)."""
        return self.__battery_level

    def call(self, contact):
        """Simulate making a call."""
        if self.__battery_level > 5:
            self.__battery_level -= 5
            print(f"Calling {contact} from {self.model}...")
        else:
            print("Battery too low to make a call!")

# Child Class (Inheritance)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_level, heart_rate=70):
        super().__init__(brand, model, battery_level)
        self.heart_rate = heart_rate

    # Polymorphism: overriding the call() method
    def call(self, contact):
        if self.get_battery_level() > 10:
            print(f"Voice calling {contact} via smartwatch {self.model}...")
        else:
            print("Not enough battery for a call on smartwatch.")

    def track_heart_rate(self):
        print(f"Current heart rate: {self.heart_rate} bpm")

# Create objects
phone = Smartphone("Samsung", "Galaxy S25", 50)
watch = Smartwatch("Apple", "Watch X", 30)

# Use methods
phone.call("Alice")
phone.charge(20)
print(f"Battery level: {phone.get_battery_level()}%")

watch.call("Bob")
watch.track_heart_rate()


#Assignment 2
# Base Class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Derived Classes
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water ⛵")

class Bike(Vehicle):
    def move(self):
        print("Pedaling through the path 🚴")

# Using polymorphism
vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    v.move()
