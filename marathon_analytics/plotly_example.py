import math
import plotly
import plotly.graph_objs as go
 
## generate some data
x = [x/10 for x in range(100)]
y = [math.sin(c) for c in x]
 
## check that the values are as expected:
print(f'x={x}')
print(f'y={y}')
 
## create a figure and plot it
fig = go.Scatter(x=x, y=y)
fig = go.Bar(x=x, y=y)
plotly.offline.plot({"data":[fig]})

# Pie chart example:
x = ["Apple Pie",
     "Chocolate Pie",
     "Pecan Pie",
     "Chocolate Pecan Pie"]
y = [5, 9, 4, 14]
 
fig = go.Pie(labels=x, values=y)
# plotly.offline.plot({"data":[fig]})
graph_div = plotly.offline.plot({"data":[fig]},
                    auto_open=False,
                    output_type="div")