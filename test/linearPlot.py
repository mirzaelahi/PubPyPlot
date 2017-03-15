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

x = np.arange(1, 100, 1)
y = np.arange(1, 100, 1)
y1 = np.arange(100, 1, -1)

pub.plot(x,y)
pub.plot(x,y1)
pub.setLabel(r'$E\ [eV]$',r'$T$')
pub.setTick(majorDx=20, majorDy=20)
pub.savePlot('linearplot', formats = ['png', 'eps'])
