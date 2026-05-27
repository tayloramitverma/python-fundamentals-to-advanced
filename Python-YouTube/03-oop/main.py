## Class method and self
## Inheritance
## Encapsulation
## polymorphism
## Class Variable
## Static method
## Peroperty Decorator
## class inheritance && isinstance() function
## multiple inheritance


class Car():
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand
    
    def full_name(self):
        return f"{self.__brand}, {self.__model}"
    
    def fule_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transportation"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fule_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "876KWH")
# print(my_tesla.__brand) ## Private varibale can't be accessible 
print(my_tesla.get_brand())
print(my_tesla.full_name())
print(my_tesla.fule_type())

## Parent Class
my_car = Car("Tata", "Safari")

# print(my_car.brand)
print(my_car.model)
print(my_car.full_name())
print(my_car.fule_type())
print(Car.total_car)
print(Car.general_description())

##isinstance example

print(isinstance(my_tesla, ElectricCar))
print(isinstance(my_tesla, Car))


## multiple inheritance

class Battery():
    def battery_info(self):
        return "This is Battery info"

class Engine():
    def engine_info(self):
        return "This is engine info"

class Electric(Battery, Engine, Car):
    pass
    
my_safari = Electric("Tata", "Safari")

print(my_safari.battery_info())
print(my_safari.engine_info())