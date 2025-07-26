
from random_walk import RandomWalk
import matplotlib.pyplot as plt

"""while True:
    #Make a Random Walk
    rw = RandomWalk(50000)
    rw.fill_walk()

    #plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='None', s=1)
    ax.set_aspect('equal')
    
    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input('Create another rw? (yes/no) ')
    if keep_running.lower() == 'no':
        break"""
        

#EX 15.3 POLLEN GRAIN

#Make a Random Walk
rw = RandomWalk(5000)
rw.fill_walk()

#plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,9))
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth = 3)
ax.set_aspect('equal')

# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=500)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=500)

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()