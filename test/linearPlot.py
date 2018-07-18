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

pub = PubPyPlot(ratio=12)
pub.formatAxes(pub.getAxis())

pub.markevery= [4, 7, 5]
pub.lw = [4, 0.5, 2]
pub.markerSize = [4, 4, 5]
pub.font = 'Times New Roman'
pub.fontFamily = 'Times New Roman'

pub.updateRcParams()

x = np.arange(1, 100, 2)
x1 = np.arange(1, 51, 2)
y = np.arange(1, 100, 2)
y1 = np.arange(100, 1, -2)
y2 = np.arange(50, 100, 2)

pub.plot(x,y, zOrder=10)
pub.plot(x1,y2)
pub.plot(x,y1, zOrder=-2)

pub.setLabel(r'$E\ [eV]$',r'$T$')
pub.setTickDim(majorDx=20, majorDy=20)
pub.legend([r'$up$', r'$down$', r'$ud$'], frameon=True, shadow=True, fancybox=True)
pub.savePlot('linearplot', formats = ['png', 'eps'])
