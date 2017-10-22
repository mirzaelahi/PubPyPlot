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
#pub.formatAxes(pub.getAxis())
ax = pub.getAxis()

pub.markevery= [4 , 7, 5]
pub.lw = [1, 1, 2]
pub.markerSize = [0, 4, 5]

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

pub.plot(theta, r)
ax.set_rmax(2)
#ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
#ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

#plt.show()

#pub.setLabel(r'$E\ [eV]$',r'$T$')
pub.setTickLabel(xTickLabels=['0', '45', '90', '135', '180', '-135', '-90', '-45'], yTickLabels=[])
#pub.setTick(majorDx=20, majorDy=20)
#pub.legend([r'$up$', r'$down$', r'$ud$'],frameon=True, shadow=True, fancybox=True)
pub.savePlot('polarPlot', formats = ['png', 'eps'])
