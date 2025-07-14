
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



#STORING DATA