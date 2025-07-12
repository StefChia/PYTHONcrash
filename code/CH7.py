'''name = input('Enter your name: ')
print(f'Hi {name}!')'''

'''#EVEN NUMBER ASSESSING
num = input('Enter a number: ')
num = int(num)

if num % 2 == 0 :
    print(f'{num} is an even number.')
else:
    print(f'{num} is an odd number.')'''
    


def even_or_odd(number):
    #check class
    if not isinstance(number,int):
        print(f'{number} is not a correct class type.\nTry again with an Int number.')
        return
    else:
        try:
            if number % 2 == 0:
                print(f"\nThe number {number} is even.")
            else:
                print(f"\nThe number {number} is odd.")
        except Exception as e:
            print(f'The error is of {e} type.')



'''car = input('What kind of rental car would you like? ')
print(f'Let me see if I can find a {car} though.')'''

'''num = input('How many people at your table? ')
num = int(num)
if num < 8 :
    print('A table is ready!')
else: 
    print('Unfortunately you have to wait.')'''
    
'''num = input('Tell me a number: ')
num = int(num)
if num % 10 == 0 :
    print(f'{num} is a multiple of 10.')
else:
    print(f'{num} is not a multiple of 10.')'''


    
#WHILE LOOPS

'''number = 1
while number <= 5 :
    print(number)
    number += 1'''
    
#QUIT PLAYING EXAMPLE
'''
prompt = '\nTell me something and I will repeat back to you.'
prompt += '\nTo end this game input "QUIT". '

message = ""
while message != 'QUIT':
    message = input(prompt)
    if message != 'QUIT':   
        print(f'\n{message}')'''

        
#USING A FLAG
'''
prompt = '\nTell me something and I will repeat back to you.'
prompt += '\nTo end this game input "QUIT". '

active = True
while active:
    message = input(prompt)
    
    if message == 'QUIT':
        active = False
    else:
        print(message)    '''


#BREAKING LOOPS
'''
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!") '''
        
#Using continue in a loop
'''
num = 0
while num < 10:
    num += 1
    
    if num % 2 == 0:
        continue
    print(num)
'''

#Pizza topping
'''
prompt = '\nWhich topping I should add to your pizza? '
prompt += '\n(To end insert "quit".) '

flag = True
while flag:
    top = input(prompt)
    if top != 'quit':
        print(f'I will add {top} to your pizza!')
    else:
        break
'''

#Movie tickets
'''
prompt = '\nHow old are you?'
prompt += '\n(Insert quit to exit.) '

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        cost = 0
    elif age <=12:
        cost = 10
    else:
        cost = 15
    print(f'Your ticket costs {cost} $.')
'''

#ALTERNATIVES
'''
prompt = '\nHow old are you?'
prompt += '\n(Insert quit to exit.) '

flag = True

while flag:
    age = input(prompt)
    if age == 'quit':
        flag = False
        continue
    age = int(age)
    if age < 3:
        cost = 0
    elif age <=12:
        cost = 10
    else:
        cost = 15
    print(f'Your ticket costs {cost} $.')
'''

#ALTERNATIVES
'''
prompt = '\nHow old are you?'
prompt += '\n(Insert quit to exit.) '

age = 0

while age != 'quit':
    age = int(age)
    if age < 3:
        cost = 0
    elif age <=12:
        cost = 10
    else:
        cost = 15
    
    if age != 0:
        print(f'Your ticket costs {cost} $.')
    age = input(prompt)
'''

#ALTERNATIVE
'''
prompt = '\nHow old are you?'
prompt += '\n(Insert quit to exit.) '

age = ""

while age != 'quit':
    age = input(prompt)
    if age != 'quit':
        
        age = int(age)
        if age < 3:
            cost = 0
        elif age <=12:
            cost = 10
        else:
            cost = 15
        print(f'Your ticket costs {cost} $.')
'''


#Using while loops with lists and dictionaries
'''
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print (f'Current user: {current_user.title()}')
    confirmed_users.append(current_user)
    
print('\nThe following users have been confirmed:')
for us in confirmed_users:
    print(f'\n{us.title()}')
'''

#REMOVING ALL INSTANCES OF A SPECIFIC VALUE FROM A LIST
'''
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)
'''

#STORING VALUES IN A DICTIONARY
'''

response = {}
flag = True

while flag:
    name = input('\nWhat is your name? ')
    mountain = input('\nWhich mountain would you like to climb? ')
    response[name] = mountain
    
    repeat = input('Would you like someone else to answer this poll? (Yes/No) ')
    if repeat.lower() == 'no':
        flag = False

#Polling is complete. Show the results.
for name,res in response.items():
    print(f'\n{name.title()} wants to go to climb {res.title()} mountain.')
'''


#DELI
'''
orders = ['Tuna Sandwich','Ham Sandwich', 'Mayo Sandwich']
finished = []

while orders:
    curr = orders.pop()
    print(f'\nI am making {curr}.')
    finished.append(curr)
    
for s in finished:
    print(f'\nThe {s} is completed.')
print('\nAll the sandwhiches are completed.')
'''

'''

orders = ['Tuna Sandwich','Ham Sandwich', 'Mayo Sandwich','Pastrami','Pastrami','Pastrami']
finished = []

if 'Pastrami' in orders:
    print('Deli has run out of Pastrami.')
    while 'Pastrami' in orders:
        orders.remove('Pastrami')

while orders:
    curr = orders.pop()
    print(f'\nI am making {curr}.')
    finished.append(curr)
    
for s in finished:
    print(f'\nThe {s} is completed.')
print('\nAll the sandwhiches are completed.')
'''

#Dream vacation
vacations = {}
flag = True

while flag:
    name = input('\nWhat is your name? ')
    vac = input('\nWhat is your drem vacation? ')
    vacations[name.lower()]= vac.lower()
    
    repeat = input('\nWould you like someone to continue the poll? (yes/no) ')
    if repeat.lower()== 'no':
        flag = False

print('\nThe poll is finished:')
for n,v in vacations.items():
    print(f'\n{n.title()} would like to go to {v.title()}.')
    