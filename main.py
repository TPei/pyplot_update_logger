__author__ = 'TPei'
import matplotlib.pyplot as plt
from timeit import default_timer as timer

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

        # set new data
        line1.set_xdata(x)
        line1.set_ydata(y)

        # resetting the limits is necessary when the graph max / min changes
        plt.ylim(min(y[-1000:]), max(y[-1000:]))
        plt.xlim(min(x[-1000:]), max(x))

        # redraw
        fig.canvas.draw()