
from die import Die
import plotly.express as px

import plotly.io as pio
pio.renderers.default = 'browser'

# Create a D6 and D10.
die_1 = Die(6)
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50000):
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
title = 'Results of Rolling a D6 and a D10 50,000 Times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

#fig.show()
fig.write_html('dice_visual_d6d10.html')