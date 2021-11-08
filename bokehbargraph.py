#create a bar chart using bokeh
#need to install bokeh and pandas packages

import pandas as pd
from bokeh.charts import bar, output_notebook, show

output_notebook()

df = pd.read_csv(r"file path")

p = Bar(df, "Category", values = "Category", 
        title = "whatever the category is", 
                legend = "top_right")

show(p)

