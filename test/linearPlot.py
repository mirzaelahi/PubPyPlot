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

pub = PubPyPlot()
pub.formatAxes(pub.getAxis())

pub.markevery= [4 , 7, 5]
pub.lw = [1, 1, 2]
pub.markerSize = [4, 4, 5]

x = np.arange(1, 100, 1)
x1 = np.arange(1, 51, 1)
y = np.arange(1, 100, 1)
y1 = np.arange(100, 1, -1)
y2 = np.arange(50, 100, 1)

pub.plot(x,y)
pub.plot(x1,y2)
pub.plot(x,y1)

pub.setLabel(r'$E\ [eV]$',r'$T$')
pub.setTick(majorDx=20, majorDy=20)
pub.legend([r'$up$', r'$down$', r'$ud$'],frameon=True, shadow=True, fancybox=True)
pub.savePlot('linearplot', formats = ['png', 'eps'])
