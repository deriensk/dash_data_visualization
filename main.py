import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })
 
df = pd.read_csv("gdp-life-exp-2007.csv")
print(df.head())


X = df.drop(['gdp_per_capita'], axis=1)
y = df['gdp_per_capita']

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig1 = px.bar(df, x="continent", y='gdp_per_capita', color="continent", barmode="group")
# fig1.show()

fig2 = px.scatter(df, x="country", y='gdp_per_capita', color="country", marginal_y="violin",
           marginal_x="box", trendline="ols", template="simple_white")
# fig2.show()


fig3 = px.scatter_matrix(df, dimensions=["population","country"], color="gdp_per_capita")
# fig3.show()


app.layout = html.Div(children=[
    html.H1(children='Hello Dash from EPITA'),

    html.Div(children='''
        Web Application test mode by Sudhamsu KHANAL
    '''),

    dcc.Graph(
        id='example-graph1',
        figure=fig1
    ),

    dcc.Graph(id='example-graph2',        
        figure=fig2),
(
    dcc.Graph(id='example-graph3',
        figure=fig3
        )
    )
    
    
])

if __name__ == '__main__':
    app.run_server(debug=True)