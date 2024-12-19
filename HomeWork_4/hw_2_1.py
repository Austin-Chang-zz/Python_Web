from dash import Dash, html, dcc, callback, Input, Output, dash_table, _dash_renderer
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
from dash_iconify import DashIconify

_dash_renderer._set_react_version("18.2.0")

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# Updated requests_pathname_prefix to /production
app1 = Dash(
    __name__,
    external_stylesheets=dmc.styles.ALL,
    requests_pathname_prefix="/production/",
)

# Rest of the code remains unchanged
radio_data = [['yield_rate', '良率'], ['thru_put', '直通率']]

selected_data = [{'value': value, 'label': value} for value in df.sales_name.unique()]

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
                    h=70,
                    href='/',
                    refresh=True,
                ),
                h=70,
            ),
            dmc.AppShellMain(
                [
                    dmc.Container(
                        dmc.Title(f"Production Yield Rate & Throught Put", order=2),
                        fluid=True,
                        ta='center',
                        my=30,
                    ),
                    dmc.Flex(
                        [
                            dmc.Stack(
                                [
                                    dmc.RadioGroup(
                                        children=dmc.Group(
                                            [
                                                dmc.Radio(l, value=k)
                                                for k, l in radio_data
                                            ],
                                            my=10,
                                        ),
                                        id="radio_item",
                                        value="yield_rate",
                                        label="請選擇查詢的種類",
                                        size="md",
                                        mb=10,
                                    ),
                                    dmc.Select(
                                        label="請選擇業務",
                                        placeholder="請選擇1個",
                                        id="dropdown-selection",
                                        value="Alice",
                                        data=selected_data,
                                        w=200,
                                        mb=10,
                                    ),
                                ],
                            ),
                            dmc.ScrollArea(
                                children=[], h=300, w='50%', id='scrollarea'
                            ),
                        ],
                        direction={"base": "column", "sm": "row"},
                        gap={"base": "sm", "sm": "lg"},
                        justify={"base": "center"},
                    ),
                    dmc.Container(
                        dmc.LineChart(
                            id='lineChart',
                            h=300,
                            dataKey="order_date",
                            data=None,
                            series=[],
                            curveType="bump",
                            tickLine="xy",
                            withXAxis=True,
                            withDots=True,
                            gridAxis='x',
                            withLegend=True,
                            xAxisLabel='year',
                        ),
                        my=50,
                    ),
                ],
            ),
        ],
        header={'height': 70},
    ),
)

@callback(
    Output('lineChart', 'data'),
    Output('lineChart', 'series'),
    Input('dropdown-selection', 'value'),
    Input('radio_item', 'value'),
)
def update_graph(sales_name_value, radio_value):
    dff = df[df.sales_name == sales_name_value]
    yield_rate_diff = dff[['sales_name', 'order_date', radio_value]]

    line_chart_data = yield_rate_diff.to_dict('records')
    if radio_value == 'yield_rate':
        label = f'{sales_name_value}: Yield Rate Chart'
    elif radio_value == 'thru_put':
        label = f'{sales_name_value}: Through Put Chart'
   
    series = [{"name": radio_value, "label": label, "color": "indigo.6"}]

    return line_chart_data, series

@callback(
    Output('scrollarea', 'children'),
    Input('dropdown-selection', 'value'),
    Input('radio_item', 'value'),
)
def update_table(sales_name_value, radio_value):
    dff = df[df.sales_name == sales_name_value]
    yield_rate_diff = dff[['sales_name', 'order_date', radio_value]]
    elements = yield_rate_diff.to_dict('records')

    rows = [
        dmc.TableTr(
            [
                dmc.TableTd(element["sales_name"]),
                dmc.TableTd(element["order_date"]),
                dmc.TableTd(element[radio_value]),
            ]
        )
        for element in elements
    ]

    if radio_value == 'yield_rate':
        head_name = '良率'
    elif radio_value == 'thru_put':
        head_name = '直通率'
    

    head = dmc.TableThead(
        dmc.TableTr(
            [
                dmc.TableTh("業務"),
                dmc.TableTh("訂單日期"),
                dmc.TableTh(head_name),
            ]
        )
    )

    body = dmc.TableTbody(rows)
    caption = dmc.TableCaption(f"{sales_name_value} ,{head_name}")
    return dmc.Table([head, body, caption])

if __name__ == '__main__':
    app1.run(debug=True)