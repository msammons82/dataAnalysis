# create a single line , line() method used.
# bokeh package needs to be installed.

from bokeh.plotting import figure, output_notebook, show

output_notebook()

p = figure(plot_width = 400, plot_height = 400)

p.line([1, 2, 3, 4, 5], [3, 1, 2, 6, 5], 
        line_width = 2, color = "green")

show(p)