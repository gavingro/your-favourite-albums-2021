from dash.dependencies import Input, Output

from app import app


@app.callback(
    Output("display-value", "children"),
    [Input("dropdown", "value")],
)
def display_value(value):
    return 'You have selected "{}"'.format(value)
