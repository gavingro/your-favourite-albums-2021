import os

import dash

from app import app, server
from layout.layout import layout1
from layout.callbacks import *

app.layout = layout1

if __name__ == "__main__":
    app.run_server(debug=True)
