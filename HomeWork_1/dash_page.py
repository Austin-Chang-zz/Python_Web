from dash import Dash,html,dcc,callback,Input,Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/Austin-Chang-zz/Python_Web/main/HomeWork/sales_orders.csv')

app1 = Dash(__name__,requests_pathname_prefix="/dash/")


# Define the layout
app1.layout = html.Div([
    html.H1("Production Page", style={'textAlign': 'center'}),
    dcc.Markdown("### Welcome to the Production Page"),
    dcc.Markdown(f"**Data Preview:**\n\n{df.head().to_markdown()}"),
    dcc.Dropdown(df.sales_name.unique(),value="Alice",id='dropdown-selection'),
    dcc.Graph(id='graph-content') 
])


@callback(
    Output('graph-content','figure'),
    Input('dropdown-selection','value')
)

def update_graph(value):
    dff = df[df.sales_name == value]
    # return px.line(dff, x='order_date',y='yield_rate',title='Production Yield Rate')
    return px.scatter(dff, x='order_date',y='yield_rate',title='Production Yield Rate')

if __name__ == '__main__':
    app1.run(debug=True)