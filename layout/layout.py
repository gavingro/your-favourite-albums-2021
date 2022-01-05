import dash
from dash import dcc
from dash import html


layout1 = html.Div(
    [
        html.H2("Hello World"),
        dcc.Dropdown(
            id="dropdown",
            options=[{"label": i, "value": i} for i in ["LA", "NYC", "MTL"]],
            value="LA",
        ),
        html.Div(id="display-value"),
    ]
)
