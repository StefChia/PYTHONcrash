# Project 2: Data visualization, analysis and API

**CH15**

“Data visualization is the use of visual representations to explore and present patterns in datasets. It’s closely associated with data analysis, which uses code to explore the patterns and connections in a dataset. ”

“Data scientists have written an impressive array of visualization and analysis tools in Python, many of which are available to you as well. One of the most popular tools is Matplotlib, a mathematical plotting library.”

“We’ll also use a package called Plotly, which creates visualizations that work well on digital devices, to analyze the results of rolling dice. Plotly generates visualizations that automatically resize to fit a variety of display devices. These visualizations can also include a number of interactive features, such as emphasizing particular aspects of the dataset when users hover over different parts of the visualization. Learning to use Matplotlib and Plotly will help you get started visualizing the kinds of data you’re most interested in.”

```bash
$ python -m pip install --user matplotlib
```

To make a simple line graph, specify the numbers you want to work with and let Matplotlib do the rest:

```python
import matplotlib.pyplot as plt

#SIMPLE PLOTS
squares = [i**2 for i in range(1,6)]

fig, ax = plt.subplots()
ax.plot(squares,linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()
```

This function can generate one or more plots in the same figure. **The variable fig represents the entire figure, which is the collection of plots that are generated. The variable ax represents a single plot in the figure; this is the variable we’ll use most of the time when defining and customizing a single plot.**
We then use the plot() method, which tries to plot the data it’s given in a meaningful way. The function plt.show() opens Matplotlib’s viewer and displays the plot, as shown in Figure 15-1. The viewer allows you to zoom and navigate the plot, and you can save any plot images you like by clicking the disk icon.”

Fortunately, Matplotlib allows you to adjust every feature of a visualization.

Now that we can read the chart better, we can see that the data is not plotted correctly. Notice at the end of the graph that the square of 4.0 is shown as 25! Let’s fix that.
**When you give plot() a single sequence of numbers, it assumes the first data point corresponds to an x-value of 0, but our first point corresponds to an x-value of 1. We can override the default behavior by giving plot() both the input and output values used to calculate the squares:”**

“Now plot() doesn’t have to make any assumptions about how the output numbers were generated. ”

“You can specify a number of arguments when calling plot() and use a number of methods to customize your plots after generating them.”

USING BUILT-IN STYLES

“To see the full list of available styles, run the following lines in a terminal session:

> import matplotlib.pyplot as plt
plt.style.available
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery',”
> 

Passi di
Python Crash Course, 3rd Edition
Eric Matthes
Il materiale potrebbe essere protetto da copyright.

“To use any of these styles, add one line of code before calling subplots():”

```python
plt.style.use('dark_background')
fig, ax = plt.subplots()
```

PLOTTING AND STYLING INDIVIDUAL PLOTS WITH scatter()

**Sometimes, it’s useful to plot and style individual points based on certain characteristics.** For example, you might plot small values in one color and larger values in a different color. You could also plot a large dataset with one set of styling options and then emphasize individual points by replotting them with different options.
**To plot a single point, pass the single x- and y-values of the point to scatter():**

```python
#SCATTER SQUARE
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)
plt.show()
```

“We call scatter() and use the s argument to set the size of the dots used to draw the graph”

PLOTTING A SERIES OF POINTS WITH scatter()

```python
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)
```

“The x_values list contains the numbers to be squared, and y_values contains the square of each number. When these lists are passed to scatter(), Matplotlib reads one value from each list as it plots each point. The points to be plotted are (1, 1), (2, 4), (3, 9), (4, 16), and (5, 25)”

**RECAP**

**ax.plot()—>linea continua**

**ax.scatter()—> singoli punti/osservazioni**

CALCULATING DATA AUTOMATICALLY

“Writing lists by hand can be inefficient, especially when we have many points. Rather than writing out each value, **let’s use a loop to do the calculations for us.**”

```python
#CALCULATING DATA AUTOMATICALLY

x_values = range(1,1001)
y_values = [i**2 for i in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values,y_values, s=10)

ax.set_title('title',fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Squared value', fontsize = 14)
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])

plt.show()
```

“**We start with a range of x-values containing the numbers 1 through 1,000 ❶. Next, a list comprehension generates the y-values by looping through the x-values (for x in x_values), squaring each number (x**2), and assigning the results to y_values.** We then pass the input and output lists to scatter()”

“**The axis() method requires four values**: the minimum and maximum values for the x-axis and the y-axis. Here, we run the x-axis from 0 to 1,100 and the y-axis from 0 to 1,100,000.”

CUSTOMIZING TICKLABELS

“When the numbers on an axis get large enough, Matplotlib defaults to scientific notation for tick labels.”

“Almost every element of a chart is customizable, so you can tell Matplotlib to keep using plain notation if you prefer:”

```python
ax.ticklabel_format(style='plain')
```

DEFINING CUSTOM COLORS

“To change the color of the points, pass the argument color to scatter() with the name of a color to use in quotation marks, as shown here:”

“You can also define custom colors using the RGB color model. ”

“using values between 0 and 1.”

“Values closer to 0 produce darker colors, and values closer to 1 produce lighter colors.”

```python
ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)
```

USING A COLORMAP

**A colormap is a sequence of colors in a gradient that moves from a starting to an ending color.** In visualizations, colormaps are used to emphasize patterns in data. For example, **you might make low values a light color and high values a darker color.** Using a colormap ensures that all points in the visualization vary smoothly and accurately along a well-designed color scale.
**The pyplot module includes a set of built-in colormaps.** **To use one of these colormaps, you need to specify how pyplot should assign a color to each point in the dataset**. Here’s how to assign a color to each point, based on its y-value:

```python
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
```

**The c argument is similar to color, but it’s used to associate a sequence of values with a color mapping. We pass the list of y-values to c, and then tell pyplot which colormap to use with the cmap argument. This code colors the points with lower y-values light blue and the points with higher y-values dark blue.** 

!IT’S similar to conditional formatting

!It works only for plt.scatter() not with plt.plot()

“You can see all the colormaps available in pyplot at [https://matplotlib.org](https://matplotlib.org/).”

SAVINGS PLOTS AUTOMATICALLY

**If you want to save the plot to a file instead of showing it in the Matplotlib viewer, you can use plt.savefig() instead of plt.show():**

```python
plt.savefig('squares_plot.png', bbox_inches='tight')
```

**The first argument is a filename for the plot image, which will be saved in the same directory as scatter_squares.py. The second argument trims extra whitespace from the plot. If you want the extra whitespace around the plot, you can omit this argument. You can also call savefig() with a Path object, and write the output file anywhere you want on your system.**

```python
path = Path('/Users/stefanochiapparini/Desktop/PYTHON/PYTHONcrash/projects/P3')
plt.savefig(path/'image_squares',bbox_inches = 'tight')
```

RANDOM WALKS

In this section, we’ll use Python to generate data for a random walk and then use Matplotlib to create a visually appealing representation of that data. A random walk is a path that’s determined by a series of simple decisions, each of which is left entirely to chance. You might imagine a random walk as the path a confused ant would take if it took every step in a random direction.
Random walks have practical applications in nature, physics, biology, chemistry, and economics.”

CREATING THE RandomWalk Class

**To create a random walk, we’ll create a RandomWalk class, which will make random decisions about which direction the walk should take. The class needs three attributes: one variable to track the number of points in the walk, and two lists to store the x- and y-coordinates of each point in the walk.
We’ll only need two methods for the RandomWalk class: the init() method and fill_walk(), which will calculate the points in the walk.**

```python
from random import choice

class RandomWalk:
    """Model a RW behavior"""
    def __init__(self, num_points=5000):
        """Initialize attributes of the class."""
        self.num_points = num_points
        
        #All walks starts at (0,0)
        self.x_values = [0]
        self.y_values = [0]
```

**To make random decisions, we’ll store possible moves in a list and use the choice() function (from the random module) to decide which move to make each time a step is taken.**

We’ll use the fill_walk() method to determine the full sequence of points in the walk.

```python
def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go, and how far to go.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
```

```python

from random_walk import RandomWalk
import matplotlib.pyplot as plt

#Make a Random Walk
rw = RandomWalk()
rw.fill_walk()

#plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values,rw.y_values,s=15)
ax.set_aspect('equal')

plt.show()
```

By default, Matplotlib scales each axis independently. But that approach would stretch most walks out horizontally or vertically. Here we use the set_aspect() method to specify that both axes should have equal spacing between tick marks.

GENERATE MULTIPLE RANDOM WALKS

Every random walk is different, and it’s fun to explore the various patterns that can be generated. One way to use the preceding code to make multiple walks without having to run the program several times is to wrap it in a while loop, like this:

“

```python
while True:
    #Make a Random Walk
    rw = RandomWalk()
    rw.fill_walk()

    #plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values,rw.y_values,s=15)
    ax.set_aspect('equal')

    plt.show()
    
    keep_running = input('Create another rw? (yes/no) ')
    if keep_running.lower() == 'no':
        break

```

“This code generates a random walk, displays it in Matplotlib’s viewer, and pauses with the viewer open. **When you close the viewer, you’ll be asked whether you want to generate another walk.** If you generate a few walks, you should see some that stay near the starting point, some that wander off mostly in one direction, some that have thin sections connecting larger groups of points, and many other kinds of walks. When you want to end the program, press N.”

STYLING THE WALK

we identify the characteristics we want to emphasize, such as **where the walk began, where it ended, and the path taken**. Next, we identify the characteristics to deemphasize, such as tick marks and labels. The result should be a simple visual representation that clearly communicates the path taken in each random walk.

We’ll use a colormap to show the order of the points in the walk, and remove the black outline from each dot so the color of the dots will be clearer. **To color the points according to their position in the walk, we pass the c argument a list containing the position of each point.** Because the points are plotted in order, this list just contains the numbers from 0 to 4,999.

edgecolors='none' to get rid of the black outline around each point. The result is a plot that varies from light to dark blue, showing exactly how the walk moves from its starting point to its ending point.

```python
while True:
    #Make a Random Walk
    rw = RandomWalk()
    rw.fill_walk()

    #plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='None', s=15)
    ax.set_aspect('equal')

    plt.show()
    
    keep_running = input('Create another rw? (yes/no) ')
    if keep_running.lower() == 'no':
        break
```

PLOTTING THE STARTING AND END POINTS

In addition to coloring points to show their position along the walk, **it would be useful to see exactly where each walk begins and ends. To do so, we can plot the first and last points individually after the main series has been plotted. We’ll make the end points larger and color them differently** to make them stand out.

```python
# Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
```

“Make sure you insert this code just before the call to plt.show() so the starting and ending points are drawn on top of all the other points.”

CLEANING UP THE AXES

“Let’s remove the axes in this plot so they don’t distract from the path of each walk.”

```python
# Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
```

ADDING PLOT POINTS

ALTERING THE SIZE TO FILL THE SCREEN

To make the plotting window better fit your screen, you can adjust the size of Matplotlib’s output. This is done in the subplots() call:

```python
fig, ax = plt.subplots(figsize = (15,9))
```

**When creating a plot, you can pass subplots() a figsize argument, which sets the size of the figure. The figsize parameter takes a tuple that tells Matplotlib the dimensions of the plotting window in inches.**

ROLLING DICE WITH PLOTLY

**Plotly to produce interactive visualizations. Plotly is particularly useful when you’re creating visualizations that will be displayed in a browser, because the visualizations will scale automatically to fit the viewer’s screen. These visualizations are also interactive; when the user hovers over certain elements on the screen, information about those elements is highlighted.**

**Plotly Express**, a subset of Plotly that focuses on generating plots with as little code as possible. Once we know our plot is correct, we’ll customize the output just as we did with Matplotlib.

In this project, we’ll analyze the results of rolling dice. When you roll one regular, six-sided die, you have an equal chance of rolling any of the numbers from 1 through 6. However, when you use two dice, you’re more likely to roll certain numbers than others. We’ll try to determine which numbers are most likely to occur by generating a dataset that represents rolling dice. Then we’ll plot the results of a large number of rolls to determine which results are more likely than others.
INSTALLING PLOTLY

```bash
$ python -m pip install --user plotly
$ python -m pip install --user pandas
```

**Plotly Express depends on pandas**, which is a library for working efficiently with data, so we need to install that as well.

“To see what kind of visualizations are possible with Plotly, visit the gallery of chart types at [https://plotly.com/python.”](https://plotly.com/python.%E2%80%9D)

**WE ALSO NEED:**

```python
import plotly.io as pio
pio.renderers.default = 'browser'
```

CREATING THE DIE CLASS

```python
from random import randint

class Die:
    "Simulate the behavior of a single die."
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)
```

ROLLING THE DIE

“Before creating a visualization based on the Die class, let’s roll a D6, print the results, and check that the results look reasonable:”

```python

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
```

ANALYZING THE RESULTS

```python
# Analyze the results.
frequencies = []
❷ poss_results = range(1, die.num_sides+1)
for value in poss_results:
❸     frequency = results.count(value)
❹     frequencies.append(frequency)

print(frequencies)
```

MAKING AN HISTOGRAM

Force plotly to go to browser

```python
import plotly.io as pio
pio.renderers.default = 'browser'
```

Create an histogram

```python
#Visualize
fig = px.bar(x=poss_results, y=frequencies)
fig.show()
```

**The final line calls fig.show(), which tells Plotly to render the resulting chart as an HTML file and open that file in a new browser tab.**

Feel free to try this now by changing px.bar() to something like px.scatter() or px.line(). You can find a full list of available chart types at [https://plotly.com/python/plotly-express](https://plotly.com/python/plotly-express).
This chart is dynamic and interactive. If you change the size of your browser window, the chart will resize to match the available space. If you hover over any of the bars, you’ll see a pop-up highlighting the specific data related to that bar.

CUSTOMIZING THE PLOT

“The first way to customize a plot with Plotly is to use some optional parameters in the initial call that generates the plot, in this case, px.bar().”

```python
#Visualize
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
```

ROLLING TWO DICE

```python
from die import Die
import plotly.express as px

import plotly.io as pio
pio.renderers.default = 'browser'

# Create a D6.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
dictionary = {}
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

    dictionary[str(value)]= frequency

print(frequencies)
print(dictionary)

#Visualize
title = 'Results of Rolling Two D6 Dice 1,000 Times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
```

“ The variable max_result makes the code for generating poss_results much easier to read ❸. We could have written range(2, 13), but this would work only for two D6 dice. When modeling real-world situations, it’s best to write code that can easily model a variety of situations. This code allows us to simulate rolling a pair of dice with any number of sides.”

FURTHER CUSTOMIZATION

Now that there are 11 bars, the default layout settings for the x-axis leave some of the bars unlabeled. While the default settings work well for most visualizations, this chart would look better with all of the bars labeled.
Plotly has an **update_layout() method that can be used to make a wide variety of updates to a figure after it’s been created.** 

Here we use the xaxis_dtick argument, which specifies the distance between tick marks on the x-axis. We set that spacing to 1, so that every bar is labeled.

ROLLING DICE OF DIFFERENT SIZES

```python
# Create a D6 and D10.
die_1 = Die(6)
die_2 = Die(10)
```

“There are six ways to roll a 7, 8, 9, 10, or 11, these are the most common results, and you’re equally likely to roll any one of them.

“ In just minutes, you can simulate a tremendous number of rolls using a large variety of dice.”

SAVING FIGURES

**When you have a figure you like, you can always save the chart as an HTML file through your browser. But you can also do so programmatically. To save your chart as an HTML file, replace the call to fig.show() with a call to fig.write_html():**

```python
fig.write_html('dice_visual_d6d10.html')
```

**The write_html() method requires one argument: the name of the file to write to. If you only provide a filename, the file will be saved in the same directory as the .py file. You can also call write_html() with a Path object, and write the output file anywhere you want on your system.**

```python
from pathlib import Path

path = Path('namepath')
fig.write_html(path/'dice_visual_d6d10.html')
```

**to open the HTML file:**

```python
import webbrowser

webbrowser.open(str(path / 'dice_visual_d6d10.html'))
```

**Or just double click the file.**

**Or in shell**

```python
open /Users/stefanochiapparini/Desktop/PYTHON/PYTHONcrash/projects/P2/dice_visual_d6d10.html
```

**INSTEAD OF FULL EXTENSIVE FOR LOOPS USE LIST COMPREHENSION AS AN ALTERNATIVE**

```python
results = [die_1.roll() + die_2.roll() + die_3.roll() for i in range(1000)]

#or

frequencies = [results.count(value) for value in poss_results]
```

CH16: DOWNLOADING DATA

**We’ll access and visualize data stored in two common data formats: CSV and JSON.** We’ll use Python’s csv module to process weather data stored in the CSV format and analyze high and low temperatures over time in two different locations. We’ll then use Matplotlib to generate a chart based on our downloaded data to display variations in temperature in two dissimilar environments: Sitka, Alaska, and Death Valley, California. Later in the chapter, we’ll use the json module to access earthquake data stored in the GeoJSON format and use Plotly to draw a world map showing the locations and magnitudes of recent earthquakes.
By the end of this chapter, you’ll be prepared to work with various types of datasets in different formats, and you’ll have a deeper understanding of how to build complex visualizations. Being able to access and visualize online data is essential to working with a wide variety of real-world datasets.

THE CSV FILE FORMAT

CSV files can be tedious for humans to read, but programs can process and extract information from them quickly and accurately.

PARSING THE CSV FILE READER

We read the file and chain the splitlines() method to get a list of all lines in the file, which we assign to lines.

```python
from pathlib import Path
import csv

path = Path('P2/weather data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
```

We read the file and chain the splitlines() method to get a list of all lines in the file, which we assign to lines.
Next, we build a reader object ❷. This is an object that can be used to parse each line in the file. To make a reader object, call the function csv.reader() and pass it the list of lines from the CSV file.
When given a reader object, the next() function returns the next line in the file, starting from the beginning of the file. Here we call next() only once, so we get the first line of the file, which contains the file headers ❸. We assign the data that’s returned to header_row. 

PRINTING THE HEADERS AND THEIR POSITIONS

The enumerate() function returns both the index of each item and the value of each item as you loop through a list. 

```python

for index, column_header in enumerate(header_row):
    print(index, column_header)
```

EXTRACTING AND READING DATA

Now that we know which columns of data we need, let’s read in some of that data. First, we’ll read in the high temperature for each day:

```python
# Extract high temperatures.
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

print(highs)
```

“We make an empty list called highs ❶ and then loop through the remaining rows in the file ❷. The reader object continues from where it left off in the CSV file and automatically returns each line following its current position.”

PLOTTING DATA IN A TEMPERATURE CHART

To visualize the temperature data we have, we’ll first create a simple plot of the daily highs using Matplotlib, as shown here:

```python

# Plot the high temperatures.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

# Format plot.
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
```

THE DATETIME MODULE

The data will be read in as a string, so we need a way to convert the string "2021-07-01" to an object representing this date. We can construct an object representing July 1, 2021, using the strptime() method from the datetime module.

```python
>>> from datetime import datetime
>>> first_date = datetime.strptime('2021-07-01', '%Y-%m-%d')
>>> print(first_date)
2021-07-01 00:00:00
```

We first import the datetime class from the datetime module. Then we call the method strptime() with the string containing the date we want to process as its first argument. The second argument tells Python how the date is formatted.

The strptime() method can take a variety of arguments to determine how to interpret the date.

PLOTTING DATES

We can improve our plot by extracting dates for the daily high temperature readings, and using these dates on the x-axis:

```python
# Extract dates and high temperatures.
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

# Plot the high temperatures.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format plot.
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
```

“The call to fig.autofmt_xdate() ❹ draws the date labels diagonally to prevent them from overlapping”

PLOTTING A LONGER TIMEFRAME

Copy the file sitka_weather_2021_simple.csv, which contains a full year’s worth of weather data for Sitka, to the folder where you’re storing the data for this chapter’s programs.
Now we can generate a graph for the entire year’s weather

PLOTTING A SECOND DATA SERIES

We can make our graph even more useful by including the low temperatures. We need to extract the low temperatures from the data file and then add them to our graph, as shown here.

```python
# Extract dates and high temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high temperatures.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
```

We add a call to plot() for the low temperatures and color these values blue 

SHADING AN AREA IN THE CHART

Let’s add a finishing touch to the graph by using shading to show the range between each day’s high and low temperatures. To do so, we’ll use the fill_between() method, which takes a series of x-values and two series of y-values and fills the space between the two series of y-values.

```python
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
```

The alpha argument controls a color’s transparency ❶. An alpha value of 0 is completely transparent, and a value of 1 (the default) is completely opaque. By setting alpha to 0.5, we make the red and blue plot lines appear lighter.

ERROR CHECKING

Missing data can result in exceptions that crash our programs, unless we handle them properly.
For example, let’s see what happens when we attempt to generate a temperature plot for Death Valley, California.

The traceback tells us that Python can’t process the high temperature for one of the dates because it can’t turn an empty string ('') into an integer ❶. Rather than looking through the data to find out which reading is missing, **we’ll just handle cases of missing data directly.
We’ll run error-checking code when the values are being read from the CSV file to handle exceptions that might arise.** Here’s how to do this:

```python
# Extract dates and high temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[3])
    except ValueError: print(f'Missing data for {current_date}')
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
```

If any data is missing, Python will raise a ValueError and we handle it by printing an error message that includes the date of the missing data. After printing the error, **the loop will continue processing the next row. If all data for a date is retrieved without error, the else block will run and the data will be appended to the appropriate lists.**

**Here we used a try-except-else block to handle missing data. Sometimes you’ll use continue to skip over some data, or use remove() or del to eliminate some data after it’s been extracted. Use any approach that works, as long as the result is a meaningful, accurate visualization.**

DOWNLOADING YOUR OWN DATA

“To download your own weather data, follow these steps:

Visit the NOAA Climate Data Online site at [https://www.ncdc.noaa.gov/cdo-web](https://www.ncdc.noaa.gov/cdo-web). In the Discover Data By section, click Search Tool. In the Select a Dataset box, choose Daily Summaries.
Select a date range, and in the Search For section, choose ZIP Codes. Enter the ZIP code you’re interested in and click Search.”

+More details look at the book

MAPPING GLOBAL DATASETS: GeoJSON Format

**In this section, you’ll download a dataset representing all the earthquakes that have occurred in the world during the previous month. Then you’ll make a map showing the location of these earthquakes and how significant each one was. Because the data is stored in the GeoJSON format, we’ll work with it using the json module. Using Plotly’s scatter_geo() plot, you’ll create visualizations that clearly show the global distribution of earthquakes.**

This data comes from one of the United States Geological Survey’s earthquake data feeds, at [https://earthquake.usgs.gov/earthquakes/feed](https://earthquake.usgs.gov/earthquakes/feed)

EXAMINING GeoJSON Data

The json module provides a variety of tools for exploring and working with JSON data. Some of these tools will help us reformat the file so we can look at the raw data more easily before we work with it programmatically.
Let’s start by loading the data and displaying it in a format that’s easier to read. This is a long data file, so instead of printing it, we’ll rewrite the data to a new file. Then we can open that file and scroll back and forth through the data more easily

```python

from pathlib import Path
import json

# Read data as a string and convert to a Python object.
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)
```

“The json.dumps() function that you saw in Chapter 10 can take an optional indent argument ❸, which tells it how much to indent nested elements in the data structure.”

“This GeoJSON file has a structure that’s helpful for location-based data. The information is stored in a list associated with the key "features". Because this file contains earthquake data, the data is in list form where every item in the list corresponds to a single earthquake. This structure might look confusing, but it’s quite powerful. It allows geologists to store as much information as they need to in a dictionary about each earthquake, and then stuff all those dictionaries into one big list.”

“We’ll only be working with one or two nesting levels at a time. We’ll start by pulling out a dictionary for each earthquake that was recorded in the 24-hour time period.

Note
When we talk about locations, we often say the location’s latitude first, followed by its longitude. This convention probably arose because humans discovered latitude long before we developed the concept of longitude. However, many geospatial frameworks list the longitude first and then the latitude, because this corresponds to the (x, y) convention we use in mathematical representations. The GeoJSON format follows the (longitude, latitude) convention. If you use a different framework, it’s important to learn what convention that framework follows.”

MAKING A LIST OF ALL THE EARTHQUAKES

```python
# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
```

Next, we’ll pull the magnitudes from each earthquake.
EXTRACTING MAGNITUDES

“We can loop through the list containing data about each earthquake, and extract any information we want. Let’s pull out the magnitude of each earthquake:”

```python

mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

print(mags[:10])

#or

mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
print(mags[:10])
```

We make an empty list to store the magnitudes, and then loop through the list all_eq_dicts ❶. Inside this loop, each earthquake is represented by the dictionary eq_dict. Each earthquake’s magnitude is stored in the 'properties' section of this dictionary, under the key 'mag' ❷. We store each magnitude in the variable mag and then append it to the list mags.

EXTRACTING LOCATION DATA

The location data for each earthquake is stored under the key "geometry". Inside the geometry dictionary is a "coordinates" key, and the first two values in this list are the longitude and latitude. Here’s how we’ll pull this data:

```python

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])
```

“The code eq_dict['geometry'] accesses the dictionary representing the geometry element of the earthquake ❶. The second key, 'coordinates', pulls the list of values associated with 'coordinates'. Finally, the 0 index asks for the first value in the list of coordinates, which corresponds to an earthquake’s longitude.”

BUILDING A WORLD MAP

“We import plotly.express with the alias px, just as we did in Chapter 15. The scatter_geo() function ❶ allows you to overlay a scatterplot of geographic data on a map. In the simplest use of this chart type, you only need to provide a list of latitudes and a list of longitudes. We pass the list lats to the lat argument, and lons to the lon argument.”

REPRESENTING MAGNITUDES

```python
title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags,title=title)
fig.show()
```

“We can improve this further by using color to represent magnitudes as well.”

CUSTOMIZING MARKER COLORS

We can use Plotly’s color scales to customize each marker’s color, according to the severity of the corresponding earthquake. We’ll also use a different projection for the base map.

```python
title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags,title=title, color=mags,
			 color_continuous_scale='Viridis', labels={'color':'Magnitude'}, projection='natural earth',)
fig.show()
```

“The projection argument accepts a number of common map projections ❹. Here we use the 'natural earth' projection, which rounds the ends of the map. Also, note the trailing comma after this last argument. When a function call has a long list of arguments spanning multiple lines like this, it’s common practice to add a trailing comma so you’re always ready to add another argument on the next line.”

OTHER COLOR SCALES

```python
>>> import plotly.express as px
>>> px.colors.named_colorscales()
```

“You can choose from a number of other color scales.”

ADDING HOVER TEXT

To finish this map, we’ll add some informative text that appears when you hover over the marker representing an earthquake. In addition to showing the longitude and latitude, which appear by default, we’ll show the magnitude and provide a description of the approximate location as well.

```python

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

print(mags[:10])
print(lons[:5])
print(lats[:5])

"""
mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
print(mags[:10])"""

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags,title=title, color=mags,
                     color_continuous_scale='Viridis', labels={'color':'Magnitude'},
                     projection='natural earth', hover_name=eq_titles, )
fig.show()
```

DOWNLOAD YOUR DATASETS

Recent Earthquakes: You can find online data files containing information about the most recent earthquakes over 1-hour, 1-day, 7-day, and 30-day periods. Go to [https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) and you’ll see a list of links to datasets for various time periods, focusing on earthquakes of different magnitudes. Download one of these datasets and create a visualization of the most recent earthquake activity.

CH17:APIS

**In this chapter, you’ll learn how to write a self-contained program that generates a visualization based on data it retrieves. Your program will use an application programming interface (API) to automatically request specific information from a website and then use that information to generate a visualization. Because programs written like this will always use current data to generate a visualization, even when that data might be rapidly changing, the visualization will always be up to date.**

USING AN API

**An API is a part of a website designed to interact with programs. Those programs use very specific URLs to request certain information. This kind of request is called an API call. The requested data will be returned in an easily processed format, such as JSON or CSV. Most apps that use external data sources, such as apps that integrate with social media sites, rely on API calls.**

GIT AND GITHUB

We’ll base our visualization on information from GitHub ([https://github.com](https://github.com/)), a site that allows programmers to collaborate on coding projects. We’ll use GitHub’s API to request information about Python projects on the site, and then generate an interactive visualization of the relative popularity of these projects using Plotly.

“GitHub takes its name from Git, a distributed version control system. Git helps people manage their work on a project in a way that prevents changes made by one person from interfering with changes other people are making. When you implement a new feature in a project, Git tracks the changes you make to each file. When your new code works, you commit the changes you’ve made, and Git records the new state of your project. If you make a mistake and want to revert your changes, you can easily return to any previously working state. (To learn more about version control using Git, see Appendix D.) Projects on GitHub are stored in repositories, which contain everything associated with the project: its code, information on its collaborators, any issues or bug reports, and so on.
When users on GitHub like a project, they can “star” it to show their support and keep track of projects they might want to use. In this chapter, we’ll write a program to automatically download information about the most-starred Python projects on GitHub, and then we’ll create an informative visualization of these projects.”

REQUESTING DATA USING AN API CALL

To see what an API call looks like

```python
https://api.github.com/search/repositories?q=language:python+sort:stars
```

Let’s examine the call. The first part, [https://api.github.com/](https://api.github.com/), directs the request to the part of GitHub that responds to API calls. The next part, search/repositories, tells the API to conduct a search through all the repositories on GitHub.
**The question mark after repositories signals that we’re about to pass an argument. The q stands for query, and the equal sign (=) lets us begin specifying a query (q=).** By using language:python, we indicate that we want information only on repositories that have Python as the primary language. The final part, +sort:stars, sorts the projects by the number of stars they’ve been given.”

You can see from the response that this URL is not primarily intended to be entered by humans, because it’s in a format that’s meant to be processed by a program. GitHub found just under nine million Python projects as of this writing ❶. The value for "incomplete_results" is true, which tells us that GitHub didn’t fully process the query ❷. GitHub limits how long each query can run, in order to keep the API responsive for all users. In this case it found some of the most popular Python repositories, but it didn’t have time to find all of them; we’ll fix that in a moment. The "items" returned are displayed in the list that follows, which contains details about the most popular Python projects on GitHub ❸.
INSTALLING REQUESTS

**The Requests package allows a Python program to easily request information from a website and examine the response.**

PROCESSING AN API RESPONSE

**Now we’ll write a program to automatically issue an API call and process the results:**

```python
import requests

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()

# Process results.
print(response_dict.keys())
```

**Then we assign the URL of the API call to the url variable ❶. This is a long URL, so we break it into two lines. The first line is the main part of the URL, and the second line is the query string.** 

**GitHub is currently on the third version of its API, so we define headers for the API call that ask explicitly to use this version of the API, and return the results in the JSON format ❷. Then we use requests to make the call to the API ❸. We call get() and pass it the URL and the header that we defined, and we assign the response object to the variable r.**

**The response object has an attribute called status_code, which tells us whether the request was successful. (A status code of 200 indicates a successful response.) We print the value of status_code so we can make sure the call went through successfully ❹. We asked the API to return the information in JSON format, so we use the json() method to convert the information to a Python dictionary ❺. We assign the resulting dictionary to response_dict.**

“Let’s take a look inside the response dictionary.”

WORKING WITH THE RESPONSE DICTIONARY

With the information from the API call represented as a dictionary, we can work with the data stored there. Let’s generate some output that summarizes the information. 

```python
# Convert the response object to a dictionary.
response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
```

“**The value associated with 'items' is a list containing a number of dictionaries, each of which contains data about an individual Python repository. We assign this list of dictionaries to repo_dicts ❷. We then print the length of repo_dicts to see how many repositories we have information for.**
To look closer at the information returned about each repository, we pull out the first item from repo_dicts and assign it to repo_dict ❸. We then print the number of keys in the dictionary to see how much information we have ❹. Finally, we print all the dictionary’s keys to see what kind of information is included ❺.”

**“(The only way to know what information is available through an API is to read the documentation or to examine the information through code, as we’re doing here.)”**

SUMMARIZING THE TOP REPOSITORIES

```python
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")
```

MONITORING APIS RATE LIMITS

**Most APIs have rate limits, which means there’s a limit to how many requests you can make in a certain amount of time.** To see if you’re approaching GitHub’s limits, enter [https://api.github.com/rate_limit](https://api.github.com/rate_limit) into a web browser.

**The information we’re interested in is the rate limit for the search API ❶. We see that the limit is 10 requests per minute ❷ and that we have 9 requests remaining for the current minute ❸. The value associated with the key "reset" represents the time in Unix or epoch time (the number of seconds since midnight on January 1, 1970) when our quota will reset ❹.** If you reach your quota, you’ll get a short response that lets you know you’ve reached the API limit. If you reach the limit, just wait until your quota resets.

**Note
Many APIs require you to register and obtain an API key or access token to make API calls.** As of this writing, GitHub has no such requirement, but if you obtain an access token, your limits will be much higher.

VISUALIZING REPOSITORY USING plotly

We’ll make an interactive bar chart: the height of each bar will represent the number of stars the project has acquired, and you’ll be able to click the bar’s label to go to that project’s home on GitHub.

“We make the initial visualization with just two lines of code ❹. This is consistent with Plotly Express’s philosophy that you should be able to see your visualization as quickly as possible before refining its appearance. Here we use the px.bar() function to create a bar chart. We pass the list repo_names as the x argument and stars as the y argument.”

STYLING THE CHART

We’ll make some changes in the initial px.bar() call and then make some further adjustments to the fig object after it’s been created.

```python
# Make visualization.
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
        yaxis_title_font_size=20)

fig.show()
```

ADDING CUSTOM TOOLTIPS

“In Plotly, you can hover the cursor over an individual bar to show the information the bar represents. This is commonly called a tooltip, and in this case, it currently shows the number of stars a project has. Let’s create a custom tooltip to show each project’s description as well as the project’s owner.”

```python
# Process repository information.
repo_dicts = response_dict['items']
repo_names, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # Build hover texts.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Make visualization.
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels,
        hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
        yaxis_title_font_size=20)

fig.show()
```

We first define a new empty list, hover_texts, to hold the text we want to display for each project ❶. In the loop where we process the data, we pull the owner and the description for each project ❷. Plotly allows you to use HTML code within text elements, so we generate a string for the label with a line break (<br />) between the project owner’s username and the description ❸. We then append this label to the list hover_texts.

In the px.bar() call, we add the hover_name argument and pass it hover_texts ❹. This is the same approach we used to customize the label for each dot in the map of global earthquake activity. As Plotly creates each bar, it will pull labels from this list and only display them when the viewer hovers over a bar.

ADDING CLICKABLE LINKS

“Because Plotly allows you to use HTML on text elements, we can easily add links to a chart. Let’s use the x-axis labels as a way to let the viewer visit any project’s home page on GitHub. We need to pull the URLs from the data and use them when generating the x-axis labels:”

```python
# Process repository information.
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Turn repo names into active links.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])
    # Build hover texts.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Make visualization.
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels,
        hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
        yaxis_title_font_size=20)

fig.show()
```

**We use the HTML anchor tag, which has the form <a href='URL'>link text</a>, to generate the link.** We then append this link to repo_links.
When we call px.bar(), we use repo_links for the x-values in the chart. The result looks the same as before, but now the viewer can click any of the project names at the bottom of the chart to visit that project’s home page on GitHub. Now we have an interactive, informative visualization of data retrieved through an API!

CUSTOMIZING MARKERS COLORS

Once a chart has been created, almost any aspect of the chart can be customized through an update method. We’ve used the update_layout() method previously. Another method, update_traces(), can be used to customize the data that’s represented on a chart.

```python
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
```

“In Plotly, a trace refers to a collection of data on a chart. The update_traces() method can take a number of different arguments; any argument that starts with marker_ affects the markers on the chart. Here we set each marker’s color to 'SteelBlue'; any named CSS color will work here. We also set the opacity of each marker to 0.6. An opacity of 1.0 will be entirely opaque, and an opacity of 0 will be entirely invisible.”

MORE REFERENCES

“A good place to start is with the article “Plotly Express in Python,” at [https://plotly.com/python/plotly-express](https://plotly.com/python/plotly-express). This is an overview of all the plots you can make with Plotly Express, and you can find links to longer articles about each individual chart type.
If you want to understand how to customize Plotly charts better, the article “Styling Plotly Express Figures in Python” will expand on what you’ve seen in Chapters 15–17. You can find this article at [https://plotly.com/python/styling-plotly-express](https://plotly.com/python/styling-plotly-express).
For more about the GitHub API, refer to its documentation at [https://docs.github.com/en/rest](https://docs.github.com/en/rest). Here you’ll learn how to pull a wide variety of information from GitHub. ”

THE HACKER NEWS API

To explore how to use API calls on other sites, let’s take a quick look at Hacker News ([https://news.ycombinator.com](https://news.ycombinator.com/)). On Hacker News, people share articles about programming and technology and engage in lively discussions about those articles. The Hacker News API provides access to data about all submissions and comments on the site, and you can use the API without having to register for a key.

**The following call returns information about the current top article as of this writing:**
[https://hacker-news.firebaseio.com/v0/item/31353677.json](https://hacker-news.firebaseio.com/v0/item/31353677.json)

```python
import requests
import json

# Make an API call, and store the response.
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)
```

**The following URL returns a simple list of all the IDs of the current top articles on Hacker News:**
[https://hacker-news.firebaseio.com/v0/topstories.json”](https://hacker-news.firebaseio.com/v0/topstories.json%E2%80%9D)

“We can use this call to find out which articles are on the home page right now, and then generate a series of API calls similar to the one we just examined. With this approach, we can print a summary of all the articles on the front page of Hacker News at the moment:”

```python
from operator import itemgetter

import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
```

First, we make an API call and print the status of the response ❶. **This API call returns a list containing the IDs of up to 500 of the most popular articles on Hacker News at the time the call is issued. We then convert the response object to a Python list ❷, which we assign to submission_ids. We’ll use these IDs to build a set of dictionaries, each of which contains information about one of the current submissions.”**

We set up an empty list called submission_dicts to store these dictionaries ❸. We then loop through the IDs of the top 30 submissions. We make a new API call for each submission by generating a URL that includes the current value of submission_id ❹. We print the status of each request along with its ID, so we can see whether it’s successful.
**Next, we create a dictionary for the submission currently being processed** ❺. We store the title of the submission, a link to the discussion page for that item, and the number of comments the article has received so far. Then we append each submission_dict to the list submission_dicts ❻.
Each submission on Hacker News is ranked according to an overall score based on a number of factors, including how many times it’s been voted on, how many comments it’s received, and how recent the submission is. **We want to sort the list of dictionaries by the number of comments. To do this, we use a function called itemgetter() ❼, which comes from the operator module. We pass this function the key 'comments', and it pulls the value associated with that key from each dictionary in the list.**