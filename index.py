import os

import pandas as pd

from app import app, server
from layout.layout import layout
from layout.callbacks import *

# # Just to supress the .loc message
pd.options.mode.chained_assignment = None

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True)
