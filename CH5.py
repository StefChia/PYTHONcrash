'''requested_toppings = ['mushrooms','green pepper','extra cheese']
nomore = ['green pepper','oil']

if requested_toppings:
    for req in requested_toppings:
        if req in nomore:
            print(f'\nSorrry we run out of {req.title()}.')
        else:
            print(f'\n{req.title()} was added as a topping.')

    print('\n\tYour pizza is ready.')
else:
    print('Are you sure to have a plain pizza?')'''
    

'''nicknames = ['hhh','ggg','kd','ad','admin']

if nicknames:
    
    for nick in nicknames:
        if nick == 'admin':
            print(f'Hello {nick.title()}, would you like to see a scouting report?')
        else:
            print(f'Hello {nick.title()}, thank you for logging today.')
else:
    print('Make sure to have names.')'''
    



'''current_users = ['Hhh','Ggg','KD','ad','admin']
new_users = ['magic','king','steph','kd','freak']

curr_users = []
for n in current_users:
    curr_users.append(n.lower())

for new in new_users:
    if new.lower() in curr_users:
        print(f'{new} is already taken.')
    else:
        print(f'{new} is available.')'''
        
        
num = list(range(1,10))

for n in num:
    if n == 1:
        print(f'{n}st')
    elif n == 2:
        print(f'{n}nd')
    elif n == 3:
        print(f'{n}rd')
    else:
        print(f'{n}th')
