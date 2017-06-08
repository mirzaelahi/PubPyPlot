# -*- coding: utf-8 -*-
#!/usr/bin/python

import matplotlib
#from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio

from math import pi
from matplotlib import rcParams
from matplotlib import rc


import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
#from matplotlib import animation

import numpy as np
#from math import pi, sqrt, sin, cos, tan
from sets import Set
import pickle
import sys
import os
import shutil
import operator as op
import time
import argparse
import scipy.io as sio
from matplotlib.ticker import MultipleLocator

# Constants
vf 			= 1E6		# Fermi velocity
q           = 1.6E-19
h           = 6.634E-34
hbar        = h / (2*pi)

def convert_V2_to_n2( x ) :
    return (np.multiply( np.sign(x), np.square( q * x ) )/ ( pi * hbar**2 * vf**2 ) )

def setTickSize( axes, length=8, width=1, dx=1, dy=1, fontsize=14 ):
    # Tick Size
    axes.xaxis.set_tick_params(length=length, width=width, labelsize=fontsize)
    axes.yaxis.set_tick_params(length=length, width=width, labelsize=fontsize)
    axes.xaxis.set_tick_params(which='minor', length=length/2.0, width=0.8*width)
    axes.yaxis.set_tick_params(which='minor', length=length/2.0, width=0.8*width)
    # Minor Tick
    mlx = MultipleLocator(dx)
    axes.xaxis.set_minor_locator(mlx)
    mly = MultipleLocator(dy)
    axes.yaxis.set_minor_locator(mly)


# LOADING MAT DATA

# MT /um [4q^2/h]
# V1
# V2



#allPlottingDataStruct = allPlottingData[ 'allPlottingData' ]

#print allPlottingData

#x = [1, 2, 3, 4, 5, 6]
#on_off = [8, 12, 500, 400, 470, 670]

x = [1, 2, 3, 4, 5]
on_off = [8, 12, 500, 400, 470]

x_ER_5_Degree = [3, 4, 5]
on_off_ER_5_Degree = [114.58, 162.16, 112]

x_ER_24_Degree = [3, 4, 5]
on_off_ER_24_Degree = [16, 48.2, 23]

# INITIATING FIGURE
fig = plt.figure(figsize=(6, 4.5))
axes = fig.add_subplot(111)

# ADJUSTING MARGIN
fig.subplots_adjust(left=0.0, bottom=0.2)

markedgw = 2.0


## PP PLOT
#XX = -np.array(vd).transpose()
#print XX.shape
#print Id.shape
lww =3.0

degreesymbol = u"\u00b0"

## Single Junction
plt.plot( x, on_off, 'ro', \
               markersize=10, linewidth=lww, label=r'$Ideal\ Edge (\sigma_{rand} \equal 0$' + degreesymbol+ ')')

plt.plot( x_ER_5_Degree, on_off_ER_5_Degree, 'gd', \
         markersize=10, linewidth=lww, label=r'$\sigma_{rand} = 5$' + degreesymbol)

plt.plot( x_ER_24_Degree, on_off_ER_24_Degree, 'bs', \
         markersize=10, linewidth=lww, label=r'$\sigma_{rand} = 24$' + degreesymbol)

labels = ['Single PNJ', 'GPNJ - WOT', 'GPNJ-WT', 'GPNJ-TG', 'GPNJ-Gen1', 'GPNJ4-Abrupt']


legend = axes.legend(bbox_to_anchor=(0., 1.05, 1., 1.102), loc=3,
                   ncol=3, mode="expand", borderaxespad=0.1, shadow=True, labelspacing=0.15, borderpad=0.3, fancybox=True, numpoints=1, handletextpad=-0.3) # setting legend

plt.ylabel(r'$On-Off\ Ratio$', fontsize=16)

## font style
params = {'mathtext.default': 'regular' }
rcParams.update(params)
#
## Limits
plt.xlim(0.5, 6.5)
plt.ylim(0, 700)
## Ticks
plt.xticks(fontsize = 14)
plt.yticks( fontsize = 14)


axes.get_xaxis().set_ticks(np.array([1, 2, 3, 4, 5, 6]))
axes.get_yaxis().set_ticks(np.array([0, 200, 400, 600]))
labels_y = [item.get_text() for item in axes.get_yticklabels()]
labels_x = [item.get_text() for item in axes.get_xticklabels()]
#print labels_x
#print labels_y
x_string_labels = [ r'$-6$', r'$-3$', r'$0$', r'$3$', r'$6$' ]
y_string_labels = [r'$0$',  r'$200$', r'$400$',  r'$600$' ]
axes.set_yticklabels(y_string_labels)
axes.set_xticklabels(labels, rotation=70)
setTickSize( axes, length=5, width=1, dx=1, dy=100, fontsize=14 )
## tick position
axes.xaxis.set_ticks_position("bottom")
axes.yaxis.set_ticks_position("left")
#
# SAVE FILE
    # PNG
pngFile="comparison_on_off_WER"
tmppngFile = pngFile + ".png"
plt.savefig(tmppngFile, dpi=600, bbox_inches='tight')
    # EPS
tmppngFile = pngFile + ".eps"
plt.savefig(tmppngFile, dpi=600, bbox_inches='tight')

