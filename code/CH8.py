'''
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
'''

'''
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
'''

'''
def message():
    print('I am trying to learns as much as I can.')

message()
'''


'''
#define fav book function
def fav_book(title):
    print(f'My favourite book is {title.title()}.')

fav_book('CENERENTOLA')
'''


'''
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'igor')

describe_pet(pet_name='Hamtaro', animal_type='hamster')
'''

#T-SHIRT function
'''
def tshirt(size,text=str):
    """Customize your t-shirt"""
    print(f'The shirt is of {size} size and the text will be {text.title()}.')
    
tshirt(40,'happy')

def makeshirt(size='L',text='I love python'):
    """Customize your t-shirt"""
    print(f'The shirt is of {size} size and the text will be {text.title()}.')

makeshirt(text='Happy Easter')
'''

#Describe city function
'''
def describe_city(city,country='Italy'):
    """Link city-country"""
    print(f'{city.title()} is in {country.title()}.')

describe_city('verona')
describe_city('firenze')
describe_city('paris','france')
'''


#Formatting names
'''
def get_formatting_names(name,surname):
    """Return a net formatted name-surname"""
    n = f'{name} {surname}'
    n = n.title()
    return n

musician = get_formatting_names('BOB','dylan')
print(musician)
'''

#Function that returns a dictionary
'''
def build_person(name, surname, age = None):
    """Returns a dictionary with the info of a person."""
    if age:
        d = {'first':name.lower(), 'last': surname.lower(), 'age': int(age)}
    else:
        d = {'first':name.lower(), 'last':surname.lower()}
    return d

a = build_person('Mario','Rossi',37)
print(a)
b = build_person('Lorenzo','Bera')
print(b)
'''

#While loop and functions
'''
def get_formatting_names(name,surname):
    """Return a net formatted name-surname"""
    n = f'{name} {surname}'
    n = n.title()
    return n

while True:
    print('\nPlease tell me your name.')
    print('\nInsert q at anytime to quit.')
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    
    formatted_values = get_formatting_names(f_name,l_name)
    print(f'Hello {formatted_values}, have a nice day!')
'''


#FUNCTION CITY-COUNTRY
'''
def get_netted_text(city,country):
    """Returns a netted city, country text"""
    text = f'{city}, {country}.'
    return text.title()

d = {'milan':'italy', 'paris':'france', 'malaga':'spain'}
for c,cc in d.items():
    print(get_netted_text(c,cc))
    
'''

# ALBUM FUNCTION RETURNING DICTIONARY
'''
def album(name_artist, album_title, n_song=None):
    """Returns a dictionary with artist name, album title and eventually num songs"""
    if n_song:
        d = {'artist':name_artist, 'title':album_title, 'n_song':n_song}
    else:
        d = {'artist':name_artist, 'title':album_title}
    return d

#dd = album('Justin Bieber','Swag',22)
#print(dd)

while True:
    print('\nPrint a dictionary for your album.')
    print('\nInsert q to quit anytime.')
    name = input('What is the name of the artist? ')
    if name == 'q':
        break
    title = input('What is the name of the album? ')
    if title == 'q':
        break
    a = album(name,title)
    print(a)
'''


#PASS TO THE FUNCTION A LIST
'''
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)    
'''

#MESSAGES
'''
def messages(text):
    """Prints the messages in a list"""
    for t in text:
        print(t)
        
m = ['Hey','You','are','a','QT']
messages(m)
'''

#SENDING MESSAGES
'''
def messages(send,sent):
    """Prints the messages in a list"""
    while send:
        curr = send.pop()
        sent.append(curr)
        print(curr)
    sent.reverse()

        
a = ['Hey','You','are','a','QT']
b = []

messages(a,b)
print(a)
print(b)

messages(a[:],b)
print(a)
print(b)
'''


#Arbitrary number of arguments
'''
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''



#SANDWICH
'''
def sandwiches(*toppings):
    """Print the toppings of a sandwich"""
    print('\nThe sandwich is made of:')
    for t in toppings:
        print(f'- {t}')
        

sandwiches('ham','cheese','salad')
'''

#Arbitrary key-word arguments
'''
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
	  user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
'''

#Cars

def make_car(manufacturer, model_name, **args):
    """Returns a dictionary of the info."""
    args['manufacturer'] = manufacturer
    args['model name'] = model_name
    return args

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)



#WORKING AND IMPORTING MODULE
'''
import module
module.make_pizza('pepperoni')
module.make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''

#Importing a specific function
'''
from module import make_pizza
make_pizza('mushrooms', 'green peppers', 'extra cheese')'''

