
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


'''class Users:
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
print(me.login_attempts)'''


#CHILD CLASS
'''
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 40
    
    def describe_battery(self):
        """Print the battery status of the electric car."""
        print(f'The current battery is {self.battery_size} KWH.')
        
        


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
print(my_leaf.battery_size)
my_leaf.describe_battery()'''



#9.6 ICE CREAM STAND

'''class Restaurant:
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
    
    def increment_number_served(self,add):
        """Ask and Add a number to the total customers served"""
        self.number_served += int(add)
        

class IceCreamStand(Restaurant):
    """It is a specific kind of restaurant for ice-creams."""
    def __init__(self, restaurant_name, cousine_type, *flavours):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cousine_type)
        self.flavours = flavours
    
    def show_flavours(self):
        """Print the flavours available."""
        for fl in self.flavours:
            print(f'The {fl} flavour is available.')


gelbo = IceCreamStand('Gelbo','Ice-Creams','vanilla','panna','choco')
print(gelbo.flavours)
gelbo.show_flavours()'''


#9.7 ADMIN
        
'''class Users:
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


class Admin(Users):
    """Model admins, a particular kind of users."""
    def __init__(self, first_name, last_name, age, *privileges):
        """Initializes the parents attributes"""
        super().__init__(first_name, last_name, age)
        self.privileges = privileges
    
    def show_privileges(self):
        """Print the privileges of the admin."""
        for pr in self.privileges:
            print(f'{pr}')


boss = Admin('Mario','Rossi', 45, 'Can add posts', 'Can delete posts', 'Can ban users')
boss.show_privileges()'''




#9.8 PRIVILEGES

'''class Users:
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
        
class Privileges:
    """Model privileges"""
    def __init__(self, *privileges):
        """Init Privileges class attributes."""
        self.privileges = privileges
    
    def show_privileges(self):
        """Print the privileges of the admin."""
        for pr in self.privileges:
            print(f'{pr}')
            

class Admin(Users):
    """Model Admin class, a particular user type."""
    def __init__(self, first_name, last_name, age, *privileges):
        """Initialize parent attributes"""
        super().__init__(first_name,last_name, age)
        self.privil = Privileges(*privileges)
        

boss = Admin('Mario','Rossi', 45,'Can add posts', 'Can delete posts', 'Can ban users')
boss.privil.show_privileges()'''






#9.9 BATTERY UPGRADE
'''
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def upgrade_battery(self):
        """Check battery size and modify it to 65"""
        if self.battery_size != 65:
            self.battery_size = 65
        


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery.battery_size == 40:
            range = 150
        elif self.battery.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")



my_leaf = ElectricCar('nissan', 'leaf', 2024)

my_leaf.battery.describe_battery()
my_leaf.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
my_leaf.get_range()
print(my_leaf.battery.battery_size)'''



#IMPORT A SINGLE CLASS FROM A MODULE modulewithclass.py
'''
from modulewithclass import Car

my_car = Car('Audi','A4', 2025)
my_car.update_odometer(23)
my_car.update_odometer(15)'''





#9.13 DICE
'''
class Dice:
    """Model a dice with n face and roll it."""
    def __init__(self,faces=6):
        "Initialize the class attributes."
        self.faces = faces
    def roll_dice(self):
        """Roll the dice."""
        from random import randint
        roll_outcome = randint(1,self.faces)
        print(f'The draw number is {roll_outcome}.')
        
sixdice = Dice(6)
faces = [6,10,20]

c=0
for f in faces:
    d =Dice(f)
    while f != 0:
        d.roll_dice()
        c += 1
        f -= 1

print(f'\n{c}')'''





#9.14 LOTTERY

'''def draw_lott(lotto):
    """Draw 4 elements for a lottery and print the winner."""
    import random as rd
    drawns = []
    for i in range(4):
        curr = rd.choice(lotto)
        lotto.remove(curr)
        drawns.append(curr)
    print(f'The final winner has the following elements:')
    for i in drawns:
        print(f'-{i}')
        

ltt  =[1,2,3,4,5,6,7,8,9,10,'a','b','c','d']
draw_lott(ltt)'''




def draw_lott(lotto):
    """Draw 4 elements for a lottery and print the winner."""
    import random as rd
    drawns = []
    for i in range(4):
        curr = rd.choice(lotto)
        lotto.remove(curr)
        drawns.append(curr)
    return drawns

def time_to_win(lotto,my_ticket):
    """Simulate the number of times you would play until you win."""
    c = 0
    while True:
        c += 1
        drawns = draw_lott(lotto[:])
        if drawns == my_ticket:
            break
    return c
    
def sim(N):
    """Simulate playing until I win, for N times. Check how far I am from probability. """
    store_times = []
    for i in range(N):
        times = time_to_win(ltt,my_ticket)
        store_times.append(1/times)
    return store_times
        


p = 1/(14*13*12*11)          

ltt  =[1,2,3,4,5,6,7,8,9,10,'a','b','c','d']
my_ticket = [3,'a',7,9]
#times = time_to_win(ltt,my_ticket)
#print(times)

storage = sim(100)
import numpy as np
print(np.mean(storage))
print(p)