# -*- coding: utf-8 -*-
"""
Author:        Mirza Elahi (me5vp)
Changelog:     2017-03-13 v0.0.0
"""

import sys
from math import pi
import numpy as np
sys.path.append('../lib/')          # appending the path to PubPyPlot
from PubPyPlot import PubPyPlot     # PubPyPlot

# take an instance of PuPyPlot
# ratio can be 21, 12, 11 meaning width by height
# one may put custom height and width as well
pub = PubPyPlot(ratio=21)

# parameters, if one changes any parameter related to core, .
# s/he should do it here.
# the below three parameter values will be taken as input ...
# for plot function serially
# i.e. first linewidth is 1.0, ...
# second linewidth is 0.5
# you may put lw parameter for each plot function  ...
# individually as well
pub.markevery= [0, 10, 5]
pub.lw = [1, 0.5, 2]
pub.markerSize = [0, 3, 5]

# update plot settings (Rc params)
pub.updateRcParams()

# data
x1 = np.arange(-pi, pi, pi/100)
x2 = np.arange(-pi, pi, pi/100)
y1 = np.sin( x1 )
y2 = np.cos( x2 )

# plot
pub.plot(x1*180/pi, y1)
pub.plot(x2*180/pi, y2)

# labels with latex support
pub.setLabel(xLabel=r'$angle\ (degree)$', yLabel=r'$value$')

# legend
pub.legend([r'$sin$', r'$cos$'], frameon=False, shadow=False,
               fancybox=False, loc='upper left')

# save plot
pub.savePlot('fileName', formats = ['png', 'eps'])
