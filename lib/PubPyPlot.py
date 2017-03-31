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
#from sets import Set
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
            
        self.plotCount = 0
        self.totalPlotProvision = 6   
        self.labelFontSize = 6.5
        self.legendFontSize = self.labelFontSize - 0.3
        self.tickFontSize = self.labelFontSize - 0.3
        self.legend_lw = 2.5/2
        self.lw = 2.5*np.ones(self.totalPlotProvision)
        self.axesColor = '#424242'
        self.majorTickWidth = 0.5
        self.majorTickLength = 3
        self.minorTickLength = 2.5
        self.axesLineWidth = 0.5
        self.axesLabelpad = 4
        self.ls='-'
        
        self.fig = plt.figure(figsize=(self.figWidth, self.figHeight))
        self.ax = self.fig.add_subplot(111)
        
        self.legendLineLength = 1.5
        self.legendLineWidth = 1.5*np.ones(self.totalPlotProvision)
        self.legendNumPoints = 1
        self.legendLabelSpacing = 0.5
        self.legendBorderaxespad = 0.5
        self.legendHandleTextPad = 0.5
        self.legendBorderPad = 0.4
        self.legendText = ''
        self.legendHandleHeight = 0.5
        self.legendBbox_to_anchor = (0., 0., 0., 0.) 
        self.markerAlpha = 1.
        self.markerEdgeWidth = 0.5*np.ones(self.totalPlotProvision)
        
        
        self.color = ['#d73027',     #red
                             '#4575b4',     #blue
                             '#fc8d59',     #orange
                             '#fee090',     #yellow
                             '#e0f3f8',     #skyblue
                             '#91bfdb'      #lightblue
                             ]
        self.markerEdgeColor = ['#8A201A',     #red
                             '#2A476D',     #blue
                             '#A9603E',     #orange
                             '#fee090',     #yellow
                             '#e0f3f8',     #skyblue
                             '#91bfdb'      #lightblue
                             ]
                             
        self.markerFaceColor=['#D68480',     #red
                             '#8196B1',     #blue
                             '#FEBFA1',     #orange
                             '#FEE8AE',     #yellow
                             '#EAF5F7',     #skyblue
                             '#B7CEDC'      #lightblue
                             ]
        self.markerSize = np.zeros(self.totalPlotProvision)
        self.marker = ['o', 's', '+', 'x', '2', 'h']
        self.markevery = 1*np.ones(self.totalPlotProvision)
        
        self.plotList = []
        
        #self.fig.subplots_adjust(left=0.2, bottom=0.2)
        self.updateRcParams()
        
    def updateRcParams(self):
        params = {'axes.labelsize': self.labelFontSize, 
                      'axes.titlesize': self.labelFontSize,
                      'font.size': self.labelFontSize,
                      'legend.fontsize': self.legendFontSize,
                      'xtick.labelsize': self.tickFontSize,
                      'ytick.labelsize': self.tickFontSize,
                      'axes.labelpad'  : self.axesLabelpad, 
                      'mathtext.default': 'regular'}        
        rcParams.update(params)
        
    def getAxis(self):
        """returns axis"""
        return self.ax
        
    def plot(self, x, y, lw=None, color=None, marker=None, ms=None, 
             markevery=None, markeredgecolor=None, markerfacecolor=None, 
                 markeredgewidth=None, ls='-'):
        """plot x vs y"""
        color = color or self.color[self.plotCount]
        ms = ms or self.markerSize[self.plotCount]
        marker = marker or self.marker[self.plotCount]
        markevery = markevery or self.markevery[self.plotCount]
        markeredgecolor = markeredgecolor or self.markerEdgeColor[self.plotCount]
        markerfacecolor = markerfacecolor or self.markerFaceColor[self.plotCount]
        markeredgewidth = markeredgewidth or self.markerEdgeWidth[self.plotCount]
        lw = lw or self.lw[self.plotCount]
        tempPlot, = self.ax.plot(x, y, lw=lw, 
                             color=color, ms=ms, marker=marker, 
                             markevery=markevery, 
                             markeredgecolor=markeredgecolor,
                             markerfacecolor=markerfacecolor,
                             markeredgewidth = markeredgewidth,
                             ls=ls)
        self.plotCount += 1
        self.plotList.append(tempPlot)
        
    def show(self):
        """show the plot"""
        plt.show()
        
    def formatAxes(self, ax):
        """formats the axis
                - tick marks
                - tick position
        """
        #for spine in ['top', 'right']:
        #    ax.spines[spine].set_visible(False)
    
        for spine in ['left', 'bottom', 'top', 'right']:
            ax.spines[spine].set_color(self.axesColor)
            ax.spines[spine].set_linewidth(self.axesLineWidth)
    
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
    
        for axis in [ax.xaxis, ax.yaxis]:
            axis.set_tick_params(direction='in', color=self.axesColor)
    
        return ax
        
    def savePlot( self, file_name, formats = ['png'], mdpi=600 ):
        """saveplots"""
        for format in formats:
            title = '{0}.{1}'.format(file_name, format)
            print ('-> Saving file {0} with {1} dpi'.format(title, mdpi) )
            self.fig.savefig(title, dpi=mdpi, bbox_inches='tight')
            
    def setLabel(self, xLabel=None, yLabel=None):
        """set labels"""
        if xLabel is not None:
            self.ax.set_xlabel(xLabel)
        if yLabel is not None:
            self.ax.set_ylabel(yLabel)
        
    def setTick( self, tickLength=None, tickWidth=None, majorDx=None, 
                majorDy=None, minorDx=None, minorDy=None, tickFontsize=None ):
        """modify ticks"""
        tickLength = tickLength or self.majorTickLength
        tickWidth = tickWidth or self.majorTickWidth
        tickFontsize = tickFontsize or self.tickFontSize
        # Tick Size
        self.ax.xaxis.set_tick_params(length=tickLength, width=tickWidth, 
                                      labelsize=tickFontsize)
        self.ax.yaxis.set_tick_params(length=tickLength, width=tickWidth, 
                                      labelsize=tickFontsize)
        self.ax.xaxis.set_tick_params(which='minor', length=0.7*tickLength, 
                                      width=0.83*tickWidth)
        self.ax.yaxis.set_tick_params(which='minor', length=0.7*tickLength, 
                                      width=tickWidth)
        self.ax.xaxis.set_tick_params(which='major', length=tickLength, 
                                      width=0.83*tickWidth)
        self.ax.yaxis.set_tick_params(which='major', length=tickLength, 
                                      width=tickWidth)
        # Major Tick location                              
        if majorDx is not None:
            # Minor Tick
            Mlx = MultipleLocator(majorDx)
            self.ax.xaxis.set_major_locator(Mlx)
        if majorDy is not None:
            Mly = MultipleLocator(majorDy)
            self.ax.yaxis.set_major_locator(Mly)
        # Minor Tick location                              
        if minorDx is not None:
            # Minor Tick
            mlx = MultipleLocator(minorDx)
            self.ax.xaxis.set_minor_locator(mlx)
        if minorDy is not None:
            mly = MultipleLocator(minorDy)
            self.ax.yaxis.set_minor_locator(mly)
            
    def legend(self, legendText, bbox_to_anchor=None, loc='upper right', 
               frameon=False, fancybox=False, shadow = False, ncol=1,
               mode=None, handletextpad=None):
        self.legendText = legendText
        bbox_to_anchor = bbox_to_anchor or self.legendBbox_to_anchor
        handletextpad = handletextpad or self.legendHandleTextPad
        self.legend = self.ax.legend(self.plotList, legendText,
                                     bbox_to_anchor = bbox_to_anchor,
                                     loc=loc, 
                                     borderaxespad=self.legendBorderaxespad, 
                                     shadow=shadow, 
                                     labelspacing=self.legendLabelSpacing, 
                                     borderpad=self.legendBorderPad, 
                                     fancybox=fancybox, 
                                     handletextpad=handletextpad, 
                                     frameon=frameon, 
                                     ncol = ncol,
                                     mode = mode,
                                     numpoints=self.legendNumPoints, 
                                     handlelength=self.legendLineLength,
                                     handleheight=self.legendHandleHeight)
                                     
        self.legend.get_frame().set_linewidth(self.axesLineWidth)
        self.legend.get_frame().set_edgecolor(self.axesColor)
        tempCount = 0
        for legobj in self.legend.legendHandles:
            legobj.set_linewidth(self.legendLineWidth[tempCount])
            tempCount += 1
            
    def setTickLabel(self, xTickLabels=None, yTickLabels=None, xRotation=0,
                             yRotation=0):
        # x tick labels
        if xTickLabels is not None:
            self.ax.set_xticklabels(xTickLabels, rotation=xRotation)
        # y tick labels
        if yTickLabels is not None:
            self.ax.set_yticklabels(yTickLabels, rotation=yRotation)
            
    def setTicks(self, xTicks=None, yTicks=None):
        # x tick 
        if xTicks is not None:
            self.ax.get_xaxis().set_ticks(xTicks)
        # y tick 
        if yTicks is not None:
            self.ax.get_yaxis().set_ticks(yTicks)
    
