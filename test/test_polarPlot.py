# -*- coding: utf-8 -*-
"""
Author:        Mirza Elahi (me5vp)
Changelog:     2017-03-13 v0.0.0
"""

import sys
from math import pi
import numpy as np
sys.path.append('../lib/')  # appending the path to PubPyPlot
from PubPyPlot import PubPyPlot
import matplotlib.pyplot as plt

pub = PubPyPlot(type='polar')
ax = pub.getAxis()


pub.markevery= [4 , 7, 5]
pub.lw = [1, 1, 2]
pub.markerSize = [0, 4, 5]

# data
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

# plot
pub.plot(theta, r)

# set radius limit
ax.set_rmax(2)

ax.grid(True)

# tick labels
pub.setTickLabel( xTickLabels=['0', '45', '90', '135', '180', '-135', '-90', 
                               '-45'], 
                            yTickLabels=[])

#save plot
pub.savePlot('polarPlot', formats = ['png', 'eps'])
