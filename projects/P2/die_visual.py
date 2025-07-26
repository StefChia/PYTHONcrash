
from die import Die
import plotly.express as px

import plotly.io as pio
pio.renderers.default = 'browser'

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
dictionary = {}
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

    dictionary[str(value)]= frequency

print(frequencies)
print(dictionary)

#Visualize
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()