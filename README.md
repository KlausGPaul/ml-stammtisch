# Labelit Data Labeller

Bokeh server application that allows selection of portions of time series data and storing it. While similar applications exist 
(https://github.com/geocene/trainset or https://grafana.com/) these often cannot readily be installed in corporate IT environments, or, in the case of grafana, need specific databases to be set up.

Plus, its a showcase for bokeh server.

## Installation

* Please download https://fonts.google.com/specimen/Asap+Condensed and store AsapCondensed-Regular.ttf in the folder `labelit/static'
* We need bokeh https://docs.bokeh.org/en/latest/docs/installation.html package
* To create a data set, run the `Crunch ECG.ipynb` notebook, this needs wfdb https://pypi.org/project/wfdb/
