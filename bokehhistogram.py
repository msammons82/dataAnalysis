#histogram using bokeh and pandas
# install bokeh and pandas packages for use

from bokeh.charts import Histogram, output_notebook, show
import pandas as pd

output_notebook()

df = pd.read_csv(r"file path")

p = Histogram(df, values = "category", 
                title = "category", 
                color = "navy")

show(p)