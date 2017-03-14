# -*- coding: utf-8 -*-
""" 
This module offers class for plotting

Author:        Mirza Elahi (me5vp)
Changelog:     2017-03-13 v0.0
"""

import matplotlib
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio

from math import pi
from matplotlib import rcParams
from matplotlib import rc

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from matplotlib import animation

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

class PubPyPlot(object):
    def __init__(self, height = None, width = None):
        """constructor of the class"""
        if width is None:
            self.figWidth = 3.39
        else:
            self.figWidth = width
        self.goldenMean = ( np.sqrt(5) - 1.0 )/2.0
        if height is None:
            self.figHeight = self.figWidth * self.goldenMean
        else:
            self.figHeight = height
        self.labelFontSize = 8
        self.tickFontSize = 8
        self.legend_lw = 2.5/2
        self.lw = 2.5
        self.SPINE_COLOR = '#424242'
        self.tickWidth = 0.5
        self.tickLength = 4
        
        self.fig = plt.figure(figsize=(self.figWidth, self.figHeight))
        self.ax = self.fig.add_subplot(111)
        #self.fig.subplots_adjust(left=0.2, bottom=0.2)
        params = {'text.latex.preamble': ['\usepackage{amsmath}'],
                      'axes.labelsize': self.labelFontSize, # fontsize for x and y labels (was 10)
                      'axes.titlesize': self.labelFontSize,
                      'font.size': self.labelFontSize, # was 10
                      'legend.fontsize': self.labelFontSize, # was 10
                      'xtick.labelsize': self.tickFontSize,
                      'ytick.labelsize': self.tickFontSize,
                      'font.family': 'serif',
                      'mathtext.default': 'regular'
            }        
        rcParams.update(params)
    def getAxis(self):
        """returns axis"""
        return self.ax
        
    def plot(self, x, y):
        """plot x vs y"""
        plt.plot(x, y, lw=self.lw)
        
    def show(self):
        """show the plot"""
        plt.show()
        
    def format_axes(self, ax):
        """formats the axis
                - tick marks
                - tick position
        """
        #for spine in ['top', 'right']:
        #    ax.spines[spine].set_visible(False)
    
        for spine in ['left', 'bottom', 'top', 'right']:
            ax.spines[spine].set_color(self.SPINE_COLOR)
            ax.spines[spine].set_linewidth(0.5)
    
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
    
        for axis in [ax.xaxis, ax.yaxis]:
            axis.set_tick_params(direction='in', color=self.SPINE_COLOR)
    
        return ax
        
    def savePlot( self, file_name, formats = ['png'], mdpi=600 ):
        """saveplots"""
        for format in formats:
            title = '{0}.{1}'.format(file_name, format)
            print '-> Saving file {0} with {1} dpi'.format(title, mdpi)
            self.fig.savefig(title, dpi=mdpi, bbox_inches='tight')
            
    def setLabel(self, xlabel, ylabel):
        """set labels"""
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
    def setTickSize( self, length=None, width=None, dx=None, dy=None, fontsize=None ):
        """modify ticks"""
        length = length or self.tickLength
        width = width or self.tickWidth
        fontsize = fontsize or self.tickFontSize
        # Tick Size
        self.ax.xaxis.set_tick_params(length=length, width=width, labelsize=fontsize)
        self.ax.yaxis.set_tick_params(length=length, width=width, labelsize=fontsize)
        self.ax.xaxis.set_tick_params(which='minor', length=length/2.0, width=0.8*width)
        self.ax.yaxis.set_tick_params(which='minor', length=length/2.0, width=0.8*width)
        if dx is not None:
            # Minor Tick
            mlx = MultipleLocator(dx)
            self.ax.xaxis.set_minor_locator(mlx)
        if dy is not None:
            mly = MultipleLocator(dy)
            self.ax.yaxis.set_minor_locator(mly)