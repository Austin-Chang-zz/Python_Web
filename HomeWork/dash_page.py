from dash import Dash,html,dcc
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Austin-Chang-zz/Python_Web/main/HomeWork/sales_orders.csv')

app = Dash(__name__)


# Define the layout
app.layout = html.Div([
    html.H1("Production Page", style={'textAlign': 'center'}),
    dcc.Markdown("### Welcome to the Production Page"),
    dcc.Markdown(f"**Data Preview:**\n\n{df.head().to_markdown()}")
])
if __name__ == '__main__':
    app.run(debug=True)