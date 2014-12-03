__author__ = 'TPei'
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from utils import *

x = []
y = []

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

start = timer()
for i in range(1, 1000000000):
    if i % 1000 == 0:
        # just some time measurements as data
        x.append(i)
        y.append(timer() - start)
        start = timer()

        update_graph(plt, fig, line1, y, x)