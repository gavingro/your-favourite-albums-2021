import os

import dash

from app import app, server
from layout.layout import layout
from layout.callbacks import *

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True)
