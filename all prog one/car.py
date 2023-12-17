#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100
    def get_descriptive_name(self):
        long_name = str(self.year) +' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+ str(self.odometer_reading) + " miles on it")
    def update_odometer(self,mileage):
        
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
             print("you can't roll back an odometer")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
class Battery():
    def __init__(self,battery_size=70):
        
        self.battery_size = battery_size
        
    def describe_battery(self):
        """print a ststement decribing the battery size"""
        print("This car has a " + str(self.battery_size)+ "-Kwh battery")
    def get_range(self):
        """print a statement about the range this battery provide"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range =275
        message = "This can go approximately " + str(range)
        message += "Miles on a full charge"
        print(message)
        
class electricCar(Car):  
    """represent aspect of a car,specific to electric vehicles"""
    def __init__(self,make,model,year):
        """initialise attributes of the parent class"""
        super().__init__(make,model,year)
        self.battery = Battery()
my_tesla=electricCar('Tesla','model S',2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()        
my_tesla.battery.get_range()
            


# In[ ]:




