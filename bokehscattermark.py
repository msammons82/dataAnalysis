# creates scatter circle markers, circe() method is used.
#need to install package bokeh

from bokeh.plotting import figure, output_notebook, show

output_notebook()

p = figure(plot_width = 400, plot_height = 400)

p.circle([1, 2, 3, 4, 5], [4, 7, 1, 6, 3], 
        size = 10, color = "navy", alpha = 0.5)

show(p)