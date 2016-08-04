
import plotly.plotly as py
import plotly.graph_objs as go

dataset= arff.load(open ('http://kristenhuber.com/Amazon_initial_50_30_10000.arff', 'rb'))
data=np.array(dataset['data'])

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[3, 4, 8, 3],
    fill= None,
    mode='lines',
    line=dict(
        color='rgb(143, 19, 131)',
    )
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[1, 6, 2, 6],
    fill='tonexty',
    mode='lines',
    line=dict(
        color='rgb(143, 19, 131)',
    )
)

data = [trace0, trace1]
py.iplot(data, filename='filling-interior-area')