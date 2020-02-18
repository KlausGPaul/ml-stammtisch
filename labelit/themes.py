"""
Helper function to assign themes to bokeh widgets and plots. Slightly more brutal approach than the built-in theme functionality.


Copyright 2020 Dr. Klaus G. Paul

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

class THEME():
    #@log_function_calls
    def __init__(self,theme="orbifold"):
        self.set_theme(theme)

    #@log_function_calls
    def set_theme(self,theme="orbifold"):
        if theme == "orbifold":
            self.background_color="#626262"
            self.background_fill_color="#565656"
            self.plot_color="#FFFFFF"
            self.text_font="Asap Condensed"
            self.text_color="#FFFFFF"
            self.tick_line_color="#FFFFFF"
            self.axis_label_text_color="#FFFFFF"
            self.axis_line_color="#FFFFFF"
            self.label_text_color="#FFFFFF"
            self.tick_line_color="#FFFFFF"
            self.good = "green"
            self.bad = "red"
            self.amber = "orange"
            self.indet = "silver"
        else:
            self.background_color="#626262"
            self.background_fill_color="#565656"
            self.plot_color="#FFFFFF"
            self.text_font="Asap Condensed"
            self.text_color="#FFFFFF"
            self.tick_line_color="#FFFFFF"
            self.axis_label_text_color="#FFFFFF"
            self.axis_line_color="#FFFFFF"
            self.label_text_color="#FFFFFF"
            self.tick_line_color="#FFFFFF"
            self.good = "green"
            self.bad = "red"
            self.amber = "orange"
            self.indet = "silver"


    #@log_function_calls
    def apply_theme_defaults(self,bokeh_tingy):
        try:
            bokeh_tingy.background_fill_color = self.background_color
        except:
            pass

        try:
            bokeh_tingy.border_fill_color = self.background_color
        except:
            pass

        try:
            bokeh_tingy.color = self.plot_color
        except:
            pass

        try:
            bokeh_tingy.axis.axis_label_text_color=self.plot_color
        except:
            pass

        try:
            bokeh_tingy.axis.axis_line_color=self.plot_color
        except:
            pass

        try:
            bokeh_tingy.axis.major_label_text_color=self.plot_color
        except:
            pass

        try:
            bokeh_tingy.axis.major_label_text_font=self.text_font
        except:
            pass

        try:
            bokeh_tingy.xaxis.major_label_text_font=self.text_font
        except:
            pass

        try:
            bokeh_tingy.yaxis.major_label_text_font=self.text_font
        except:
            pass

        try:
            bokeh_tingy.yaxis.major_label_text_color=self.text_color
        except:
            pass

        try:
            bokeh_tingy.title.text_font=self.text_font
        except:
            pass

        try:
            if 'label_text_font' in bokeh_tingy.legend.__dict__.keys():
                bokeh_tingy.legend.label_text_font = self.text_font
        except:
            pass

        try:
            if 'label_text_line_height' in bokeh_tingy.legend.__dict__.keys():
                bokeh_tingy.legend.label_text_line_height = 10
        except:
            pass

        try:
            if 'glyph_height' in bokeh_tingy.legend.__dict__.keys():
                bokeh_tingy.legend.glyph_height = 20
        except:
            pass

        try:
            if 'label_text_color' in bokeh_tingy.legend.__dict__.keys():
                bokeh_tingy.legend.label_text_color = self.text_color
        except:
            pass

        try:
            if 'background_fill_color' in bokeh_tingy.legend.__dict__.keys():
                bokeh_tingy.legend.background_fill_color = self.background_color
        except:
            pass

        try:
            if 'label_standoff' in bokeh_tingy.legend.__dict__.keys():
                bokeh_tingy.legend.label_standoff = 0
        except:
            pass

        try:
            if 'border_line_color' in bokeh_tingy.legend.__dict__.keys():
                bokeh_tingy.legend.border_line_color = self.background_color
        except:
            pass

        try:
            bokeh_tingy.axis.major_tick_line_color=self.plot_color
        except:
            pass

        try:
            if 'margin' in bokeh_tingy.legend.__dict__.keys():
                bokeh_tingy.legend.margin = 0
        except:
            pass

        try:
            if 'padding' in bokeh_tingy.legend.__dict__.keys():
                bokeh_tingy.legend.padding = 0
        except:
            pass

        try:
            bokeh_tingy.title.text_color=self.plot_color
        except:
            pass

        try:
            bokeh_tingy.xaxis.minor_tick_line_color=None
        except:
            pass

        try:
            bokeh_tingy.yaxis.minor_tick_line_color=None
        except:
            pass

        try:
            bokeh_tingy.toolbar.logo=None
        except:
            pass

        try:
            bokeh_tingy.xgrid.grid_line_alpha = 0.5
        except:
            pass

        try:
            bokeh_tingy.xgrid.grid_line_dash = [2,4]
        except:
            pass

        try:
            bokeh_tingy.ygrid.grid_line_alpha = 0.5
        except:
            pass

        try:
            bokeh_tingy.ygrid.grid_line_dash = [2,4]
        except:
            pass

        try:
            bokeh_tingy.xgrid.grid_line_alpha = 0.5
        except:
            pass

        try:
            bokeh_tingy.xgrid.grid_line_dash = [2,4]
        except:
            pass

        try:
            bokeh_tingy.ygrid.grid_line_alpha = 0.5
        except:
            pass

        try:
            bokeh_tingy.ygrid.grid_line_dash = [2,4]
        except:
            pass

        try:
            bokeh_tingy.toolbar.logo=None
        except:
            pass

        #try:

        return bokeh_tingy