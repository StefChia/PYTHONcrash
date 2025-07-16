
#Test for the function in name_function.py
'''
from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
'''    
#EX 11.3 Employees

class Employee:
    """Model the employee class"""
    def __init__(self,first_name,last_name,salary):
        """Initialize the class attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self,amount=5000):
        """Increase salary by an amount."""
        am = amount
        self.salary += am
    