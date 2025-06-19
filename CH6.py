'''alien_0 = {'colour':'green','lifepoints':5}

print(alien_0['colour'])
print(alien_0['lifepoints'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0['colour'] = 'yellow'

print(f'Now the colour is {alien_0["colour"]}.')'''

#example

'''alien_0 = {'position_x':0, 'position_y':25, 'vel':'middle'}

print(f'The initial position is {alien_0["position_x"]} meters on x axes.')

if alien_0['vel'] == 'low':
    alien_0['position_x'] = alien_0['position_x'] + 1
elif alien_0['vel'] == 'middle':
    alien_0['position_x']+= 2
else:
    alien_0['position_x'] = alien_0['position_x'] + 3
    
print(f'The final position is {alien_0["position_x"]} on x axis.')'''

#example

'''fav_language = {
    'Sara' : 'python',
    'jen' : 'c',
    'edward' : 'rust',
    'phil' : 'python'    
}
print(f'Sara favourite language is: {fav_language.get('diego')}.')'''



#example
'''
marina = {'first_name':'Marina', 'last_name':'Pancheri', 'age':24, 'city':'Roma'}
print(marina['first_name'])
print(marina['last_name'])
print(marina['age'])
print(marina['city'])'''

#example
'''
fav_num = {'Lebron': 23, 'KD':35, 'Steph':30, 'Freak': 34,'Joker': 12}
print(fav_num['Joker'])
'''

#example
'''
dict = {'jump': 'take a leap'}
print(f'Jump:\n{dict["jump"]}.')
'''

#example
'''
fav_language = {
    'sara' : 'python',
    'jen' : 'c',
    'edward' : 'rust',
    'phil' : 'python'    
}
for name, lang in fav_language.items():
    print(f'The fav language of {name.title()} is {lang}.')

sel_names = ['luke','jen']

for name in sorted(fav_language.keys(),reverse=True):
    print(f'\nHi {name.title()}!')
    
    if name.lower() in sel_names:
        print(f'I know you really like {fav_language[name].upper()}.')  

for lang in set(fav_language.values()):
    print(lang)
'''

#example
'''
rivers = {'Nile':'Egypt','Rio':'Brazil','Senna':'France'}
for riv, country in rivers.items():
    print(f'The {riv.title()} runs thorugh {country.title()}.')

for riv in rivers:
    print(riv.title())

for country in rivers.values():
    print(country)
'''
#example
'''
fav_language = {
    'sara' : 'python',
    'jen' : 'c',
    'edward' : 'rust',
    'phil' : 'python'    
}
names_todo =['jen', 'albert','pier','phil']
for name in names_todo:
    if name in fav_language.keys():
        print(f'\n{name.title()}, you already voted.')
    else:
        print(f'\nPlease {name.title()}, come to vote.')
'''

#NESTING
'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
'''

#Example
'''
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
'''


#Example
'''
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is: {languages[0]}.")
'''

#Example
'''
marina = {'hair':'brown','city':'rome','age':24}
ale = {'hair':'blonde', 'city':'milan', 'age':23}
giulia = {'hair':'black', 'city':'milan', 'age':23}

friends = [marina, ale, giulia]
for fr in friends:
    print(f'\n{fr['hair']}, {fr['city'].title()}, {fr['age']}.')
'''

#example
'''
marina = ['ponte','milan','rome']
ale = ['vezza', 'milan']
giulia = ['villa', 'milan', 'menheim']

places = {'marina':marina, 'ale':ale, 'giulia':giulia}

for name,pl in places.items():
    print(f'\n{name.title()} favourite places are:')
    for place in pl:
        print(f'\n{place.title()}')
'''

#example
'''
fav_num = {
    'Lebron': [6,23],
    'KD':[35,7],
    'Steph':[30,],
    'Freak': [34,],
    'Joker': [12,]}

for nm, nb in fav_num.items():
    print(f'\nThe favourite numbers of {nm.title()}:')
    for n in nb:
        print(f'\n\t{n}')
'''

#example

cities = {
    'london':{'country':'uk','population': 15, 'fact':'Not bad'},
    'milan':{'country':'ita','population':2, 'fact':'good food'},
    'madrid':{'country':'spain','population':1, 'fact':'nice buildings'}
    }

for nm, pills in cities.items():
    print(f'\nThe features of {nm.title()} are:')
    for f,g in pills.items():
        print(f'{f}:\t{g}')