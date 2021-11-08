# box plot using bokeh
# need to install bokeh, and pandas packages

from bokeh.charts import BoxPlot, output_notebook, show
import pandas as pd

output_notebook()

df = pd.read_csv(r"file path")

p = BoxPlot(df, values = "category", label = "category", 
            color = "yellow", title = "category",
            legend = "top_right")

show(p)