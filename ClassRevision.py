'''
ClassRevision
'''


class Cars:

    def __init__ (self,color,brand,model,type):
        self.color = color
        self.brand = brand
        self.model = model
        self.type = type

    def name_CarBrand(self):
        print(f"This car is a {self.brand}.")
    
class Bikes(Cars):
    
    def name_BikeBrand(self):
        print(f"This bike is a {self.brand}.")


    pass

'''
Cars
'''

c1 = Cars("Red","Ferrari","La Ferrari","Sports")
c2 = Cars("Blue","Ford","Focus","Hatchback")

'''
Bikes
'''

b1 = Bikes("Black","Kawasaki","Ninja 500","Sports")
b2 = Bikes("Red","Yamaha","R1","Sports")

class Garage:

    def __init__(self,max_capacity,floors):
        self.capacity = []
        self.cars = str([])
        self.bikes = str([])
        self.max_capacity = max_capacity
        self.floors = floors

    def park_car(self,Cars):
        if len(self.capacity) < self.max_capacity:
            self.capacity.append(Cars)
            return True
        return False
    
    def park_bike(self,Bikes):
        if len(self.capacity) < self.max_capacity:
            self.capacity.append(Bikes)
            return True
        else:
            print("Garage is Full")
    
    def check_garage(self):
        for vehicle in self.capacity:
            if isinstance(vehicle,Bikes):
                print(f"Bike: {vehicle.color} {vehicle.brand} {vehicle.model} ({vehicle.type})")   
                
            elif isinstance(vehicle,Cars):
                print(f"Car: {vehicle.color} {vehicle.brand} {vehicle.model} ({vehicle.type})")
                    
    
    
g1 = Garage(7,1)


g1.park_car(c1)
g1.park_bike(b1)
g1.park_car(c2)
g1.park_bike(b2)
g1.check_garage()