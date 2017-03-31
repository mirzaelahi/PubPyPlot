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
pub.updateRcParams()



pub.marker = ['o', 'd', 's']
pub.markerFaceColor= ['#d73027',     #red
                             '#4575b4',     #blue
                             '#fc8d59',     #orange
                             '#fee090',     #yellow
                             '#e0f3f8',     #skyblue
                             '#91bfdb'      #lightblue
                             ]

x = [1, 2, 3, 4, 5]
on_off = [8, 12, 500, 400, 470]

x_ER_5_Degree = [3, 4, 5]
on_off_ER_5_Degree = [114.58, 162.16, 112]

x_ER_24_Degree = [3, 4, 5]
on_off_ER_24_Degree = [16, 48.2, 23]

degreesymbol = u"\u00b0"

ms=5

pub.plot(x, on_off, ms=ms, ls='', markevery=1)
pub.plot(x_ER_5_Degree, on_off_ER_5_Degree, ms=ms, ls='', markevery=1)
pub.plot(x_ER_24_Degree, on_off_ER_24_Degree, ms=ms, ls='', markevery=1)

pub.setLabel(yLabel=r'$On-Off\ Ratio$')
pub.setTick(majorDx=1, majorDy=100)
pub.legend([r'$Ideal\ Edge (\sigma_{rand} \equal 0$' + degreesymbol+ ')', 
            r'$\sigma_{rand} = 5$' + degreesymbol, 
                      r'$\sigma_{rand} = 24$' + degreesymbol],
                        bbox_to_anchor=(-0.015, 1., 1.03, 1.102), loc= 3,
                        mode="expand", ncol=3,
                        frameon=True, shadow=False, fancybox=True)
xTickLabels = ['Single PNJ', 'GPNJ-WOT', 'GPNJ-WT', 'GPNJ-TG', 'GPNJ-Gen1']
pub.setTicks(xTicks=np.arange(1, 6))
pub.setTickLabel(xTickLabels=xTickLabels, xRotation=70)
pub.savePlot('marker', formats = ['png', 'eps'])
