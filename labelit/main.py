"""
labelit

A python/bokeh server based tool. Adapted to ECG data.
Copyright 2020 Klaus G. Paul

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from bokeh.plotting import curdoc
from bokeh.layouts import row, column, layout
from bokeh.models import Select
from bokeh.models import Legend
from bokeh.models import Range1d
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Button, TextInput
from bokeh.events import ButtonClick
import numpy as np
import os

import themes

import logging
import pandas as pd
import random

class GUI():
    def __init__(self,doc=None,sc=None):
        self.theme = themes.THEME()
        self.have_plots = False

        self.dfAnomalies = pd.read_parquet("data/abnormalities.parquet")

    def save_selection(self,event):
        indices = sorted(self.cds.selected.indices)
        ddf = self.df.iloc[range(min(indices),max(indices)+1)]
        fromdt = ddf.iloc[0].Timestamp.strftime("%Y%m%d.%H%M%S")
        todt = ddf.iloc[-1].Timestamp.strftime("%Y%m%d.%H%M%S")
        ddf.to_parquet("results/{}.{}.{}.{}.{}.parquet".format(self.select_record.value,len(ddf),fromdt,todt,self.comment.value),
                        use_deprecated_int96_timestamps=True)
        self.save.button_type="success"


    def display_record(self,attr,old,new):
        self.save.disabled=True
        self.select_record.disabled=True
        self.comment.disabled=True
        df = pd.read_parquet("data/{}.parquet".format(new))

        # This is very specific to the ECG datasetm data files may have MLII and one of V1, V2, V4, V5
        df.sort_values("Timestamp",inplace=True)
        self.df = df.copy()
        y = {}
        mapping = {}
        for c in sorted(df.columns):
            if c[0] == "V":
                if "y1" in y.keys():
                    y["y2"] = c
                    mapping[c] = "y2"
                else:
                    y["y1"] = c
                    mapping[c] = "y1"
            elif c == "MLII":
                y["y2"] = c
                mapping[c] = "y2"

        df.rename(columns=mapping,inplace=True)

        df["color"] = "white"

        ddf = self.dfAnomalies[self.dfAnomalies.record == new]

        if not self.have_plots:
            self.cds = ColumnDataSource(df)
            self.cds_as = ColumnDataSource(ddf)
            p = []

            TOOLTIPS = [("symbol","@symbol"),("ann","@annotation")]
            p_new = figure(plot_width=1200, plot_height=75, x_axis_type="datetime",title="Anomalies",
                        tools="box_select,pan,box_zoom,reset",
                        tooltips=TOOLTIPS)
            p_new = self.theme.apply_theme_defaults(p_new)
            p_new.inverted_triangle(x="Timestamp",y=0,source=self.cds_as,color="red",size=10)
            p_new.ygrid.visible = False
            p_new.yaxis.visible = False
            p_new.outline_line_color = None
            p.append(p_new)

            for parameter in ["y1","y2"]:
                if "sample" in parameter.lower():
                    continue
                if len(p)<=0:
                    p_new = figure(plot_width=1200, plot_height=200, x_axis_type="datetime",title="{}".format(y[parameter]),
                        tools="box_select,pan,box_zoom,reset")
                        #y_range=(self.ymin[parameter],self.ymax[parameter]),tools="box_select,pan,box_zoom,reset")
                else:
                    p_new = figure(plot_width=1200, plot_height=200, x_axis_type="datetime",title="{}".format(y[parameter]),
                        x_range=p[0].x_range,#y_range=(self.ymin[parameter],self.ymax[parameter]),
                        tools="box_select,pan,box_zoom,reset")
                elem1 = p_new.circle(x="Timestamp",y=parameter,color="color",source=self.cds,#alpha="alpha",
                            selection_fill_color="#111111",selection_line_color="#111111",
                            nonselection_line_color="#00498F",nonselection_fill_color="#00498F")
                elem2 = p_new.line(x="Timestamp",y=parameter,color="color",source=self.cds,alpha=0.15,line_color="red",line_width=0.25)
                legend = Legend(items=[
                    (y[parameter], [elem1]),
                    (y[parameter], [elem2]),
                    ],location="top_center",orientation="horizontal",
                        background_fill_color=self.theme.background_color,border_line_color=None,label_text_font=self.theme.text_font,
                        label_text_line_height=10,glyph_height=20,label_text_color=self.theme.text_color,label_standoff=0,margin=0,
                        click_policy="hide")
                p_new = self.theme.apply_theme_defaults(p_new)
                p_new.add_layout(legend,'below')
                p_new.legend.click_policy="hide"
                p.append(p_new)

            p_new = figure(plot_width=600, plot_height=600, title="{} over {}".format(y["y2"],y["y1"]),
                        tools="box_select,pan,box_zoom,reset")
            p_new.circle(x="y1",y="y2",color="color",source=self.cds,alpha=0.25,
                            selection_fill_color="#111111",selection_line_color="#111111",
                            nonselection_line_color="#00498F",nonselection_fill_color="#00498F")
            p_new = self.theme.apply_theme_defaults(p_new)
            p.append(p_new)

            self.plots = p
            self.have_plots = True
        else:
            self.cds.data = {"Timestamp":df["Timestamp"],"y1":df["y1"],"y2":df["y2"],"color":df["color"]}
            self.cds.selected.indices = []
            self.cds_as.data = {"Timestamp":ddf["Timestamp"],
                            "symbol":ddf["symbol"],
                            "annotation":ddf["annotation"]}

        # I disagree with the zooming functionality adding a padding, plus it forces zooming out
        self.plots[0].x_range.start = df["Timestamp"].min()
        self.plots[0].x_range.end = df["Timestamp"].max()
        self.save.disabled=False
        self.select_record.disabled=False
        self.comment.disabled=False
        self.comment.value="good"
        self.save.button_type="default"
        

    def create_content(self,doc):
        available_records = []
        for f in os.listdir("./data"):
            if f.endswith(".parquet") and len(f.split(".")[0]) == 3:
                available_records.append(f.split(".")[0])
        self.select_record = Select(options=sorted(available_records))
        self.save = Button(label="Save Selection (edit class if not 'good')")
        self.comment = TextInput(value="good")

        self.select_record.on_change("value",self.display_record)

        self.select_record.value = sorted(available_records)[random.randrange(0,len(available_records))]
        self.save.on_event(ButtonClick, self.save_selection)
        doc.add_root(column([row([self.select_record,self.save,self.comment]),
            column(self.plots)]))


doc = curdoc()
doc.title = "Labelit"
args = doc.session_context.request.arguments

gui = GUI(doc=doc,sc=doc.session_context.id)
gui.create_content(doc)
