class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol Or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla=ElectricCar("Tesla","Model S", "100kwh")        
#print(my_tesla.brand)
print(my_tesla.full_name())
print(my_tesla.get_brand())

my_car=Car("Honda","City")
#my_car.model="Amaze"

print(my_car.model)



# my_new_car=Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())