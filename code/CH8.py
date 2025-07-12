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
    