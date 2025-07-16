# NOTES

https://github.com/ehmatthes/pcc_3e.git

**Part I
Basics**

Part I of this book teaches you the basic concepts you’ll need to write Python programs. Many of these concepts are common to all programming languages, so they’ll be useful throughout your life as a programmer.
In Chapter 1 you’ll install Python on your computer and run your first program, which prints the message Hello world! to the screen.
In Chapter 2 you’ll learn to assign information to variables and work with text and numerical values.
Chapters 3 and 4 introduce lists. Lists can store as much information as you want in one place, allowing you to work with that data efficiently. You’ll be able to work with hundreds, thousands, and even millions of values in just a few lines of code.
In Chapter 5 you’ll use if statements to write code that responds one way if certain conditions are true, and responds in a different way if those conditions are not true.
Chapter 6 shows you how to use Python’s dictionaries, which let you make connections between different pieces of information. Like lists, dictionaries can contain as much information as you need to store.

In Chapter 7 you’ll learn how to accept input from users to make your programs interactive. You’ll also learn about while loops, which run blocks of code repeatedly as long as certain conditions remain true.
In Chapter 8 you’ll write functions, which are named blocks of code that perform a specific task and can be run whenever you need them.

Chapter 9 introduces classes, which allow you to model real-world objects. You’ll write code that represents dogs, cats, people, cars, rockets, and more.
Chapter 10 shows you how to work with files and handle errors so your programs won’t crash unexpectedly. You’ll store data before your program closes and read the data back in when the program runs again. You’ll learn about Python’s exceptions, which allow you to anticipate errors and make your programs handle those errors gracefully.
In Chapter 11 you’ll learn to write tests for your code, to check that your programs work the way you intend them to. As a result, you’ll be able to expand your programs without worrying about introducing new bugs. Testing your code is one of the first skills that will help you transition from beginner to intermediate programmer.”

**CH1:**

“First, use the cd command to navigate to the python_work folder, which is in the Desktop folder. Next, use the ls command to make sure hello_world.py is in this folder. Then run the file using the command python3 hello_world.py.
Most of your programs will run fine directly from your editor. But as your work becomes more complex, you’ll want to run some of your programs from a terminal.”

“Variables Are Labels
Variables are often described as boxes you can store values in. This idea can be helpful the first few times you use a variable, but it isn’t an accurate way to describe how variables are represented internally in Python. It’s much better to think of variables as labels that you can assign to values.”

ABOUT STRINGS

“A string is a series of characters. Anything inside quotes is considered a string in Python,”

METHODS

“A method is an action that Python can perform on a piece of data. The dot (.) after name in name.title() tells Python to make the title() method act on the variable name. Every method is followed by a set of parentheses, because methods often need additional information to do their work. That information is provided inside the parentheses. The title() function doesn’t need any additional information, so its parentheses are empty.”

```python
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
```

“The lower() method is particularly useful for storing data. You typically won’t want to trust the capitalization that your users provide, so you’ll convert strings to lowercase before storing them. Then when you want to display the information, you’ll use the case that makes the most sense for each string.”

“Using Variables in Strings
In some situations, you’ll want to use a variable’s value inside a string.”(aka f string)

```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)”
```

“place the letter f immediately before the opening quotation mark . Put braces around the name or names of any variable you want to use inside the string. ”

```python
“first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")”

```

You can also apply method to the variables

“To add a tab to your text, use the character combination \t:

```python
print("Python")
Python
print("\tPython")
Python

#To add a newline in a string, use the character combination \n:
print("Languages:\nPython\nC\nJavaScript")
Languages:
Python
C
JavaScript
```

“Stripping Whitespace
Extra whitespace can be confusing in your programs.”

```python
>>> favorite_language = ' python '
❷ >>> favorite_language.rstrip()
' python'
❸ >>> favorite_language.lstrip()
'python '
❹ >>> favorite_language.strip()
'python”

```

To ensure that no whitespace exists at the right side of a string, use the strip() method:

strip()

rstrip()

lstrip()

“In the real world, these stripping functions are used most often to clean up user input before it’s stored in a program.”

Removing Prefixes
When working with strings, another common task is to remove a prefix. Consider a URL with the common prefix https://. We want to remove this prefix, so we can focus on just the part of the URL that users need to enter into an address bar.”

```python
“>>> nostarch_url = 'https://nostarch.com'
>>> nostarch_url.removeprefix('https://')
'nostarch.com”
```

method removeprefix()

Numbers

Integers

Floats: 

“Python calls any number with a decimal point a float.”

“When you divide any two numbers, even if they are integers that result in a whole number, you’ll always get a float:”

“If you mix an integer and a float in any other operation, you’ll get a float as well”

“Python defaults to a float”

Underscores in Numbers

```python
>>> universe_age = 14_000_000_000
>>> print(universe_age)
14000000000
```

“When you print a number that was defined using underscores, Python prints only the digits:”

“Python ignores the underscores”

Multiple Assignment
You can assign values to more than one variable using just a single line of code.”

```python
>>> x, y, z = 0, 0, 0
```

Constants
A constant is a variable whose value stays the same throughout the life of a program. Python doesn’t have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed:

```python
MAX_CONNECTIONS = 5000
```

“How Do You Write Comments?
In Python, the hash mark (#) indicates a comment. Anything following a hash mark in your code is ignored by the Python interpreter.”

“writing good comments can save you time by summarizing your overall approach clearly.”

“Writing clear, concise comments in your code is one of the most beneficial habits you can form as a new programmer.”

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

“If two Python programmers are asked to solve the same problem, they should come up with fairly compatible solutions. This is not to say there’s no room for creativity in programming. On the contrary, there is plenty of room for creativity! However, much of programming consists of using small, common approaches to simple situations within a larger, more creative project. The nuts and bolts of your programs should make sense to other Python programmers.”

“Don’t try to write perfect code; write code that works, and then decide whether to improve your code for that project or move on to something new.”

**CH2:LISTS**

“What Is a List?
A list is a collection of items in a particular order.”

“In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.”

“Accessing Elements in a List
Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired.”

```python
“bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])”

```

“ndex Positions Start at 0, Not 1”

“This is true of most programming languages, and the reason has to do with how the list operations are implemented at a lower level.”

“Using this counting system, you can get any element you want from a list by subtracting one from its position in the list. For instance, to access the fourth item in a list, you request the item at index 3.”

“for accessing the last element in a list. If you ask for the item at index -1”

“This convention extends to other negative index values as well. The index -2 returns the second item from the end of the list”

```python
“bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)”
```

“Most lists you create will be dynamic, meaning you’ll build a list and then add and remove elements from it as your program runs its course. ”

“To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.”

```python
“motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)”

```

“You might want to add a new element to a list for many reasons.”

```python
motorcycles.append('ducati')
```

“Appending Elements to the End of a List
The simplest way to add a new element to a list is to append the item to the list. When you append an item to a list, the new element is added to the end of the list.”

“The append() method makes it easy to build lists dynamically. For example, you can start with an empty list and then add items to the list using a series of append() calls.”

```python
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
```

“Building lists this way is very common, because you often won’t know the data your users want to store in a program until after the program is running. To put your users in control, start by defining an empty list that will hold the users’ values. Then append each new value provided to the list you just created.”

“Inserting Elements into a List
You can add a new element at any position in your list by using the insert() method.”

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)”
```

“Removing Elements from a List
Often, you’ll want to remove an item or a set of items from a list. ”

“You can remove an item according to its position in the list or according to its value.”

```python
del motorcycles[0]
```

“You can remove an item from any position in a list using the del statement if you know its index.”

Removing an Item Using the pop() Method
Sometimes you’ll want to use the value of an item after you remove it from a list.”

“For example, you might want to get the x and y position of an alien that was just shot down, so you can draw an explosion at that position. In a web application, you might want to remove a user from a list of active members and then add that user to a list of inactive members.
The pop() method removes the last item in a list, but it lets you work with that item after removing it. ”

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
```

“Popping Items from Any Position in a List
You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses:”

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

```

Removing an Item by Value

“Sometimes you won’t know the position of the value you want to remove from a list.”

remove() method.

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)”
```

“You can also use the remove() method to work with a value that’s being removed from a list. Let’s remove the value 'ducati' and print a reason for removing it from the list:”

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")”
```

“The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to make sure all occurrences of the value are removed. You’ll learn how to do this in Chapter 7.”

**ORGANIZING A LIST**

“you’ll frequently want to present your information in a particular order.”

Python provides a number of different ways to organize your lists, depending on the situation.

- Sorting a List Permanently with the sort() Method

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
cars.sort(reverse=True)
```

“The cars are now in alphabetical order”

“in reverse-alphabetical order by passing the argument reverse=True to the sort() method”

- Sorting a List Temporarily with the sorted() Function

The sorted() function lets you display your list in a particular order, but doesn’t affect the actual order of the list.

```python
print("\nHere is the sorted list:")
print(sorted(cars))”
```

in alphabetical order, can also accept a reverse=True argument if you want to display a list in reverse-alphabetical order

“Printing a List in Reverse Order” reverse() method

“Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list:”

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)”
```

“The reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same list a second time.”

FINDING THE LENGTH OF A LIST

“ find the length of a list by using the len() function”

Note:
Python counts the items in a list starting with one, so you shouldn’t run into any off-by-one errors when determining the length of a list.”

Avoiding Index Errors When Working with Lists
There’s one type of error that’s common to see when you’re working with lists for the first time. ”

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])

Traceback (most recent call last):
  File "motorcycles.py", line 2, in <module>
    print(motorcycles[3])
          ~~~~~~~~~~~^^^
IndexError: list index out of range
```

“Because of the off-by-one nature of indexing in lists, this error is typical. People think the third item is item number 3, because they start counting at 1. But in Python the third item is number 2, because it starts indexing at 0.”

“Keep in mind that whenever you want to access the last item in a list, you should use the index -1. This will always work, even if your list has changed size since the last time you accessed it:”

CH4:LOOPS FOR LISTS

Looping Through an Entire List
You’ll often want to run through all entries in a list, performing the same task with each item.

Python’s for loop

Here value-by-value in a list

“Then we define a for loop. This line tells Python to pull a name from the list magicians, and associate it with the variable magician. ”

“Python then repeats these last two lines, once for each name in the list.”

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```

“Looping is important because it’s one of the most common ways a computer automates repetitive tasks.”

“Also keep in mind when writing your own for loops that you can choose any name you want for the temporary variable that will be associated with each value in the list. However, it’s helpful to choose a meaningful name that represents a single item from the list. ”

“You can also write as many lines of code as you like in the for loop. Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list. Therefore, you can do as much work as you like with each value in the list.”

Avoiding Indentation Errors
Python uses indentation to determine how a line, or group of lines, is related to the rest of the program.”

“Python’s use of indentation makes code very easy to read. Basically, it uses whitespace to force you to write neatly formatted code with a clear visual structure.”

“few common indentation errors. For example, people sometimes indent lines of code that don’t need to be indented or forget to indent lines that need to be indented.”

Forgetting to Indent
Always indent the line after the for statement in a loop.”

Forgetting to Indent Additional Lines
Sometimes your loop will run without any errors but won’t produce the expected result.

logical error. The syntax is valid Python code, but the code does not produce the desired result because a problem occurs in its logic.”

Indenting Unnecessarily

Indenting Unnecessarily After the Loop

Forgetting the Colon
The colon at the end of a for statement tells Python to interpret the next line as the start of a loop.

**Making Numerical Lists**
Many reasons exist to store a set of numbers. For example, you’ll need to keep track of the positions of each character in a game, and you might want to keep track of a player’s high scores as well.

**Using the range() Function**

Python’s range() function makes it easy to generate a series of numbers.

```python
for value in range(1, 5):
    print(value)
```

“The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide. Because it stops at that second value, the output never contains the end value, which would have been 5 in this case.”

“You can also pass range() only one argument, and it will start the sequence of numbers at 0.”

“If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function.”

“We can also use the range() function to tell Python to skip numbers in a given range. If you pass a third argument to range(), Python uses that value as a step size when generating numbers.”

```python
even_numbers = list(range(2, 11, 2))
print(even_numbers)
```

“You can create almost any set of numbers you want to using the range() function. For example,”

```python
squares = []
for value in range(1, 11):
❶     square = value ** 2
❷     squares.append(square)

print(squares)
```

**List Comprehensions**
The approach described earlier for generating the list squares consisted of using three or four lines of code. A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element. 

1)open a set of square brackets and **define the expression for the values you want to store** in the new list.

2)Then, **write a for loop** to generate the numbers you want to feed into the expression, and close the square brackets.

```python
squares = [value**2 for value in range(1, 11)]
print(squares)
```

“It takes practice to write your own list comprehensions, but you’ll find them worthwhile once you become comfortable creating ordinary lists.”

**Simple Statistics with a List of Numbers**
A few Python functions are helpful when working with lists of numbers. For example, you can easily find the minimum, maximum, and sum of a list of numbers:

```python
>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45
```

WORKING WITH PART OF A LIST

You can also work with a specific group of items in a list, called a slice in Python.
**Slicing a List**
To make a slice, you specify the index of the first and last elements you want to work with. As with the range() function, Python stops one item before the second index you specify.

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

['martina', 'michael', 'florence']
```

Recall that a negative index returns an element a certain distance from the end of a list; therefore, you can output any slice from the end of a list. For example, if we want to output the last three players on the roster, we can use the slice players[-3:]:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

>>> print(players[:5:2])
['charles', 'michael', 'eli']
```

You can include a third value in the brackets indicating a slice. If a third value is included, this tells Python how many items to skip between items in the specified range.

When you’re working with data, you can use slices to process your data in chunks of a specific size.

**COPYING A LIST (da non sottovalutare**

To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]).

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
❶ friend_foods = my_foods[:]

❷ my_foods.append('cannoli')
❸ friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)”

#COMPARE WITH friend_food = my_food (it's not equivalent)

>>> my_food = ['pizza','pasta','cake']
>>> friend_food = my_food
>>> my_food.append('cannoli')
>>> print(friend_food[-1])
cannoli
>>> print(friend_food)
['pizza', 'pasta', 'cake', 'cannoli']

'''RECALL: ACTUALLY THE SECOND CASE ASSIGN THE TWO LABELS (I.E. THE TWO LIST NAMES)
 TO THE SAME DATA'''
```

If we had simply set friend_foods equal to my_foods, we would not produce two separate lists.

This syntax actually tells Python **to associate the new variable friend_foods with the list that is already associated with my_foods, so now both variables point to the same list.** As a result, when we add 'cannoli' to my_foods, it will also appear in friend_foods.

**TUPLES**

Lists work well for storing collections of items that can change throughout the life of a program.

However, sometimes you’ll want to create a list of items that cannot change. Tuples allow you to do just that. Python refers to values that cannot change as immutable, and an immutable list is called a tuple. 

For example, if we have a rectangle that should always be a certain size, we can ensure that its size doesn’t change by putting the dimensions into a tuple:

A tuple looks just like a list, except you use parentheses instead of square brackets. Once you define a tuple, you can access individual elements by using each item’s index, just as you would for a list.

```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions[0]=100 #This raise an error
'''This is beneficial because we want Python to raise an error when a line 
of code tries to change the dimensions of the rectangle.
'''
```

Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable. If you want to define a tuple with one element, you need to include a trailing comma:
my_t = (3,)
It doesn’t often make sense to build a tuple with one element, but this can happen when tuples are generated automatically.

```python
dimensions = (200, 50)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
```

We then associate a new tuple with the variable dimensions, and print the new values. Python doesn’t raise any errors this time, because reassigning a variable is valid.

**STYLING YOUR CODE**

“Writing easy-to-read code helps you keep track of what your programs are doing and helps others understand your code as well.

“Python programmers have agreed on a number of styling conventions to ensure that everyone’s code is structured in roughly the same way.”

The Style Guide: 

“Python Enhancement Proposal (PEP)”

[https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)

“The Python style guide was written with the understanding that code is read more often than it is written. You’ll write your code once”

“start reading it as you begin debugging.”

“Given the choice between writing code that’s easier to write or code that’s easier to read, Python programmers will almost always encourage you to write code that’s easier to read. ”

Indentation
PEP 8 recommends that you use four spaces per indentation level.

Line Length
Many Python programmers recommend that each line should be less than 80 characters.

“PEP 8 also recommends that you limit all of your comments to 72 characters per line,”

“Most editors allow you to set up a visual cue, usually a vertical line on your screen, that shows you where these limits are.”

Appendix B shows you how to configure your text editor so it always inserts four spaces each time you press the TAB key and shows a vertical guideline to help you follow the 79-character limit. **(STILL TO DO)**

Blank Lines
To group parts of your program visually, use blank lines.”

“Blank lines won’t affect how your code runs, but they will affect the readability of your code. The Python interpreter uses horizontal indentation to interpret the meaning of your code, but it disregards vertical spacing.”

**CH5: IF STATEMENTS**

Programming often involves examining a set of conditions and deciding which action to take based on those conditions. Python’s if statement allows you to examine the current state of a program and respond appropriately to that state.

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
❶     if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

**CONDITIONAL TESTS**

At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test. The two states: True OR False

CHECKING FOR EQUALITY

Most conditional tests compare the current value of a variable to a specific value of interest.

```python
car == 'audi'
```

“using a double equal sign (==). This equality operator ”

“Testing for equality is case sensitive in Python.”

```python
car = 'Audi'
car == 'audi'
car.lower() == 'audi'
```

“if case doesn’t matter and instead you just want to test the value of a variable, you can convert the variable’s value to lowercase before doing the comparison:”

“Websites enforce certain rules for the data that users enter in a manner similar to this. For example, a site might use a conditional test like this to ensure that every user has a truly unique username, not just a variation on the capitalization of another person’s username. When someone submits a new username, that new username is converted to lowercase and compared to the lowercase versions of all existing usernames. During this check, a username like 'John' will be rejected if any variation of 'john' is already in use.”

CHECKING FOR INEQUALITY

When you want to determine whether two values are not equal, you can use the inequality operator (!=).

NUMERICAL COMPARISONS

You can include various mathematical comparisons in your conditional statements as well, such as less than, less than or equal to, greater than, and greater than or equal to:

```python
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
```

CHECKING MULTIPLE CONDITIONS

You may want to check multiple conditions at the same time. For example, sometimes you might need two conditions to be True to take an action. Other times, you might be satisfied with just one condition being True. The keywords **and and or** can help you in these situations.

“To check whether two conditions are both True simultaneously, use the keyword and to combine the two conditional tests; if each test passes, the overall expression evaluates to True. If either test fails or if both tests fail, the expression evaluates to False.”

```python
>>> age_0 = 22
>>> age_1 = 18
❶ >>> age_0 >= 21 and age_1 >= 21
False
```

“The keyword or allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass. An or expression fails only when both individual tests fail.”

```python
>>> age_0 = 22
>>> age_1 = 18
❶ >>> age_0 >= 21 or age_1 >= 21
True
❷ >>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
```

CHECKING WHETHER A VALUE IS IN A LIST

“To find out whether a particular value is already in a list, use the keyword in.”

```python
cars = ['audi','porsche','alfa','bmw']

car = 'Audi'
if car.lower() in cars:
    print(f'{car.title()} is available.')
```

“Other times, it’s important to know if a value does not appear in a list. You can use the keyword not in this situation.”

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
```

**BOOLEAN EXPRESSION**

As you learn more about programming, you’ll hear the term Boolean expression at some point. **A Boolean expression is just another name for a conditional test. A Boolean value is either True or False, just like the value of a conditional expression after it has been evaluated.**
Boolean values are often **used to keep track of certain conditions,** such as whether a game is running or whether a user can edit certain content on a website:

```python
game_active = True
can_edit = False
```

Boolean values provide an efficient way to track the state of a program or a particular condition that is important in your program.

**RECAP ABOUT EQUIVALENCE:**

**SIMPLE RULE: YOU CAN EXCHANGE EQUIVALENT CONDITIONS IF YOU CHANGE AND WITH OR AND ADD NOT ON BOTH STATEMENTS AND CHANGE THE ORDER OF THE ACTIONS.**

```python
a = 19
b = 18

if a >= 18 and b >= 18:
	print('You both can enter')
	
#EQUIVALENT TO 

if not a>= 18 or not b >= 18:
else:
	print('You can both enter')
```

**USEFUL FOR REWRITING CONDITIONS IN THE GUARD CLAUSE FORMAT (I.E. MORE CLEAN AND ORDER IN CODE)**

IF STATEMENTS

When you understand conditional tests, you can start writing if statements. Several different kinds of if statements exist, and your choice of which to use depends on the number of conditions you need to test.

**Indentation plays the same role in if statements as it did in for loops. All indented lines after an if statement will be executed if the test passes, and the entire block of indented lines will be ignored if the test does not pass.**

SIMPLE IF STATEMENT

```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
```

The simplest kind of if statement has one test and one action:

IF-ELSE STATEMENTS

Often, you’ll want to take one action when a conditional test passes and a different action in all other cases. Python’s if-else syntax makes this possible.

The if-else structure works well in situations in which you want Python to always execute one of two possible actions.

```python
age = 17
❶ if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
❷ else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

**IF-ELIF-ELSE**

Often, you’ll need to test more than two possible situations, and to evaluate these you can use Python’s if-elif-else syntax. Python executes only one block in an if-elif-else chain. **It runs each conditional test in order, until one passes. When a test passes, the code following that test is executed and Python skips the rest of the tests.**

ORDER/GERARCHY IS IMPORTANT HERE

```python
age = 12
❶ if age < 4:
print("Your admission cost is $0.")
❷ elif age < 18:
print("Your admission cost is $25.")
❸ else:
print("Your admission cost is $40.")
```

**“The elif line ❷ is really another if test, which runs only if the previous test failed.”**

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
```

“Rather than printing the admission price within the if-elif-else block, it would be more concise to set just the price inside the if-elif-else chain and then have a single print() call that runs after the chain has been evaluated:”

**Using Multiple elif Blocks**
You can use as many elif blocks in your code as you like.

**Omitting the else block**

The else block is a catchall statement. It matches any condition that wasn’t matched by a specific if or elif test, and that can sometimes include invalid or even malicious data. If you have a specific final condition you’re testing for, consider using a final elif block and omit the else block. 

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
```

**Testing multiple conditions**

The if-elif-else chain is powerful, but it’s only appropriate to use when you just need one test to pass. 

“However, sometimes it’s important to check all conditions of interest. In this case, you should use a series of simple if statements with no elif or else blocks.”

```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

In summary, if you want only one block of code to run, use an if-elif-else chain. If more than one block of code needs to run, use a series of independent if statements.

**USING IF STATEMENTS WITH LISTS**

You can watch for special values that need to be treated differently than other values in the list.

```python
requested_toppings = ['mushrooms','green pepper','extra cheese']
nomore = ['green pepper','oil']

for req in requested_toppings:
    if req in nomore:
        print(f'\nSorrry we run out of {req.title()}.')
    else:
        print(f'\n{req.title()} was added as a topping.')

print('\n\tYour pizza is ready.')
```

**CHECKING THAT A LIST IS NOT EMPTY**

In this situation, it’s useful to check whether a list is empty before running a for loop.

**When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False.**

```python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

STYLING YOUR IF STATEMENTS

```python
if age < 4:    #OK
if age<4:      #LESS OK
```

“ The only recommendation PEP 8 provides for styling conditional tests is to use a single space around comparison operators, such as ==, >=, and <=.”

**CH6: DICTIONARIES**

Understanding dictionaries allows you to model a variety of real-world objects more accurately. You’ll be able to create a dictionary representing a person and then store as much information as you want about that person.

“You’ll be able to store any two kinds of information that can be **matched up**”

AS FEATURES OF AN OBJECTS

```python
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
```

“This simple dictionary stores information about a particular alien:”

“wrapped in braces ({}) with a series of key-value pairs inside the braces”

“A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary.”

ACCESSING VALUES IN A DICTIONARY

```python
alien_0 = {'color': 'green'}
print(alien_0['color'])
```

ADDING NEW KEY-VALUE PAIRS

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

“Because screen coordinates usually start at the upper-left corner of the screen, we’ll place the alien on the left edge of the screen by setting the x-coordinate to 0 and 25 pixels from the top by setting its y-coordinate to positive 25, as shown here”

“Dictionaries retain the order in which they were defined. 

STARTING WITH AN EMPTY DICTIONARY

“It’s sometimes convenient, or even necessary, to start with an empty dictionary and then add each new item to it.”

```python
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
```

“Typically, you’ll use empty dictionaries when storing user-supplied data in a dictionary or when writing code that generates a large number of key-value pairs automatically.”

MODIFY VALUES IN A DICTIONARY

**Basically just overwrite.**

“To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key.”

```python
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
```

“For a more interesting example, let’s track the position of an alien that can move at different speeds. We’ll store a value representing the alien’s current speed and then use it to determine how far to the right the alien should move:”

```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
❶ if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
❷ alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")
```

“This technique is pretty cool: by changing one value in the alien’s dictionary, you can change the overall behavior of the alien. For example, to turn this medium-speed alien into a fast alien, you would add this line:”

```python
alien_0['speed'] = 'fast'
```

“The if-elif-else block would then assign a larger value to x_increment the next time the code runs.”

REMOVING THE KEY-PAIR 

“When you no longer need a piece of information that’s stored in a dictionary, you can use the del statement to completely remove a key-value pair. All del needs is the name of the dictionary and the key that you want to remove.”

```python
del alien_0['points']
print(alien_0)”
```

A DICTIONARY OF SIMILAR OBJECTS (STORE ONE FEATURES FOR DIFFERENT OBJECTS)

“The previous example involved storing different kinds of information about one object, an alien in a game. You can also use a dictionary to store one kind of information about many objects.”

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
```

“When you know you’ll need more than one line to define a dictionary, press ENTER after the opening brace. Then indent the next line one level (four spaces) and write the first key-value pair, followed by a comma. From this point forward when you press ENTER, your text editor should automatically indent all subsequent key-value pairs to match the first key-value pair.”

USING get() TO ACCESS VALUES

Using keys in square brackets to retrieve the value you’re interested in from a dictionary might cause one potential problem: if the key you ask for doesn’t exist, you’ll get an error.

```python
“Traceback (most recent call last):
  File "alien_no_points.py", line 2, in <module>
    print(alien_0['points'])
          ~~~~~~~^^^^^^^^^^
KeyError: 'points”
```

For dictionaries specifically, you can use the get() method to set a default value that will be returned if the requested key doesn’t exist.
**The get() method requires** a key as a first argument. **As a second optional argument, you can pass the value to be returned if the key doesn’t exist:”**

```python
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
```

If there’s a chance the key you’re asking for might not exist, consider using the get() method instead of the square bracket notation.

**If you leave out the second argument in the call to get() and the key doesn’t exist, Python will return the value None. The special value None means “no value exists.” This is not an error: it’s a special value meant to indicate the absence of a value. You’ll see more uses for None in Chapter 8.**

**LOOPING THROUGH A DICTIONARY**

“ You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values.”

LOOPING THROUGH KEY-VALUE PAIRS

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

**method items(),** which returns a sequence of key-value pairs. The for loop then assigns each of these pairs to the two variables provided.”

LOOPING THROUGH AL THE KEYS IN A DICTIONARY

“The keys() method is useful when you don’t need to work with all of the values in a dictionary.”

“Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output if you wrote:”

```python
for name in favorite_languages:

#EQUIVALENT

for name in favorite_languages.keys():
```

```python
favorite_languages = {
    --snip--
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

❶     if name in friends:
❷         language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
```

You can also use the keys() method to find out if a particular person was polled. This time, let’s find out if Erin took the poll:

```python
favorite_languages = {
    --snip--
    }

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!
```

LOOPING INTO DICTIONARY KEY IN A PARTICULAR ORDER

Looping through a dictionary returns the items in the same order they were inserted. Sometimes, though, you’ll want to loop through a dictionary in a different order.
You can use the sorted() function to get a copy of the keys in order:

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

LOOPING THROUGH ALL VALUES IN A DICTIONARY

If you are primarily interested in the values that a dictionary contains, you can use the values() method to return a sequence of values without any keys. 

```python
print("The following languages have been mentioned:")
for language in favorite_languages.values():
print(language.title())
```

To see each language chosen without repetition, we can use a set. **A set is a collection in which each item must be unique:**

```python
favorite_languages = {
    --snip--
    }

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
```

“Here we use set() to pull out the unique languages in favorite_languages.values().
The result is a nonrepetitive list of languages that have been mentioned by people taking the poll:”

Note:
You can build a set directly using braces and separating the elements with commas:

“It’s easy to mistake sets for dictionaries because they’re both wrapped in braces. When you see braces but no key-value pairs, you’re probably looking at a set. Unlike lists and dictionaries, sets do not retain items in any specific order.”

```python
>>> languages = {'python', 'rust', 'python', 'c'}
>>> languages
{'rust', 'python', 'c'}
```

**NESTING**

Sometimes you’ll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary. This is called nesting. You can nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary. Nesting is a powerful feature, as the following examples will demonstrate.

A LIST OF DICTIONARY

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

❶ aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```

or 

```python
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range (30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
```

It’s common to store a number of dictionaries in a list when each dictionary contains many kinds of information about one object. For example, you might create a dictionary for each user on a website, as we did in [user.py](http://user.py/) on page 99, and store the individual dictionaries in a list called users. 

A DICTIONARY OF LISTS

“Rather than putting a dictionary inside a list, it’s sometimes useful to put a list inside a dictionary. ”

“You can nest a list inside a dictionary anytime you want more than one value to be associated with a single key in a dictionary.”

```python
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
❶ print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

❷ for topping in pizza['toppings']:
    print(f"\t{topping}")
```

```python
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

❶ for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
❷     for language in languages:
        print(f"\t{language.title()}")
```

Note
You should not nest lists and dictionaries too deeply. If you’re nesting items much deeper than what you see in the preceding examples, or if you’re working with someone else’s code with significant levels of nesting, there’s most likely a simpler way to solve the problem.

A DICTIONARY OF DICTIONARIES

“You can nest a dictionary inside another dictionary, but your code can get complicated quickly when you do. ”

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }

❶ for username, user_info in users.items():
❷     print(f"\nUsername: {username}")
❸     full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

❹     print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

**CH7: USER INPUTS AND WHILE LOOPS**

“To do so, you usually need to get some information from the user.”

“You’ll also learn how to keep programs running as long as users want them to, so they can enter as much information as they need to; then, your program can work with that information. You’ll use Python’s while loop to keep programs running as long as certain conditions remain true.”

“The input() function pauses your program and waits for the user to enter some text. Once Python receives the user’s input, it assigns that input to a variable to make it convenient for you to work with.”

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

“**The input() function takes one argument: the prompt** that we want to display to the user, so they know what kind of information to enter.”

“ The program waits while the user enters their response and continues after the user presses ENTER.”

“you should include a clear, easy-to-follow prompt that tells the user exactly what kind of information you’re looking for.”

```python
“prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")”
```

**Using int() to Accept Numerical Input**
When you use the **input() function**, Python interprets everything the user enters **as a string**.

We can resolve this issue by using the **int() function**, which converts the input string to a numerical value.”

```python
“>>> age = input("How old are you? ")
How old are you? 21
❶ >>> age = int(age)
>>> age >= 18
```

**The Modulo Operator**
A useful tool for working with numerical information is the modulo operator (%), which divides one number by another number and returns the remainder:

The modulo operator doesn’t tell you how many times one number fits into another; it only tells you what the remainder is.
When one number is divisible by another number, the remainder is 0, so the modulo operator always returns 0. You can use this fact to determine if a number is even or odd:

```python
“number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")”

Passi di
Python Crash Course, 3rd Edition
Eric Matthes
Il materiale potrebbe essere protetto da copyright.
```

**INTRODUCING WHILE LOOPS**

**“The for loop takes a collection of items and executes a block of code once for each item in the collection. In contrast, the while loop runs as long as, or while, a certain condition is true.”**

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

The programs you use every day most likely contain while loops. For example, a game needs a while loop to keep running as long as you want to keep playing, and so it can stop running as soon as you ask it to quit. Programs wouldn’t be fun to use if they stopped running before we told them to or kept running even after we wanted to quit, so while loops are quite useful.

**LETTING THE PLAYER CHOOSE WHEN TO QUIT**

“We can make the [parrot.py](http://parrot.py/) program run as long as the user wants by putting most of the program inside a while loop. We’ll define a quit value and then keep the program running as long as the user has not entered the quit value:”

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
```

**USING A FLAG**

If many possible events might occur to stop the program, trying to test all these conditions in one while statement becomes complicated and difficult.
For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False. **As a result, our overall while statement needs to check only one condition: whether the flag is currently True. Then, all our other tests (to see if an event has occurred that should set the flag to False) can be neatly organized in the rest of the program.**

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
❶ while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
```

**the logic is taken care of in other parts of the program.**

now that we have a flag to indicate whether the overall program is in an active state, **it would be easy to add more tests (such as elif statements) for events that should cause active to become False.** This is useful in complicated programs like games, in which there may be many events that should each make the program stop running. When any of these events causes the active flag to become False, the main game loop will exit, a Game Over message can be displayed, and the player can be given the option to play again.

USING BREAKS TO EXIT A LOOP

**To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement.** The break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren’t, so the program only executes code that you want it to, when you want it to.

```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

❶ while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```

**A loop that starts with while True ❶ will run forever unless it reaches a break statement.** The loop in this program continues asking the user to enter the names of cities they’ve been to until they enter 'quit'. When they enter 'quit', the break statement runs, causing Python to exit the loop.

**“You can use the break statement in any of Python’s loops. For example, you could use break to quit a for loop that’s working through a list or a dictionary.”**

**USING continue in a loop**

```python
current_number = 0
while current_number < 10:
	current_number += 1
  if current_number % 2 == 0:
     continue

  print(current_number)
```

“**Rather than breaking out of a loop entirely** without executing the rest of its code, you can use the continue statement to return to the beginning of the loop, based on the result of a conditional test.”

“If the modulo is 0 (which means current_number is divisible by 2), the continue statement tells Python to ignore the rest of the loop and return to the beginning.”

**i.e. con break esci proprio dal while loop, con continue esci dal singolo run del loop**

**Continue —> to next loop run**

**AVOIDING INFINITE LOOPS**

Every while loop needs a way to stop running so it won’t continue to run forever.

```python
# This loop runs forever!
x = 1
while x <= 5:
    print(x)
```

Every programmer accidentally writes an infinite while loop from time to time, especially when a program’s loops have subtle exit conditions. **If your program gets stuck in an infinite loop, press CTRL-C or just close the terminal window displaying your program’s output.**
To avoid writing infinite loops, test every while loop and make sure the loop stops when you expect it to.

**VS Code, like many editors, displays output in an embedded terminal window. To cancel an infinite loop, make sure you click in the output area of the editor before pressing CTRL-C.**

**USING A WHILE LOOP WITH LISTS AND DICTIONARIES**

“But to keep track of many users and pieces of information, we’ll need to use lists and dictionaries with our while loops.
**A for loop is effective for looping through a list, but you shouldn’t modify a list inside a for loop because Python will have trouble keeping track of the items in the list. To modify a list as you work through it, use a while loop.”**

MOVING ITEMS FROM ONE LIST TO ANOTHER

```python
# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
❶ unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
❷ while unconfirmed_users:
❸     current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
❹     confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

recall: while unconfirmed_users —> means when the list is not empty

REMOVING ALL INSTANCES OF A SPECIFIC VALUE FROM A LIST

“Say you have a list of pets with the value 'cat' repeated several times. To remove all instances of that value, you can run a while loop until 'cat' is no longer in the list”

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)
```

FILLING A DICTIONARY WITH USER INPUT

“You can prompt for as much input as you need in each pass through a while loop. Let’s make a polling program in which each pass through the loop prompts for the participant’s name and response. **We’ll store the data we gather in a dictionary, because we want to connect each response with a particular user:”**

```python
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
❶     name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
❷     responses[name] = response

    # Find out if anyone else is going to take the poll.
❸     repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
❹ for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
```

**CH8:FUNCTIONS**

“named blocks of code designed to do one specific job.”

“**you call the function responsible for it. ”**

“You’ll learn how to write certain functions whose primary job is to display information and other functions designed to process data and return a value or set of values. Finally, you’ll learn to **store functions in separate files called modules** to help organize your main program files.
DEFINE A FUNCTION

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```

“Any indented lines that follow def greet_user(): make up the body of the function. **The text on the second line is a comment called a docstring, which describes what the function does.** ”

“When you want to use this function, you have to call it. A function call tells Python to execute the code in the function. To call a function, you write the name of the function, followed by any necessary information in parentheses. ”

PASSING INFORMATION TO A FUNCTION

```python
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
```

ARGUMENTS AND PARAMETERS

“The variable username in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do its job. The value 'jesse' in greet_user('jesse') is an example of an argument.”

“the value was assigned to the parameter username.”

“People sometimes speak of arguments and parameters interchangeably. Don’t be surprised if you see the variables in a function definition referred to as arguments or the variables in a function call referred to as parameters.”

PASSING ARGUMENTS

“Because a function definition can have multiple parameters, a function call may need multiple arguments. You can pass arguments to your functions in a number of ways. You can use **positional arguments**, which need to be in the same order the parameters were written; **keyword arguments**, where each argument consists of a variable name and a value; and **lists and dictionaries of values**. ”

**Positional Arguments**
When you call a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to do this is based on the order of the arguments provided. Values matched up this way are called positional arguments.”

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'igor')
```

“Calling a function multiple times is a very efficient way to work. The code describing a pet is written once in the function. Then, anytime you want to describe a new pet, you call the function with the new pet’s information.”

**order matters in positional arguments!**

**KEYWORD ARGUMENTS**

**A keyword argument is a name-value pair that you pass to a function.** You **directly associate the name and the value within the argument**, so when you pass the argument to the function, there’s **no confusion** (you won’t end up with a harry named Hamster). Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.”

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```

The function describe_pet() hasn’t changed. But when we call the function, we explicitly tell Python which parameter each argument should be matched with. 
**The order of keyword arguments doesn’t matter because Python knows where each value should go.** The following two function calls are equivalent.

**! Note
When you use keyword arguments, be sure to use the exact names of the parameters in the function’s definition.**

DEFAULT VALUES

“When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value.”

```python
def describe_pet(pet_name, animal_type='dog'):
"""Display information about a pet."""
print(f"\nI have a {animal_type}.")
print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
```

**!Note
When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly.**

“It doesn’t really matter which calling style you use. As long as your function calls produce the output you want, just use the style you find easiest to understand.”

AVOIDING ARGUMENTS ERRORS

“Unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work.”

```python
describe_pet()
```

Traceback (most recent call last):
❶   File "[pets.py](http://pets.py/)", line 6, in <module>
❷     describe_pet()
^^^^^^^^^^^^^^
❸ TypeError: describe_pet() missing 2 required positional arguments:
'animal_type' and 'pet_name”

“The traceback first tells us the location of the problem ❶, allowing us to look back and see that something went wrong in our function call. Next, the offending function call is written out for us to see ❷. Last, the traceback tells us the call is missing two arguments and reports the names of the missing arguments ❸. **If this function were in a separate file, we could probably rewrite the call correctly without having to open that file and read the function code.**

“This is another motivation for giving your variables and functions descriptive names. If you do, Python’s error messages will be more useful to you and anyone else who might use your code.”

**RETURN VALUES**

**“A function doesn’t always have to display its output directly. Instead, it can process some data and then return a value or set of values. The value the function returns is called a return value. The return statement takes a value from inside a function and sends it back to the line that called the function. Return values allow you to move much of your program’s grunt work into functions, which can simplify the body of your program.”**

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
❶     full_name = f"{first_name} {last_name}"
❷     return full_name.title()

❸ musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

**When you call a function that returns a value, you need to provide a variable that the return value can be assigned to.**

**Making an Argument Optional**
Sometimes it makes sense to make an argument optional, so that people using the function can choose to provide extra information only if they want to. You can use default values to make an argument optional.

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
❶     if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
❷     else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

❸ musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```

Recall: Python interprets non-empty strings as True

RETURNING A DICTIONARY
A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries.

You can easily extend this function to accept optional values like a middle name, an age, an occupation, or any other information you want to store about a person.

```python
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```

“You can think of None as a placeholder value.”

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

PASSING A LIST

“When you pass a list to a function, the function gets direct access to the contents of the list.”

```python
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

MODIFYING A LIST IN A FUNCTION

“When you pass a list to a function, the function can modify the list. **Any changes made to the list inside the function’s body are permanent,** allowing you to work efficiently even when you’re dealing with large amounts of data.”

“We can reorganize this code by writing two functions, each of which does one specific job. Most of the code won’t change; we’re just structuring it more carefully. ”

```python
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

“This program has the same output as the version without functions, but the code is much more organized. ”

“This program is easier to extend and maintain than the version without functions.”

**“This example also demonstrates the idea that every function should have one specific job. The first function prints each design, and the second displays the completed models. This is more beneficial than using one function to do both jobs. If you’re writing a function and notice the function is doing too many different tasks, try to split the code into two functions. Remember that you can always call a function from another function, which can be helpful when splitting a complex task into a series of steps.”**

PREVENTING MODIFYING LIST IN A FUNCTION

“ You may decide that even though you’ve printed all the designs, you want to keep the original list of unprinted designs for your records. But because you moved all the design names out of unprinted_designs, the list is now empty, and the empty list is the only version you have; the original is gone. In this case, you can address this issue by passing the function a copy of the list, not the original. ”

```python
function_name(list_name[:])
```

**“The slice notation [:] makes a copy of the list to send to the function.”**

“The function print_models() can do its work because it still receives the names of all unprinted designs. But this time it uses a copy of the original unprinted designs list, not the actual unprinted_designs list. The list completed_models will fill up with the names of printed models like it did before, but the original list of unprinted designs will be unaffected by the function.
Even though you can preserve the contents of a list by passing a copy of it to your functions, you should pass the original list to functions unless you have a specific reason to pass a copy. It’s more efficient for a function to work with an existing list, because this avoids using the time and memory needed to make a separate copy. ”

PASSING AN ARBITRARY NUMBER OF ARGUMENTS

“ The function in the following example has one parameter, *toppings, but this parameter collects as many arguments as the calling line provides:”

“The asterisk in the parameter name *toppings tells Python to make a tuple called toppings, containing all the values this function receives.”

“Note that Python packs the arguments into a tuple, even if the function receives only one value:”

```python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

Mixing Positional and Arbitrary Arguments
If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.”

```python
def make_pizza(size, *toppings)
```

**!Note
You’ll often see the generic parameter name *args, which collects arbitrary positional arguments like this.**

ARBITRARY KEYWORD ARGUMENTS

Sometimes you’ll want to accept an arbitrary number of arguments, but **you won’t know ahead of time what kind of information will be passed to the function. In this case, you can write functions that accept as many key-value pairs** as the calling statement provides.

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
	  user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
```

**!Note
You’ll often see the parameter name **kwargs used to collect nonspecific keyword arguments.”**

**STORING YOUR FUNCTIONS IN MODULES**

One advantage of functions is the way they separate blocks of code from your main program. When you use descriptive names for your functions, your programs become much easier to follow. **You can go a step further by storing your functions in a separate file called a module and then importing that module into your main program. An import statement tells Python to make the code in a module available in the currently running program file.**
**Storing your functions in a separate file allows you to hide the details of your program’s code and focus on its higher-level logic. It also allows you to reuse functions in many different programs.** 

“Knowing how to import functions also allows you to use libraries of functions that other programmers have written.
There are several ways to import a module”

**HOW TO IMPORT A MODULE**

IMPORT AN ENTIRE MODULE

**A module is a file ending in .py that contains the code you want to import into your program.** 

same directory for the two files

```python
pizza.py
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

making_pizzas.py
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

When Python reads this file, the line **import pizza** tells Python to open the file [pizza.py](http://pizza.py/) and copy all the functions from it into this program. All you need to know is that any function defined in [pizza.py](http://pizza.py/) will now be available in making_pizzas.py.

```python
#WORKING AND IMPORTING MODULE
import module
module.make_pizza('pepperoni')
module.make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

**To call a function from an imported module, enter the name of the module you imported, pizza, followed by the name of the function, make_pizza(), separated by a dot ❶. This code produces the same output as the original program that didn’t import a module.**

IMPORTING SPECIFIC FUNCTIONS

**You can import as many functions as you want from a module by separating each function’s name with a comma:**

```python
from module_name import function_0, function_1, function_2
```

**“With this syntax, you don’t need to use the dot notation when you call a function. Because we’ve explicitly imported the function make_pizza() in the import statement, we can call it by name when we use the function.”**

USING AS TO GIVE A FUNCTION AN ALIAS

“f the name of a function you’re importing might conflict with an existing name in your program, or if the function name is long, you can use a short, unique alias—an alternate name similar to a nickname for the function.”

```python
from module_name import function_0 as alias
```

USING AS TO GIVE A MODULE AN ALIAS

“You can also provide an alias for a module name. Giving a module a short alias, like p for pizza, allows you to call the module’s functions more quickly. Calling p.make_pizza() is more concise than calling pizza.make_pizza():”

```python
import pizza as p

p.make_pizza(16, 'pepperoni')
```

IMPORTING EVERY FUNCTION IN A MODULE

**You can tell Python to import every function in a module by using the asterisk (*) operator:**

```python
from pizza import *

make_pizza(16, 'pepperoni')
```

“The asterisk in the import statement tells Python to copy every function from the module pizza into this program file. Because every function is imported, you can call each function by name without using the dot notation. ”

“**The best approach is to import the function or functions you want, or import the entire module and use the dot notation.”**

STYLING FUNCTIONS

“You need to keep a few details in mind when you’re styling functions. Functions should have descriptive names, and these names should use lowercase letters and underscores. Descriptive names help you and others understand what your code is trying to do. Module names should use these conventions as well.
Every function should have a comment that explains concisely what the function does. This comment should appear immediately after the function definition and use the docstring format. In a well-documented function, other programmers can use the function by reading only the description in the docstring. 
If you specify a default value for a parameter, no spaces should be used on either side of the equal sign:

```python
def function_name(parameter_0, parameter_1='default value')
```

The same convention should be used for keyword arguments in function calls:

```python
function_name(value_0, parameter_1='value')
```

RECAP

```python
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
```

**“Functions also make your code easier to test and debug. When the bulk of your program’s work is done by a set of functions, each of which has a specific job, it’s much easier to test and maintain the code you’ve written. You can write a separate program that calls each function and tests whether each function works in all the situations it may encounter. When you do this, you can be confident that your functions will work properly each time you call them.”**

CH9: CLASSES

**Object-oriented programming (OOP) is one of the most effective approaches to writing software. In object-oriented programming, you write classes that represent real-world things and situations, and you create objects based on these classes. When you write a class, you define the general behavior that a whole category of objects can have.**

**When you create individual objects from the class, each object is automatically equipped with the general behavior; you can then give each object whatever unique traits you desire. You’ll be amazed how well real-world situations can be modeled with object-oriented programming.
Making an object from a class is called instantiation, and you work with instances of a class.** 

**you’ll write classes and create instances of those classes. You’ll specify the kind of information that can be stored in instances, and you’ll define actions that can be taken with these instances.**

You’ll also write classes that extend the functionality of existing classes, so similar classes can share common functionality, and you can do more with less code. You’ll store your classes in modules and import classes written by other programmers into your own program files.
**Learning about object-oriented programming will help you see the world as a programmer does.** It’ll help you understand your code—not just what’s happening line by line, but also the bigger concepts behind it. Knowing the logic behind classes will train you to think logically, so you can write programs that effectively address almost any problem you encounter.

CREATING AND USING A CLASS

**!!!!You can model almost anything using classes.** 

Let’s start by writing a simple class, Dog, that represents a dog—not one dog in particular, but any dog. **What do we know about most pet dogs?** Well, they all have a name and an age. We also know that most dogs sit and roll over. Those two pieces of information (name and age) and those two behaviors (sit and roll over) **will go in our Dog class because they’re common to most dogs. This class will tell Python how to make an object representing a dog. After our class is written, we’ll use it to make individual instances, each of which represents one specific dog.**

CREATING THE DOG CLASS

```python
dog.py
class Dog:
    """A simple attempt to model a dog."""

❷     def __init__(self, name, age):
        """Initialize name and age attributes."""
         self.name = name
	       self.age = age

❹     def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

	    def roll_over(self):
	        """Simulate rolling over in response to a command."""
	        print(f"{self.name} rolled over!")
```

“ By convention, capitalized names refer to classes in Python. There are no parentheses in the class definition because we’re creating this class from scratch. We then write a docstring describing what this class does.”

**DOCKSTRING:**

**"""Initialize attributes to describe a dog""”**

The **init**() Method —> Initialize
**A function that’s part of a class is a method.** 

Everything you learned about functions applies to methods as well; **the only practical difference for now is the way we’ll call methods.** **The init() method ❷ is a special method that Python runs automatically whenever we create a new instance based on the Dog class.**

“We define the **init**() method to have three parameters: self, name, and age. The self parameter is required in the method definition, and it must come first, before the other parameters. It must be included in the definition because when Python calls this method later (to create an instance of Dog), the method call will automatically pass the self argument. **Every method call associated with an instance automatically passes self, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class.** When we make an instance of Dog, Python will call the **init**() method from the Dog class. We’ll pass Dog() a name and an age as arguments; self is passed automatically, so we don’t need to pass it. Whenever we want to make an instance from the Dog class, we’ll provide values for only the last two parameters, name and age.”

**The two variables defined in the body of the init() method each have the prefix self ❸. Any variable prefixed with self is available to every method in the class, and we’ll also be able to access these variables through any instance created from the class.** The line [self.name](http://self.name/) = name takes the value associated with the parameter name and assigns it to the variable name, which is then attached to the instance being created. The same process happens with self.age = age. **Variables that are accessible through instances like this are called attributes.**

The Dog class has two other methods defined: sit() and roll_over() ❹. Because these methods don’t need additional information to run, we just define them to have one parameter, self. The instances we create later will have access to these methods. In other words, they’ll be able to sit and roll over. 

MAKING AN INSTANCE FROM A CLASS

**Think of a class as a set of instructions for how to make an instance. The Dog class is a set of instructions that tells Python how to make individual instances representing specific dogs.**

```python
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```

When Python reads this line, it calls the **init**() method in Dog with the arguments 'Willie' and 6. **The init() method creates an instance representing this particular dog** and sets the name and age attributes using the values we provided. **Python then returns an instance representing this dog.** We assign that instance to the variable my_dog. The naming convention is helpful here; we can usually assume that a capitalized name like Dog refers to a class, and a lowercase name like my_dog refers to a single instance created from a class.

ACCESSING ATTRIBUTES

“To access the attributes of an instance, you use dot notation. ”

```python
my_dog.name
```

CALLING METHODS

“After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog.”

```python
my_dog.sit()
```

“To call a method, give the name of the instance (in this case, my_dog) and the method you want to call, separated by a dot. When Python reads my_dog.sit(), it looks for the method sit() in the class Dog and runs that code.”

You can make as many instances from one class as you need, as long as you give each instance a unique variable name or it occupies a unique spot in a list or dictionary.

WORKING WITH CLASSES AND INSTANCES

Once you write a class, you’ll spend most of your time working with instances created from that class. One of the first tasks you’ll want to do is **modify the attributes associated with a particular instance.** You can modify the attributes of an instance directly or write methods that update attributes in specific ways.

SETTING A DEFAULT VALUE FOR AN ATTRIBUTE

```python
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
    
my_car = Car('Audi','A4', 2025)
print(f'My car infos:\n{my_car.get_descriptive_name()}')
my_car.read_odometer()
```

“When an instance is created, attributes can be defined without being passed in as parameters. These attributes can be defined in the **init**() method, where they are assigned a default value.”

MODIFYING ATTRIBUTE METHODS

You can change an attribute’s value in three ways: you can change the value directly through an instance, set the value through a method, or increment the value (add a certain amount to it) through a method. Let’s look at each of these approaches.

MODIFYING AN ATTRIBUTE VALUE DIRECTLY

The simplest way to modify the value of an attribute is to access the attribute directly through an instance. Here we set the odometer reading to 23 directly:

```python
my_new_car.odometer_reading = 23
```

We use dot notation to access the car’s odometer_reading attribute, and set its value directly.

Sometimes you’ll want to access attributes directly like this, but **other times you’ll want to write a method that updates the value for you.**

MODIFYING AN ATTRIBUTE VALUE THROUGH A METHOD

It can be helpful to have methods that update certain attributes for you. **Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.**

“Sometimes you’ll want to increment an attribute’s value by a certain amount, rather than set an entirely new value. ”

```python

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
```

**RECAP:**

**-self —> itself the instance of the wannabe object**

### 🔹 `self`

- Refers to **the instance** of the class (i.e., the specific object you're working with).
- Always the **first parameter** in **instance methods (i.e. the ones with self as first parameter vs non-instance methods)**
- Used to access attributes and methods that belong to **that specific object**.

**-attributes —> setted via __init __       self.attribute**

### 🔹 Attributes

- **Variables** tied to a specific object (instance).
- Created in `__init__()` using `self.attribute_name = value`.

**-methods —> functions defined in the class     self.method()**

### 🔹 Methods

- **Functions** defined inside a class.
- Operate on the object via `self`.
- You call them using: `object.method()`

INHERITANCE

**You don’t always have to start from scratch when writing a class. If the class you’re writing is a specialized version of another class you wrote, you can use inheritance. When one class inherits from another, it takes on the attributes and methods of the first class. The original class is called the parent class, and the new class is the child class. The child class can inherit any or all of the attributes and methods of its parent class, but it’s also free to define new attributes and methods of its own.**

“When you’re writing a new class based on an existing class, you’ll often want to call the **init**() method from the parent class. This will initialize any attributes that were defined in the parent **init**() method and make them available in the child class.”

```python
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

❸     def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
❹         super().__init__(make, model, year)

❺ my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
```

**When you create a child class, the parent class must be part of the current file and must appear before the child class in the file.** We then define the child class, ElectricCar ❷. T**he name of the parent class must be included in parentheses in the definition of a child class. The init() method takes in the information required to make a Car instance ❸.
The super() function ❹ is a special function that allows you to call a method from the parent class. This line tells Python to call the init() method from Car, which gives an ElectricCar instance all the attributes defined in that method.** The name super comes from a convention of calling the parent class a superclass and the child class a subclass.

```python
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)        #This is the inherit part concerning attributes
        self.battery_size = 40
    
    def describe_battery(self):
        """Print the battery status of the electric car."""
        print(f'The current battery is {self.battery_size} KWH.')
```

OVERRIDING METHODS FROM THE PARENT CLASS

**You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class. To do this, you define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the parent class method and only pay attention to the method you define in the child class.**

Say the class Car had a method called fill_gas_tank(). This method is meaningless for an all-electric vehicle, so you might want to override this method.

```python
class ElectricCar(Car):
    --snip--

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")
```

Now if someone tries to call fill_gas_tank() with an electric car, Python will ignore the method fill_gas_tank() in Car and run this code instead. When you use inheritance, you can make your child classes retain what you need and override anything you don’t need from the parent class.

INSTANCES AS ATTRIBUTES

you might recognize that part of one class can be written as a separate class. **You can break your large class into smaller classes that work together; this approach is called composition.**
For example, if we continue adding detail to the ElectricCar class, we might notice that we’re adding many attributes and methods specific to the car’s battery. When we see this happening, we can stop and move those attributes and methods to a separate class called Battery. Then we can use a Battery instance as an attribute in the ElectricCar class:

```python
class Car:
    --snip--

class Battery:
    """A simple attempt to model a battery for an electric car."""

❶     def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size   

❷     def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
❸         self.battery = Battery()         **#HERE WE USE AN INSTANCE AS AN ATTRIBUTE**

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
```

“This looks like a lot of extra work, but now we can describe the battery in as much detail as we want without cluttering the ElectricCar class.”

MODELING REAL-WORLD OBJECTS

**When you wrestle with questions like these, you’re thinking at a higher logical level rather than a syntax-focused level. You’re thinking not about Python, but about how to represent the real world in code. When you reach this point, you’ll realize there are often no right or wrong approaches to modeling real-world situations. Some approaches are more efficient than others, but it takes practice to find the most efficient representations. If your code is working as you want it to, you’re doing well!** 

IMPORTING CLASSES

To help, Python lets you store classes in modules and then import the classes you need into your main program.
IMPORTING A SINGLE CLASS

```python
from mulewithclass import Car
from mulewithclass import Car, ElectricCar
```

STORING MULTIPLE CLASSES IN A MODULE

IMPORTING AN ENTIRE MODULE

**You can also import an entire module and then access the classes you need using dot notation. This approach is simple and results in code that is easy to read.**

```python
import car

my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
```

IMPORTING ALL CLASSES FROM A MODULE

```python
from module import *
```

This method is not recommended.

IMPORT A MODULE IN A MODULE

Sometimes you’ll want to spread out your classes over several modules to keep any one file from growing too large and avoid storing unrelated classes in the same module. When you store your classes in several modules, you may find that a class in one module depends on a class in another module. When this happens, you can import the required class into the first module.

```python
"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery:
    --snip--

class ElectricCar(Car):
    --snip--
```

**“The class ElectricCar needs access to its parent class Car, so we import Car directly into the module. ”**

USING ALIASES

As you saw in Chapter 8, aliases can be quite helpful when using modules to organize your projects’ code. You can use aliases when importing classes as well.

You can also give a module an alias. 

```python
from electric_car import ElectricCar as EC
import electric_car as ec
```

When you’re starting out, keep your code structure simple. Try doing everything in one file and moving your classes to separate modules once everything is working. If you like how modules and files interact, try storing your classes in modules when you start a project. Find an approach that lets you write code that works, and go from there.

THE PYTHON STANDARD LIBRARY

The Python standard library is a set of modules included with every Python installation. Now that you have a basic understanding of how functions and classes work, you can start to use modules like these that other programmers have written. You can use any function or class in the standard library by including a simple import statement at the top of your file. **Let’s look at one module, random, which can be useful in modeling many real-world situations.
One interesting function from the random module is randint(). This function takes two integer arguments and returns a randomly selected integer between (and including) those numbers.**

```python
from random import randint
dice = randint(1,6)
```

Another useful function is choice(). This function takes in a list or tuple and returns a randomly chosen element:

```python
>>> from random import choice
>>> players = ['charles', 'martina', 'michael', 'florence', 'eli']
>>> first_up = choice(players)
>>> first_up
'florence”
```

STYLING CLASSES

**Class names should be written in CamelCase. To do this, capitalize the first letter of each word in the name, and don’t use underscores.** Instance and module names should be written in lowercase, with underscores between words.
Every class should have a docstring immediately following the class definition. 

Within a class you can use one blank line between methods, and within a module you can use two blank lines to separate classes.

If you need to import a module from the standard library and a module that you wrote, place the import statement for the standard library module first. Then add a blank line and the import statement for the module you wrote. In programs with multiple import statements, this convention makes it easier to see where the different modules used in the program come from.

CH10: FILES AND EXCEPTIONS

**You’ll learn to handle errors so your programs don’t crash when they encounter unexpected situations. You’ll learn about exceptions, which are special objects Python creates to manage errors that arise while a program is running. You’ll also learn about the json module, which allows you to save user data so it isn’t lost when your program stops running.**

People will be able to run your program, do some work, and then close the program and pick up where they left off.

READING FROM A FILE

An incredible amount of data is available in text files. Reading from a file is particularly useful in data analysis applications, but it’s also applicable to any situation in which you want to analyze or modify information stored in a file. 
When you want to work with the information in a text file, the first step is to read the file into memory. You can then work through all of the file’s contents at once or work through the contents line by line.

```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)
```

To work with the contents of a file, we need to tell Python the path to the file. **A path is the exact location of a file or folder on a system.** Python provides a module called pathlib that makes it easier to work with files and directories, no matter which operating system you or your program’s users are working with. A module that provides specific functionality like this is often called a library, hence the name pathlib.
**We start by importing the Path class from pathlib. There’s a lot you can do with a Path object that points to a file. For example, you can check that the file exists before working with it, read the file’s contents, or write new data to the file.** Here, we build a Path object representing the file pi_digits.txt, which we assign to the variable path ❶. **Since this file is saved in the same directory as the .py file we’re writing, the filename is all that Path needs to access the file.”**

**!NOTE**

**VS Code looks for files in the folder that was most recently opened. press CTRL-O (⌘-O on macOS), and open that folder.**

“Once we have a Path object representing pi_digits.txt, we use the read_text() method to read the entire contents of the file ❷. The contents of the file are returned as a single string, which we assign to the variable contents.”

“The only difference between this output and the original file is the extra blank line at the end of the output. The blank line appears because read_text() returns an empty string when it reaches the end of the file; this empty string shows up as a blank line.
We can remove the extra blank line by using rstrip() on the contents”

“This approach is called method chaining, and you’ll see it used often in programming.”

RELATIVE AND ABSOLUTE FILE PATH

When you pass a simple filename like pi_digits.txt to Path, Python looks in the directory where the file that’s currently being executed (that is, your .py program file) is stored.
Sometimes, depending on how you organize your work, **the file you want to open won’t be in the same directory as your program file.** For example, you might store your program files in a folder called python_work; inside python_work, you might have another folder called text_files to distinguish your program files from the text files they’re manipulating. Even though text_files is in python_work, just passing Path the name of a file in text_files won’t work, because Python will only look in python_work and stop there; it won’t go on and look in text_files. To get Python to open files from a directory other than the one where your program file is stored, you need to provide the correct path.
**There are two main ways to specify paths in programming. A relative file path tells Python to look for a given location relative to the directory where the currently running program file is stored.** Since text_files is inside python_work, we need to build a path that starts with the directory text_files, and ends with the filename. 

```python
path = Path('text_files/filename.txt')
```

**You can also tell Python exactly where the file is on your computer, regardless of where the program that’s being executed is stored. This is called an absolute file path.** 

```python
path = Path('/home/eric/data_files/text_files/filename.txt')
```

**Using absolute paths, you can read files from any location on your system.**

NOTE: 

“Windows systems use a backslash (\) instead of a forward slash (/) when displaying file paths, but you should use forward slashes in your code, even on Windows. The pathlib library will automatically use the correct representation of the path when it interacts with your system, or any user’s system.”

ACCESSING A FILE LINE

When you’re working with a file, you’ll often want to examine each line of the file. You might be looking for certain information in the file, or you might want to modify the text in the file in some way. For example, you might want to read through a file of weather data and work with any line that includes the word sunny in the description of that day’s weather. In a news report, you might look for any line with the tag <headline> and rewrite that line with a specific kind of formatting.
You can use the splitlines() method to turn a long string into a set of lines, and then use a for loop to examine each line from a file, one at a time.

```python
from pathlib import Path

path = Path('pi_digits.txt')
❶ contents = path.read_text()      #A single string

❷ lines = contents.splitlines()      #A list of strings
for line in lines:
    print(line)
```

WORKING WITH FILE CONTENT

After you’ve read the contents of a file into memory, you can do whatever you want with that data, so let’s briefly explore the digits of pi. ”

```python
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))
```

**When Python reads from a text file, it interprets all text in the file as a string.** If you read in a number and want to work with that value in a numerical context, you’ll have to convert it to an integer using the int() function or a float using the float() function.”

LARGE FILE ONE MILLION DIGITS

Python has no inherent limit to how much data you can work with; you can work with as much data as your system’s memory can handle.

WRITING TO A FILE

**One of the simplest ways to save data is to write it to a file.** When you write text to a file, the output will still be available after you close the terminal containing your program’s output.

WRITING A SINGLE LINE

**Once you have a path defined, you can write to a file using the write_text() method.** 

```python
from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming.")
```

NOTE: 

**Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.**

WRITING MULTIPLES LINES

To write more than one line to a file, **you need to build a string containing the entire contents of the file, and then call write_text() with that string.**

```python
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)
```

There’s no limit to the length of your strings, and **this is how many computer-generated documents are created.**

**!NOTE:**

**Be careful when calling write_text() on a path object. If the file already exists, write_text() will erase the current contents of the file and write new contents to the file. Later in this chapter, you’ll learn to check whether a file exists using pathlib.**

EXCEPTIONS

**Python uses special objects called exceptions to manage errors that arise during a program’s execution. Whenever an error occurs that makes Python unsure of what to do next, it creates an exception object. If you write code that handles the exception, the program will continue running.** If you don’t handle the exception, the program will halt and show a traceback, which includes a report of the exception that was raised.
**Exceptions are handled with try-except blocks. A try-except block asks Python to do something, but it also tells Python what to do if an exception is raised.** When you use try-except blocks, your programs will continue running even if things start to go wrong. Instead of tracebacks, which can be confusing for users to read, users will see friendly error messages that you’ve written.

HANDLING THE ZeroDivisionError Exception

```python
Traceback (most recent call last):
  File "division_calculator.py", line 1, in <module>
    print(5/0)
          ~^~
❶ ZeroDivisionError: division by zero
```

The error reported in the traceback, ZeroDivisionError, is an exception object ❶. Python creates this kind of object in response to a situation where it can’t do what we ask it to. When this happens, Python stops the program and tells us the kind of exception that was raised. We can use this information to modify our program. 

USING TRY-EXCEPT BLOCKS

When you think an error may occur, you can **write a try-except block to handle the exception that might be raised. You tell Python to try running some code, and you tell it what to do if the code results in a particular kind of exception.**

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

**If the code in the try block causes an error, Python looks for an except block whose error matches the one that was raised, and runs the code in that block.**

“In this example, the code in the try block produces a ZeroDivisionError, so Python looks for an except block telling it how to respond. ”

It’s bad that the program crashed, but it’s also not a good idea to let users see tracebacks. Nontechnical users will be confused by them, and in a malicious setting, attackers will learn more than you want them to. For example, they’ll know the name of your program file, and they’ll see a part of your code that isn’t working properly. A skilled attacker can sometimes use this information to determine which kind of attacks to use against your code.

“**We can make this program more error resistant by wrapping the line that might produce errors in a try-except block. The error occurs on the line that performs the division, so that’s where we’ll put the try-except block. This example also includes an else block. Any code that depends on the try block executing successfully goes in the else block:”**

```python
print("Give me two numbers, and I'll divide them.")
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
        print(answer)
```

“We ask Python to try to complete the division operation in a try block ❶, which includes only the code that might cause an error. 

**The only code that should go in a try block is code that might cause an exception to be raised. Sometimes you’ll have additional code that should run only if the try block was successful; this code goes in the else block. The except block tells Python what to do in case a certain exception arises when it tries to run the code in the try block.**
By anticipating likely sources of errors, you can write robust programs that continue to run even when they encounter invalid data and missing resources. Your code will be resistant to innocent user mistakes and malicious attacks.”

HANDLING THE FileNotFoundError

```python
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
```

**The encoding argument is needed when your system’s default encoding doesn’t match the encoding of the file that’s being read.** This is most likely to happen when reading from a file that wasn’t created on your system.

ANALYZING TEXT

```python
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
```

WORKING WITH MULTIPLE FILES

```python
from pathlib import Path
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
    count_words(path)
```

Using the try-except block in this example provides two significant advantages. We prevent our users from seeing a traceback, and we let the program continue analyzing the texts it’s able to find. **If we don’t catch the FileNotFoundError that siddhartha.txt raises, the user would see a full traceback, and the program would stop running after trying to analyze Siddhartha. It would never analyze Moby Dick or Little Women.**

FAILING SILENTLY with pass

But you don’t need to report every exception you catch. **Sometimes, you’ll want the program to fail silently when an exception occurs and continue on as if nothing happened. To make a program fail silently, you write a try block as usual, but you explicitly tell Python to do nothing in the except block. Python has a pass statement that tells it to do nothing in a block.**

```python
def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        --snip--
    except FileNotFoundError:
        pass
    else:
        --snip--
```

The pass statement also acts as a placeholder. It’s a reminder that you’re choosing to do nothing at a specific point in your program’s execution and that you might want to do something there later. For example, in this program we might decide to write any missing filenames to a file called missing_files.txt. Our users wouldn’t see this file, but we’d be able to read the file and deal with any missing texts.

Python’s error-handling structures give you fine-grained control over how much to share with users when things go wrong; it’s up to you to decide how much information to share.

STORING DATA

Whatever the focus of your program is, you’ll store the information users provide in data structures such as lists and dictionaries. When users close a program, you’ll almost always want to save the information they entered. A simple way to do this involves storing your data using the json module.
**The json module allows you to convert simple Python data structures into JSON-formatted strings, and then load the data from that file the next time the program runs. You can also use json to share data between different Python programs. Even better, the JSON data format is not specific to Python, so you can share data you store in the JSON format with people who work in many other programming languages. It’s a useful and portable format, and it’s easy to learn.**

The JSON (JavaScript Object Notation) format was originally developed for JavaScript. However, it has since become a common format used by many languages, including Python.

**USING json.dumps() and jason.loads()**

Let’s write a short program that stores a set of numbers and another program that reads these numbers back into memory. The first program will use json.dumps() to store the set of numbers, and the second program will use json.loads().
**The json.dumps() function takes one argument: a piece of data that should be converted to the JSON format. The function returns a string, which we can then write to a data file.**

```python
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
```

**“It’s customary to use the file extension .json to indicate that the data in the file is stored in the JSON format.”**

“Now we’ll write a separate program that uses json.loads() to read the list back into memory:”

```python
from pathlib import Path
import json
path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
```

**“This function takes in a JSON-formatted string and returns a Python object (in this case, a list), which we assign to numbers.”**

SAVING AND READING USER-GENERATED DATA

“Saving data with json is useful when you’re working with user-generated data, because if you don’t store your user’s information somehow, you’ll lose it when the program stops running.

```python
#To store

from pathlib import Path
import json

❶ username = input("What is your name? ")

❷ path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

❸ print(f"We'll remember you when you come back, {username}!")

#To retrieve

from pathlib import Path
import json

❶ path = Path('username.json')
contents = path.read_text()
❷ username = json.loads(contents)

print(f"Welcome back, {username}!")
```

There are many helpful methods you can use with Path objects. The **exists() method returns True if a file or folder exists** and False if it doesn’t.

```python
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
    print(f"We'll remember you when you come back, {username}!")
```

**REFACTORING**

**Often, you’ll come to a point where your code will work, but you’ll recognize that you could improve the code by breaking it up into a series of functions that have specific jobs. This process is called refactoring.**

```python

from pathlib import Path
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

greet_user()
```

**If the path that’s passed to get_stored_username() doesn’t exist, the function returns None ❷. This is good practice: a function should either return the value you’re expecting, or it should return None.** This allows us to perform a simple test with the return value of the function. 

**This compartmentalization of work is an essential part of writing clear code that will be easy to maintain and extend.**

**RECALL: json.dumps() and json.loads()**

TESTING YOUR CODE

When you write a function or a class, you can also write tests for that code. **Testing proves that your code works as it’s supposed to in response to all the kinds of input it’s designed to receive.**

**The pytest library is a collection of tools that will help you write your first tests quickly and simply**, while supporting your tests as they grow in complexity along with your projects. Python doesn’t include pytest by default, so you’ll learn to install external libraries. Knowing how to install external libraries will make a wide variety of well-designed code available to you. These libraries will expand the kinds of projects you can work on immensely.
You’ll learn to build a series of tests and check that each set of inputs results in the output you want. You’ll see what a passing test looks like and what a failing test looks like, and you’ll learn how a failing test can help you improve your code. You’ll learn to test functions and classes, and you’ll start to understand how many tests to write for a project.

**A third-party package is a library that’s developed outside the core Python language.**

UPDATING pip

**Python includes a tool called pip that’s used to install third-party packages.** Because pip helps install packages from external resources, it’s updated often to address potential security issues. So, we’ll start by updating pip.

```bash
python -m pip install --upgrade pip
```

python -m pip, tells Python to run the module pip. The second part, install --upgrade, tells pip to update a package that’s already been installed. The last part, pip, specifies which third-party package should be updated.

**more in general:**

```bash
python -m pip install --upgrade package_name
```

INSTALL pytest

```bash
python -m pip install --user pytest
```

We’re still using the core command pip install, without the --upgrade flag this time. Instead, we’re using the --user flag, which tells Python to install this package for the current user.

**More in general to install a third-party package:**

```bash
python -m pip install --user package_name
```

Note: 

If you have any difficulty running this command, try running the same command without the --user flag.

TESTING A FUNCTION

But say we want to modify get_formatted_name() so it can also handle middle names. **As we do so, we want to make sure we don’t break the way the function handles names that have only a first and last name.** We could test our code by running [names.py](http://names.py/) and entering a name like Janis Joplin every time we modify get_formatted_name(), but that would become tedious. **Fortunately, pytest provides an efficient way to automate the testing of a function’s output. If we automate the testing of get_formatted_name(), we can always be confident that the function will work when given the kinds of names we’ve written tests for.**

UNIT TESTS AND TEST CASES

There is a wide variety of approaches to testing software. One of the simplest kinds of test is a unit test. **A unit test verifies that one specific aspect of a function’s behavior is correct. A test case is a collection of unit tests that together prove that a function behaves as it’s supposed to, within the full range of situations you expect it to handle.**
**A good test case considers all the possible kinds of input a function could receive and includes tests to represent each of these situations. A test case with full coverage includes a full range of unit tests covering all the possible ways you can use a function.** Achieving full coverage on a large project can be daunting. **It’s often good enough to write tests for your code’s critical behaviors** and then aim for full coverage only if the project starts to see widespread use.

**With pytest, writing your first unit test is pretty straightforward. We’ll write a single test function. The test function will call the function we’re testing, and we’ll make an assertion about the value that’s returned. If our assertion is correct, the test will pass; if the assertion is incorrect, the test will fail.**

```python
from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
```

Before we run the test, let’s take a closer look at this function. **The name of a test file is important; it must start with test_. When we ask pytest to run the tests we’ve written, it will look for any file that begins with test_, and run all of the tests it finds in that file.**
In the test file, we first import the function that we want to test: get_formatted_name(). **Then we define a test function:** in this case, test_first_last_name() ❶. **This is a longer function name than we’ve been using, for a good reason. First, test functions need to start with the word test, followed by an underscore. Any function that starts with test_ will be discovered by pytest, and will be run as part of the testing process.**
Also, test names should be longer and **more descriptive than a typical function name. You’ll never call the function yourself; pytest will find the function and run it for you.** Test function names should be long enough that if you see the function name in a test report, you’ll have a good sense of what behavior was being tested.

**Next, we call the function we’re testing** ❷. Here we call get_formatted_name() with the arguments 'janis' and 'joplin', just like we used when we ran [names.py](http://names.py/). **We assign the return value of this function to formatted_name.
Finally, we make an assertion ❸. An assertion is a claim about a condition.** Here we’re claiming that the value of formatted_name should be 'Janis Joplin'.

RUNNING A TEST

If you run the file test_name_function.py directly, you won’t get any output because we never called the test function. **Instead, we’ll have pytest run the test file for us.
To do this, open a terminal window and navigate to the folder that contains the test file.** If you’re using VS Code, you can open the folder containing the test file and use the terminal that’s embedded in the editor window. **In the terminal window, enter the command pytest.**

```bash
pytest
========================= test session starts =========================
❶ platform darwin -- Python 3.x.x, pytest-7.x.x, pluggy-1.x.x
❷ rootdir: /.../python_work/chapter_11
❸ collected 1 item

❹ test_name_function.py .                                          [100%]
========================== 1 passed in 0.00s ==========================
```

Let’s try to make sense of this output. First of all, we see some information about the system the test is running on ❶. I’m testing this on a macOS system, so you may see some different output here. **Most importantly, we can see which versions of Python, pytest, and other packages are being used to run the test.**
Next, we see the **directory where the test is being run from** ❷: in my case, python_work/chapter_11. We can see that **pytest found one test to run ❸, and we can see the test file that’s being run** ❹. **The single dot after the name of the file tells us that a single test passed, and the 100% makes it clear that all of the tests have been run.** A large project can have hundreds or thousands of tests, and the dots and percentage-complete indicator can be helpful in monitoring the overall progress of the test run.
**The last line tells us that one test passed, and it took less than 0.01 seconds to run the test.**
This output indicates that the function get_formatted_name() will always work for names that have a first and last name, unless we modify the function. 

When we modify get_formatted_name(), we can run this test again. If the test passes, we know the function will still work for names like Janis Joplin.

!**Note
If you’re not sure how to navigate to the right location in the terminal, see “Running Python Programs from a Terminal” on page 11.** Also, if you see a message that the pytest command was not found, use the command python -m pytest instead.

A FAILING TEST

This version should work for people with middle names, but when we test it, we see that we’ve broken the function for people with just a first and last name.

```bash
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()
```

The unit test is:

```python
from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
```

This time running pytest we get the following input

```bash
pytest
========================= test session starts =========================
--snip--
❶ test_name_function.py F                                          [100%]
❷ ============================== FAILURES ===============================
❸ ________________________ test_first_last_name _________________________
    def test_first_last_name():
        """Do names like 'Janis Joplin' work?"""
❹ >       formatted_name = get_formatted_name('janis', 'joplin')
❺ E       TypeError: get_formatted_name() missing 1 required positional
            argument: 'last'

test_name_function.py:5: TypeError
======================= short test summary info =======================
FAILED test_name_function.py::test_first_last_name - TypeError:
    get_formatted_name() missing 1 required positional argument: 'last'
========================== 1 failed in 0.04s ==========================
```

The first item of note in the output is **a single F ❶, which tells us that one test failed.** We then see a section that focuses on FAILURES ❷, because failed tests are usually the most important thing to focus on in a test run. **Next, we see that test_first_last_name() was the test function that failed ❸. An angle bracket ❹ indicates the line of code that caused the test to fail. The E on the next line ❺ shows the actual error that caused the failure: a TypeError due to a missing required positional argument, last.** The most important information is repeated in a shorter summary at the end, so when you’re running many tests, you can get a quick sense of which tests failed and why.

RESPONDING TO A TEST FAIL

What do you do when a test fails? Assuming you’re checking the right conditions, a passing test means the function is behaving correctly and a failing test means there’s an error in the new code you wrote. So when a test fails, don’t change the test. If you do, your tests might pass, but any code that calls your function like the test does will suddenly stop working. Instead, **fix the code that’s causing the test to fail.** Examine the changes you just made to the function, and figure out how those changes broke the desired behavior.

This is ideal; it means the function works for names like Janis Joplin again, without us having to test the function manually. Fixing our function was easier because the failed test helped us identify how the new code broke existing behavior.

ADDING NEW TESTS

Now that we know get_formatted_name() works for simple names again, let’s write a second test for people who include a middle name. **We do this by adding another test function to the file test_name_function.py**

```python
def test_first_last_middle_name():
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
```

We name this new function test_first_last_middle_name(). **The function name must start with test_ so the function runs automatically when we run pytest. We name the function to make it clear which behavior of get_formatted_name() we**’re testing.

output:

```bash
pytest
========================= test session starts =========================
--snip--
collected 2 items

❶ test_name_function.py ..                                         [100%]
========================== 2 passed in 0.01s ==========================
```

The two dots ❶ indicate that two tests passed, which is also clear from the last line of output. This is great! We now know that the function still works for names like Janis Joplin, and we can be confident that it will work for names like Wolfgang Amadeus Mozart as well.

TESTING A CLASS

In the first part of this chapter, you wrote tests for a single function. **Now you’ll write tests for a class.** You’ll use classes in many of your own programs, so it’s helpful to be able to prove that your classes work correctly. If you have passing tests for a class you’re working on, you can be confident that improvements you make to the class won’t accidentally break its current behavior.

A VARIETY OF ASSERTIONS

So far, you’ve seen just one kind of assertion: a claim that a string has a specific value. **When writing a test, you can make any claim that can be expressed as a conditional statement. If the condition is True as expected, your assumption about how that part of your program behaves will be confirmed; you can be confident that no errors exist.** If the condition you assume is True is actually False, the test will fail and you’ll know there’s an issue to resolve. **Table 11-1 shows some of the most useful kinds of assertions you can include in your initial tests.**

Table 11-1: Commonly Used Assertion Statements in Tests

Assertion
Claim

assert a == b
Assert that two values are equal.

assert a != b
Assert that two values are not equal.

assert a
Assert that a evaluates to True.

assert not a
Assert that a evaluates to False.

assert element in list
Assert that an element is in a list.

assert element not in list
Assert that an element is not in a list.

A CLASS TO TEST

**Testing a class is similar to testing a function, because much of the work involves testing the behavior of the methods in the class. However, there are a few differences**, so let’s write a class to test. 

```python
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
```

Once you have an instance representing a particular survey, you display the survey question with show_question(), store a response using store_response(), and show results with show_results().

```python
from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()
```

Implementing such changes would risk affecting the current behavior of the class AnonymousSurvey. For example, it’s possible that while trying to allow each user to enter multiple responses, we could accidentally change how single responses are handled. To ensure we don’t break existing behavior as we develop this module, we can write tests for the class.

TESTING THE AnonymusSurvey class

```python
# test_survey.py
from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English') 
    assert 'English' in language_survey.responses
```

To test the behavior of a class, we need to make an instance of the class. We create an instance called language_survey ❷ with the question "What language did you first learn to speak?" We store a single response, English, using the store_response() method. Then we verify that the response was stored correctly by asserting that English is in the list language_survey.responses ❸.

**If this test fails, we’ll know from the function name in the test summary that there was a problem storing a single response to the survey.**

**By default, running the command pytest with no arguments will run all the tests that pytest discovers in the current directory. To focus on the tests in one file, pass the name of the test file you want to run.** 

```bash
pytest test_survey.py
```

Let’s verify that three responses can be stored correctly. To do this, we **add another method (unit test) to TestAnonymousSurvey**:

```python
from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English') 
    assert 'English' in language_survey.responses

def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
```

We call the new function test_store_three_responses(). We create a survey object just like we did in test_store_single_response(). We define a list containing three different responses ❶, and then we call store_response() for each of these responses. Once the responses have been stored, we write another loop and assert that each response is now in language_survey.responses ❷.

USING FIXTURES

these tests are a bit repetitive, so we’ll use another feature of pytest to make them more efficient.

In test_survey.py, we created a new instance of AnonymousSurvey in each test function. This is fine in the short example we’re working with, but in a real-world project with tens or hundreds of tests, this would be problematic.
**In testing, a fixture helps set up a test environment. Often, this means creating a resource that’s used by more than one test. We create a fixture in pytest by writing a function with the decorator @pytest.fixture. A decorator is a directive placed just before a function definition; Python applies this directive to the function before it runs, to alter how the function code behaves.** Don’t worry if this sounds complicated; you can start to use decorators from third-party packages before learning to write them yourself.
Let’s use a fixture to create a single survey instance that can be used in both test functions in test_survey.py:

```python
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
```

Notice that the definitions of both test functions have changed ❸ ❺; **each test function now has a parameter called language_survey. When a parameter in a test function matches the name of a function with the @pytest.fixture decorator, the fixture will be run automatically and the return value will be passed to the test function.** In this example, the function language_survey() supplies both test_store_single_response() and test_store_three_responses() with a language_survey instance.

You don’t need to use fixtures right away; it’s better to write tests that have a lot of repetitive code than to write no tests at all. Just know that when you’ve written enough tests that the repetition is getting in the way, there’s a well-established way to deal with the repetition.

**When you want to write a fixture, write a function that generates the resource that’s used by multiple test functions. Add the @pytest.fixture decorator to the new function, and add the name of this function as a parameter for each test function that uses this resource.** Your tests will be shorter and easier to write and maintain from that point forward.

e.g.

```python
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
```

```python
# test_Employee.py
from CH11 import Employee
import pytest

@pytest.fixture
def emp():
    """Create Instance for other tests."""
    emp = Employee('Mario','Rossi',10000)
    return emp

def test_give_default_rise(emp):
    emp.give_raise()
    assert emp.salary == 15000

def test_give_custom_rise(emp):
    emp.give_raise(10000)
    assert emp.salary == 20000
```

You don’t have to write tests for all the simple projects you try as a new programmer. But as soon as you start to work on projects that involve significant development effort, you should test the critical behaviors of your functions and classes. You’ll be more confident that new work on your project won’t break the parts that work, and **this will give you the freedom to make improvements to your code. If you accidentally break existing functionality, you’ll know right away, so you can still fix the problem easily. Responding to a failed test that you ran is much easier than responding to a bug report from an unhappy user.**

**Write tests for the most critical behaviors of your functions and classes, but don’t aim for full coverage in early projects unless you have a specific reason to do so.**

**Part II
Projects**

**Congratulations! You now know enough about Python to start building interactive and meaningful projects. Creating your own projects will teach you new skills and solidify your understanding of the concepts introduced in Part I.
Part II contains three kinds of projects, and you can choose to do any or all of these projects in whichever order you like. Here’s a brief description of each project to help you decide which to dig into first.**

**Alien Invasion: Making a Game with Python**
In the Alien Invasion project (Chapters 12, 13, and 14), you’ll use the Pygame package to develop a 2D game. The goal of the game is to shoot down a fleet of aliens as they drop down the screen, in levels that increase in speed and difficulty. At the end of the project, you’ll have learned skills that will enable you **to develop your own 2D games in Pygame.**

**Data Visualization**
The Data Visualization projects start in Chapter 15, where you’ll learn to generate data and create a series of functional and beautiful visualizations of that data using Matplotlib and Plotly. Chapter 16 teaches you to access data from online sources and feed it into a visualization package to create plots of weather data and a map of global earthquake activity. Finally, Chapter 17 shows you how to write a program to automatically download and visualize data. **Learning to make visualizations allows you to explore the field of data science,** which is one of the highest-demand areas of programming today.

**Web Applications**
In the Web Application project (Chapters 18, 19, and 20), you’ll use the Django package to create a simple web application that allows users to keep a journal about different topics they’ve been learning about. Users will create an account with a username and password, enter a topic, and then make entries about what they’re learning. You’ll also deploy your app to a remote server so anyone in the world can access it.
After completing this project, **you’ll be able to start building your own simple web applications, and you’ll be ready to delve into more thorough resources on building applications with Django.**