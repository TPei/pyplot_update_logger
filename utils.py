__author__ = 'TPei'


def update_graph(subplot, figure, line_object, x, y = None):
    # set new data
    line_object.set_xdata(x)
    line_object.set_ydata(y)

    # resetting the limits is necessary when the graph max / min changes
    subplot.ylim(min(y[-1000:]), max(y[-1000:]))
    subplot.xlim(min(x[-1000:]), max(x))

    # redraw
    figure.canvas.draw()