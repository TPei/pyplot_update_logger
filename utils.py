__author__ = 'TPei'


def update_graph(subplot, figure, line_object, values, keys=None):
    # set new data
    line_object.set_xdata(keys)
    line_object.set_ydata(values)

    # resetting the limits is necessary when the graph max / min changes
    subplot.ylim(min(values[-1000:]), max(values[-1000:]))
    subplot.xlim(min(keys[-1000:]), max(keys))

    # redraw
    figure.canvas.draw()