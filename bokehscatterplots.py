#scatter plot using bokeh and pandas
# need to install bokeh and pandas packages

from bokeh.charts import Scatter, output_notebook, show
import pandas as pd

output_notebook()

df = pd.read_csv(r"file path")

p = Scatter(df, x = "category", y = "category", 
            title = "category titles", 
            xlabel = "x label", ylabel = "y label",
            color = "orange")

show(p)