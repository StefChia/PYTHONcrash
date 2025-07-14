
#Importing pi
'''from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
lines = contents.splitlines()
for line in lines:
    print(line)

pi_string = ''
for l in lines:
    pi_string += l.strip()
print(pi_string)
print(len(pi_string))'''


#CHECKING BIRTHDAY IN MILLION DIGIT

'''from pathlib import Path
path = Path('pi_million_digits.txt')
content = path.read_text().rstrip()
lines = content.splitlines()
pi_string = ''
for l in lines:
    pi_string += l.lstrip()

birthday = input('What is your birthday in digits? (mmddyyyy) ')
if birthday in pi_string:
    print('Yes it is.')
else:
    print('No, it is not.')'''
    


#10.1 LEARNING PYTHON
'''from pathlib import Path
path = Path('learning.txt')
content = path.read_text().rstrip()
print(content)
lines = content.splitlines()
for l in lines:
    print(l)

print(lines)'''


#10.2 LEARNING C

'''from pathlib import Path
path = Path('learning.txt')
content = path.read_text().rstrip()
print(content)
lines = content.splitlines()
for l in lines:
    l = l.replace('python','C')
    print(l)
'''


#10.3 MORE COINCISE

'''from pathlib import Path
path = Path('learning.txt')
content = path.read_text().rstrip()
print(content)
for l in content.splitlines():
    print(l)
    '''
    


#WRITE TO A FILE

'''from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming.")'''


#WRITE MULTIPLES LINES
'''
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)'''



#10.4 GUESTS

'''name = input('What is your name? ')
from pathlib import Path
path = Path('guests.txt')
path.write_text(name)'''

#10.5 GUESTS BOOK

'''names =''
flag = True
while flag:
    curr = input('What is your name? ')
    names += f'{curr.title()}\n'
    dd = input('Is there another name? (yes/not) ')
    if dd.lower() == 'not' :
        flag = False

from pathlib import Path
path = Path('Guests_book.txt')
path.write_text(names)
'''




#EXCEPTIONS
'''try:
    print(5/0)
except ZeroDivisionError:
    print('You cannot divide by zero!')'''



#DIVISION CALCULATOR HANDLING ZeroDivisionError

'''print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:    
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)'''
        
        
        
#HANDLING THE FileNotFoundError 

'''from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")'''


#ANALYZING TEXT

'''from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")'''
    

#WORKING WITH MULTIPLE FILES

'''from pathlib import Path
def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 
        'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)'''
    
    
#ALTERNATIVE

'''from pathlib import Path

def count_mult(filenames):
    """For all path in a list, it couunts the words and provides the coder a text with the file not available."""
    m = 'missing_files.txt'
    p = Path(m)
    missing_files = []
    
    def count_words(path, missing_files):
        """Count the approximate number of words in a file."""
        try:
            contents = path.read_text(encoding='utf-8')
        except FileNotFoundError:
            missing_files.append(f'{path}\n')
        else:
            # Count the approximate number of words in the file:
            words = contents.split()
            num_words = len(words)
            print(f"The file {path} has about {num_words} words.")
            
    for filename in filenames:
        path = Path(filename)
        count_words(path,missing_files)
    fin = ''    
    for i in missing_files:
        fin += i
    p.write_text(fin)
    
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 
        'little_women.txt']
count_mult(filenames)'''



#10.6 ADDITION

'''while True:
    print('\nEnter two numbers and I will give you the sum.\nEnter "q" to quit at anytime.')
    num1 = input('What is the first number? ')
    if num1 == 'q':
        break
    num2 = input('What is the second number? ')
    if num2 == 'q':
        break
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print('Recall: you should enter numbers!')
    else:
        sum = num1 + num2
        print(f'The sum is: {sum}')'''
        


#10.8 CATS AND DOGS

'''from pathlib import Path
paths = ['cats.txt','dogs.txt','lupi.txt']
for p in paths:
    path = Path(p)
    try:
        content = path.read_text().rstrip()
    except FileNotFoundError:
        print(f'\n{p} is not a valid path.')
    else:
        print(f'\n{content}')
        lines = content.splitlines()
        for line in lines:
            print(line)'''

#10.9 SAME BUT SILENT

'''from pathlib import Path
paths = ['cats.txt','dogs.txt','lupi.txt']
for p in paths:
    path = Path(p)
    try:
        content = path.read_text().rstrip()
    except FileNotFoundError:
        pass
    else:
        print(f'\n{content}')
        lines = content.splitlines()
        for line in lines:
            print(line)'''

#10.10 COMMON WORDS

'''from pathlib import Path
path = Path('alice.txt')
try:
    content = path.read_text().rstrip()
except FileNotFoundError:
    print(f'The path {path} is not a valid one.')
else:
    content = content.lower()
    print(content.count('the'))
    print(content.count('the '))
'''






#STORING DATA using JSON format

'''from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)'''


#RETRIVING FROM JSON FORMAT

'''from pathlib import Path
import json
path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
'''

#es
'''
from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")'''
    



#REFACTORING

'''from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
         return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()'''



#10.11-10.12 FAVORITE NUMBER

'''from pathlib import Path
import json
path = Path('favorite_num.json')
if path.exists():
    content = path.read_text()
    num = json.loads(content)
    print(f'Your favorite number is {num}')
else:
    num = input('What is your favorite number? ')
    content = json.dumps(num)
    path.write_text(content)
    print('We will remember next time.')'''



#10.13 USER DICTIONARY ICE CREAMS

'''from pathlib import Path
import json

path = Path('Cust_tastes.json')

def check(path):
    """Checks if a path exist and print the values. Otherwise ask for client taste."""
    if path.exists():
        content = path.read_text()
        d = json.loads(content)
        print(f'{path} is a valid path.\n')
        for k,v in d.items():
            print(f'\n{k.title()} favorite taste is {v}.')
    else:
        d = {}
        while True:
            name = input('Name of the customer: ')
            taste = input('Fav taste of the customer: ')
            contin = input('Add another? (yes/no)')
            d[name.lower()] = taste.lower()
            if contin.lower() == 'no':
                break
        content = json.dumps(d)
        path.write_text(content)
        
check(path)      '''



#10.14 VERIFY USER

from pathlib import Path
import json

path = Path('usernames.json')

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
         return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greetings(path):
    """ """
    username = get_stored_username(path)
    if username:
        check = input(f'Is {username} your username? (y/n)')
        if check == 'yes':
            print('It is allright!')
        else:
            new = get_new_username(path)
            print(f'We have saved {new} as your username for next time.')
    else:
        user = get_new_username(path)
        print(f'\nThanks to have registered. Your username is {user}.')


greetings(path)