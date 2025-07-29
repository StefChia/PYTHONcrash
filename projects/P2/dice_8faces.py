
import plotly.express as px
import matplotlib.pyplot as plt

from die import Die

import plotly.io as pio
pio.renderers.default = 'browser'

d1 = Die(8)
d2 = Die(8)

results = []
for i in range(1000):
    result = d1.roll() + d2.roll()
    results.append(result)
    
frequency = []
poss = range(2, d1.num_sides+d2.num_sides+1)
for j in poss:
    freq = results.count(j)
    frequency.append(freq)

title = 'Plot possible values and frequency.'
labels = {'x':'values', 'y':'freq'}

fig = px.bar(x=poss, y=frequency, title=title, labels=labels)

fig.show()

