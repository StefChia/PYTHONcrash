
#Class Dog
'''class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")'''


#Class Restaurant
'''class Restaurant:
    """It's a restaurant."""
    def __init__(self, restaurant_name, cousine_type):
        self.name = restaurant_name
        self.type = cousine_type
        
    def describe_restaurant(self):
        print(f'{self.name} is a restaurant of {self.type} cousine.')
    
    def open_restaurant(self):
        print('The restaurant is open.')
    
l = {'syesta':'Steakhouse','garden':'pizza','ciccio':'pizza'}
for i, j in l.items():
    inst = Restaurant(i,j)
    print(inst.name)
    print(inst.type)
    inst.describe_restaurant()
    inst.open_restaurant()
    
    
syesta = Restaurant('Syesta','Steakhouse')
print(syesta.name)
print(syesta.type)
syesta.describe_restaurant()
syesta.open_restaurant()'''




#class Users
'''
class Users:
    """Class for classic users infos."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def custom_greetings(self):
        print(f'Hi {self.first_name} {self.last_name}, you look good!')

me = Users('Ciccio','Games', 89)
me.custom_greetings()'''



#class Car
'''
class Car:
    """Represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Returns a neatly formatted string name syinthesis."""
        n = f'{self.make} {self.model} {self.year}'
        return n.title()

    def read_odometer(self):
        """Print a statement showing the car mileage."""
        print(f'The car mileage is: {self.odometer_reading} KM')
    
    def update_odometer(self,mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cannot roll the odometer back!')
    def increment_odometer(self,miles):
        """Add a number of miles run to the odometer record.
        The number has to be positive."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('You cannot roll odometer back!')
    
my_car = Car('Audi','A4', 2025)
my_car.update_odometer(23)
my_car.update_odometer(15)

my_car.increment_odometer(-5)
my_car.increment_odometer(5)

print(f'My car infos:\n{my_car.get_descriptive_name()}')
my_car.read_odometer()
'''


#9.4 NUMBER SERVED
'''
class Restaurant:
    """It's a restaurant."""
    def __init__(self, restaurant_name, cousine_type):
        self.name = restaurant_name
        self.type = cousine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f'{self.name} is a restaurant of {self.type} cousine.')
    
    def open_restaurant(self):
        print('The restaurant is open.')
    
    def set_number_served(self,num):
        """Set the number of customers served."""
        self.number_served = num
    
    def increment_number_served(self):
        """Ask and Add a number to the total customers served"""
        add = input('How many more we have served? ')
        self.number_served += int(add)
        
    
syesta = Restaurant('Syesta','Steakhouse')
print(f'{syesta.name.title()} has served {syesta.number_served} customers today.')
#syesta.number_served = 15
#syesta.set_number_served(15)
syesta.increment_number_served()
print(f'{syesta.name.title()} has served {syesta.number_served} customers today.')'''



#9.5 LOGIN ATTEMPTS


class Users:
    """Class for classic users infos."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    
    def custom_greetings(self):
        print(f'Hi {self.first_name} {self.last_name}, you look good!')
    
    def increment_login_attempts(self):
        """Increment current streak of login attempts by 1. """
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the current streak o login attempts."""
        self.login_attempts = 0
    

me = Users('Ciccio','Games', 89)
me.custom_greetings()
for i in range(1,10):
    me.increment_login_attempts()

print(me.login_attempts)
me.reset_login_attempts()
print(me.login_attempts)