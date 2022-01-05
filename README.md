# friesen-2021-wrapped
Dataviz (and relevant Dash App) for Will Friesen's 2021 Wrapped Album list.

Application hosted with [Heroku](https://our-favourite-albums-2021.herokuapp.com).

Data grabbed from the [google sheets](https://docs.google.com/spreadsheets/d/1E6YwZ5SdZPHBeOZQTKj22AWFnbCqjbhlv9Tplt73RQk/edit?fbclid=IwAR0lxp9NPKsdTe2mpNoLWL7eB7rmdtvafhdMIxx4He24wEobpU52PS_3kAM#gid=0).


## Architecture

* index.py
    * *(Dash App to run server from and assemble layout from.)*
* app.py
    * *(Plotly Dash app objects to be imported around in components and callbacks and index.py)*
* Procfile
    * *(Necessary for gunuicorn Heroku Deployment)
* runtime.txt
    * *(Necessary for gunuicorn Heroku Deployment)
* layout/
    * callbacks.py
    * layout.py
    * components/
        * *(graphs and layout components)*.
* assets/
    * *(our css media files).*
* data/
    * datafunc.py
        * *(Functions for working with album data).
    * data.py
        * *(data objects from reading in data and pipeline.)
    * AOTY-2021.lists.csv
        * *our 2021 data*.
* tests/
    * *(unittesting files)*.
