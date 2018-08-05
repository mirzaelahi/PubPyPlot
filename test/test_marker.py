# -*- coding: utf-8 -*-
"""
Author:        Mirza Elahi (me5vp)
Changelog:     2017-03-13 v0.0.0
"""

import sys
from math import pi
import numpy as np
sys.path.append('../lib/')          # appending the path to PubPyPlot
from PubPyPlot import PubPyPlot     # PubPyPlot Lib
import matplotlib.pyplot as plt

# take an instance of PuPyPlot
pub = PubPyPlot()
# if one changes any parameter related to core, s/he should do it here.
# update Rc params
pub.updateRcParams()

# color/marker setup
pub.marker = ['o', 'd', 's']
pub.markerFaceColor= ['#d73027',     #red
                     '#4575b4',     #blue
                     '#fc8d59',     #orange
                     '#fee090',     #yellow
                     '#e0f3f8',     #skyblue
                     '#91bfdb'      #lightblue
                     ]
# data
x1 = [1, 2, 3, 4, 5, 6, 7]
y1 = [8, 12, 500, 400, 470, 600, 55]

x2 = [3, 4, 5, 6, 7]
y2 = [114.58, 162.16, 112, 120, 53]

x3 = [3, 4, 5, 6, 7]
y3 = [16, 48.2, 23, 20, 51]

degreesymbol = pub.degreesymbol
ms=5
# plot
pub.plot(x1, y1,  ms=ms, ls='', markevery=1, zOrder=5)
pub.plot(x2, y2, ms=ms, ls='', markevery=1, zOrder=4)
pub.plot(x3, y3, ms=ms, ls='', markevery=1, zOrder=1)

# labels
pub.setLabel(yLabel=r'$value$')

# tick positions
pub.setTickDim(majorDx=1, majorDy=100)

# legend in a custom location with 3 column
pub.legend([r'$leg1$', r'$leg2$', r'$leg3$'], 
               bbox_to_anchor=(-0.015, 1., 1.03, 1.102), loc= 3,
               mode="expand", ncol=3,
               frameon=True, shadow=False, fancybox=True)

# custom xtick positions
pub.setTicks( xTicks=np.arange(1, 9) )

# custom xtick labels
xTickLabels = ['SJ', 'DJ', 'DJT', 'TG', 'DS', 'AJ', 'EL']
pub.setTickLabel(xTickLabels=xTickLabels, xRotation=70)

# limit
pub.setLimit(xLim=[0.5, 7.5], yLim=[-20, 650])

# save plot
pub.savePlot('marker', formats = ['png', 'eps'])
