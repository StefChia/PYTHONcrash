
from die import Die
import plotly.express as px

import plotly.io as pio
pio.renderers.default = 'browser'

# Create a D6 and D6.
die_1 = Die()
die_2 = Die()
die_3 = Die()

"""# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)"""
    
#Uusing list comprehension
results = [die_1.roll() + die_2.roll() + die_3.roll() for i in range(1000)]
    
# Analyze the results.

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
dictionary = {}
poss_results = range(3, max_result+1)

"""
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)"""

#With list comprehension
frequencies = [results.count(value) for value in poss_results]

print(frequencies)

#Visualize
title = 'Results of Rolling Two D6 Dice 1,000 Times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()