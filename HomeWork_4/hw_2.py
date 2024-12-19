from dash import Dash, html, callback, Input, Output, dash_table
import pandas as pd
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_extensions as de


df = pd.read_csv('https://raw.githubusercontent.com/Austin-Chang-zz/Python_Web/main/HomeWork/sales_orders.csv')


# Display the DataFrame
print(df)

# Check for required columns
required_columns = ['sales_name', 'order_date', 'yield_rate', 'thru_put']
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"Dataset is missing one or more required columns: {required_columns}")

app1 = Dash(
    __name__,
    external_stylesheets=dmc.styles.ALL,
    requests_pathname_prefix="/production/",
)

radio_data = [['yield_rate', '良率'], ['thru_put', '直通率']]

selected_data = [{'value': value, 'label': value} for value in df['sales_name'].dropna().unique()]

app1.layout = dmc.MantineProvider(
    dmc.AppShell(
        children=[
            dmc.AppShellHeader(
                dmc.NavLink(
                    label="職能發展學院",
                    leftSection=DashIconify(icon="tabler:gauge"),
                    active=True,
                    variant="filled",
                    color="blue",
                    id="school_icon",
                    href='/',
                ),
                height=70,
            ),
            dmc.AppShellMain(
                [
                    dmc.Container(
                        dmc.Title("Production Yield Rate & Throughput", order=2),
                        fluid=True,
                        ta='center',
                        my=30,
                    ),
                    dmc.Flex(
                        [
                            dmc.Stack(
                                [
                                    dmc.RadioGroup(
                                        children=[
                                            dmc.Radio(label, value)
                                            for value, label in radio_data
                                        ],
                                        id="radio_item",
                                        value="yield_rate",
                                        label="請選擇查詢的種類",
                                        size="md",
                                    ),
                                    dmc.Select(
                                        label="請選擇業務",
                                        placeholder="請選擇1個",
                                        id="dropdown-selection",
                                        data=selected_data,
                                    ),
                                ],
                            ),
                            dmc.ScrollArea(
                                children=[],
                                height=300,
                                style={"width": "50%"},
                                id='scrollarea'
                            ),
                        ],
                        direction={"base": "column", "sm": "row"},
                        gap={"base": "sm", "sm": "lg"},
                    ),
                ],
            ),
        ],
        header={'height': 70},
    ),
)

@callback(
    [Output('scrollarea', 'children')],
    [Input('dropdown-selection', 'value'),
     Input('radio_item', 'value')],
)
def update_table(sales_name_value, radio_value):
    if not sales_name_value or not radio_value:
        return [dmc.Text("Please select both options.")]
    
    filtered_df = df[df['sales_name'] == sales_name_value]
    if filtered_df.empty:
        return [dmc.Text("No data available for the selected filters.")]

    rows = [
        dmc.TableRow(
            [
                dmc.TableCell(row["sales_name"]),
                dmc.TableCell(row["order_date"]),
                dmc.TableCell(row[radio_value]),
            ]
        )
        for _, row in filtered_df.iterrows()
    ]
    head_name = "良率" if radio_value == 'yield_rate' else "直通率"

    return [dmc.Table(
        [
            dmc.TableHead(
                dmc.TableRow(
                    [
                        dmc.TableCell("業務"),
                        dmc.TableCell("訂單日期"),
                        dmc.TableCell(head_name),
                    ]
                )
            ),
            dmc.TableBody(rows)
        ]
    )]

if __name__ == '__main__':
    app1.run(debug=True)
