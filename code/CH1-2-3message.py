import random
vips =['Alessandro Magno','Seneca','Momo Hali','Feyman']

print(f'Dear {vips[0]}, Would you go out for a dinner?')
busy = 'Momo Hali'
vips.remove(busy)
print(f'Unfortunately {busy} is not available.')
new = 'Isaia'
vips.insert(0,new.lower())
print(f'{new.title()} will be happy to join!')

print('You lucky guys, what do you think about add three more friends!')
vips.insert(0,'Cesare')
vips.insert(2,'Barbero')
vips.append('Gandalf')
print(f'Even the great {vips[-1].title()} will join us!')
print(len(vips))
print(f'The {len(vips)}th person is {vips[-1]}.')

while len(vips)>2 :
    byby = vips.pop(random.choice(range(len(vips))))
    print(f'Sorry {byby.title()}, you will join us next time.')

print(f'We are ivinting only {len(vips)} to the dinner.')
del vips[1]
del vips[0]
print(vips)