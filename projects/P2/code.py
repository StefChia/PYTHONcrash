
import matplotlib.pyplot as plt
from pathlib import Path

"""#SIMPLE PLOTS
squares = [i**2 for i in range(1,6)]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(range(1,6),squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()"""


"""#SCATTER SQUARE
plt.style.use('classic')
fig, ax = plt.subplots()

ax.scatter(2, 4, s=200)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()"""



"""#PLOT MULTIPLE POINTS WITH SCATTER()
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()"""


"""#CALCULATING DATA AUTOMATICALLY

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

#ax.ticklabel_format(style='plain')

plt.show()"""





"""#COLORMAP WITH pyplot

x_values = range(1,1001)
y_values = [i**2 for i in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values,y_values,c= y_values, cmap=plt.cm.Blues, s=5)

ax.set_title('title',fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Squared value', fontsize = 14)
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])

#ax.ticklabel_format(style='plain')

plt.show()"""



"""
#SAVE PLOT AUTOMATICALLY

x_values = range(1,1001)
y_values = [i**2 for i in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values,y_values,c= y_values, cmap=plt.cm.Blues, s=5)

ax.set_title('title',fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Squared value', fontsize = 14)
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])

plt.savefig('image_squares',bbox_inches = 'tight')"""


"""#SAVE PLOT WITH A Path object
x_values = range(1,1001)
y_values = [i**2 for i in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values,y_values,c= y_values, cmap=plt.cm.Blues, s=5)

ax.set_title('title',fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Squared value', fontsize = 14)
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])

path = Path('/Users/stefanochiapparini/Desktop/PYTHON/PYTHONcrash/projects/P3')
plt.savefig(path/'image_squares',bbox_inches = 'tight')
"""



"""#EX 15.1

fig, ax = plt.subplots()

ax.scatter(range(1,5001),[i**3 for i in range(1,5001)], c =[i**3 for i in range(1,5001)], cmap = plt.cm.Blues, s = 3)

ax.set_title('Cube', fontsize = 14)
ax.set_xlabel('Numbers',fontsize = 14)
ax.set_ylabel('Cubes',fontsize = 14)

ax.tick_params(labelsize=14)

plt.show()"""







#PLOTLY
