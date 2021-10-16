from ipywidgets import interact, interactive, fixed, interact_manual,IntSlider
import ipywidgets as widgets
from ipywidgets import HBox, Label,VBox
from IPython.core.display import display
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd













class dashboard:
    def __init__(self):
        self.x1 = np.linspace(0, 2 * np.pi)
        plt.ioff() # turn off interactive mode so figure doesn't show
        self.fig1 = plt.figure()
        self.ax1 = self.fig1.add_subplot(1, 1, 1)
        plt.ion() # figure still doesn't show
        self.line1, = self.ax1.plot(self.x1, np.sin(self.x1))
        plt.ylim([-5,5])

        def update2(a = 10.0, b =1 ,c =0):
            self.line1.set_ydata( a* np.sin(b * self.x1 + c))
            self.fig1.canvas.draw_idle()
            

        self.a = widgets.IntSlider(min = 1 , max = 5)
        self.b = widgets.IntSlider(min = 1 , max = 5)
        self.c = widgets.IntSlider(min = 1 , max = 5)
        #ui = widgets.VBox([a, b, c])
        
        #w = widgets.interactive_output(update2, {"a": sl})
        self.out = widgets.interactive_output(update2, {'a': self.a, 'b': self.b, 'c': self.c})
        def update3():
            update2(self.a.value, self.b.value,  self.c.value )

        self.up = update3
        
    def display(self):
        plt.ioff() # turn off interactive mode so figure doesn't show
        self.fig1 = plt.figure()
        self.ax1 = self.fig1.add_subplot(1, 1, 1)
        plt.ion() # figure still doesn't show
        self.line1, = self.ax1.plot(self.x1, np.sin(self.x1))
        plt.ylim([-5,5])
        self.up()

        display(
            VBox([
                HBox([
                    self.fig1.canvas,  
                    VBox([
                        Label("amplitude"),
                        self.a, 
                        Label("omega"),
                        self.b, 
                        Label("phi"),
                        self.c 
                        ])
                    ])
                ])
                )

d = dashboard()