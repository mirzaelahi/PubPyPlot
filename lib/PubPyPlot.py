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
    def __init__(self, height = None, width = None, ratio=None):
        """constructor of the class"""
        self.goldenMean = ( np.sqrt(5) - 1.0 )/2.0
        if ratio==21:
            self.figWidth = 3.39
            self.figHeight = self.figWidth * self.goldenMean
        elif ratio==12:
            self.figWidth = 3.39
            self.figHeight = self.figWidth * self.goldenMean
            self.figWidth = 3.39/2.0
        elif ratio==11:
            self.figWidth = 3.39/2
            self.figHeight = 3.39/2
        if ratio is None and width is None:
            self.figWidth = 3.39
            #else:
            #self.figWidth = width
    
        if ratio is None and height is None:
            self.figHeight = self.figWidth * self.goldenMean
        elif height is not None and width is not None:
            self.figHeight = height
            self.figWidth = width
            
        self.plotCount = 0
        self.totalPlotProvision = 6   
        self.labelFontSize = 6.0
        self.legendFontSize = self.labelFontSize
        self.tickFontSize = self.labelFontSize
        self.legend_lw = 2.5/2.1
        self.lw = 2.5*np.ones(self.totalPlotProvision)
        self.axesColor = '#000000'
        self.majorTickWidth = 0.4
        self.majorTickLength = 2.7
        self.minorTickLength = self.majorTickLength * 0.7
        self.axesLineWidth = 0.4
        self.axesLabelpad = 1.5
        self.tickPad = 3
        self.ls='-'
        self.fontFamily = 'serif'
        self.font = 'Arial Narrow'
        
        self.legendLineLength = 2.5
        self.legendLineWidth = 1.2*np.ones(self.totalPlotProvision)
        self.legendNumPoints = 1
        self.legendLabelSpacing = 0.1
        self.legendBorderaxespad = 0.5
        self.legendHandleTextPad = 0.5
        self.legendBorderPad = 0.4
        self.legendText = ''
        self.legendHandleHeight = 0.5
        self.legendBbox_to_anchor = (1., 1.)
        self.markerAlpha = 1.
        self.markerEdgeWidth = 0.5*np.ones(self.totalPlotProvision)
        self.dashes = [3, 2, 3, 2]  # 3 points on, 2 off, 3 on, 2 off
        
        
        self.color = ['#ef1616',     #red
                             '#0e59ac',     #blue
                             '#567d53',     #green
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
                             #orange fc8d59
        self.markerSize = np.zeros(self.totalPlotProvision)
        self.marker = ['o', 's', '+', 'x', '2', 'h']
        self.markevery = 1*np.ones(self.totalPlotProvision)
        
        self.plotList = []
        
        
        
        # INITIATE FIGURE
        self.fig = plt.figure(figsize=(self.figWidth, self.figHeight))
        self.ax = self.fig.add_subplot(111)
        #self.fig.subplots_adjust(left=0.2, bottom=0.2)
        
        # SET TICK FONT // TODO
        for label in self.ax.get_xticklabels():
            label.set_fontproperties(self.font)

        for label in self.ax.get_yticklabels():
            label.set_fontproperties(self.font)
        self.updateRcParams()
        
    def updateRcParams(self):
        params = {'axes.labelsize': self.labelFontSize, 
                      'axes.titlesize': self.labelFontSize,
                      'font.size': self.labelFontSize,
                      'legend.fontsize': self.legendFontSize,
                      'xtick.labelsize': self.tickFontSize,
                      'ytick.labelsize': self.tickFontSize,
                      'axes.labelpad'  : self.axesLabelpad,
                      'font.family' : self.fontFamily,
                      'font.serif' : self.font,
                      'mathtext.fontset': 'custom',
                      'mathtext.rm': self.font,
                      'mathtext.it': self.font,
                      'mathtext.bf': self.font,
                      'font.family' : self.font}
        rcParams.update(params)
        
    def getAxis(self):
        """returns axis"""
        return self.ax
        
    def plot(self, x, y, lw=None, color=None, marker=None, ms=None,
             markevery=None, markeredgecolor=None, markerfacecolor=None, 
                 markeredgewidth=None, ls='-', zOrder=1, dashes=None):
        """plot x vs y"""
        color = color or self.color[self.plotCount]
        ms = ms or self.markerSize[self.plotCount]
        marker = marker or self.marker[self.plotCount]
        markevery = markevery or self.markevery[self.plotCount]
        markeredgecolor = markeredgecolor or self.markerEdgeColor[self.plotCount]
        markerfacecolor = markerfacecolor or self.markerFaceColor[self.plotCount]
        markeredgewidth = markeredgewidth or self.markerEdgeWidth[self.plotCount]
        dashes = dashes or self.dashes
        if ls == '-':
            dashes = ''
        
        lw = lw or self.lw[self.plotCount]
        tempPlot, = self.ax.plot(x, y, lw=lw, 
                             color=color, ms=ms, marker=marker, 
                             markevery=markevery, 
                             markeredgecolor=markeredgecolor,
                             markerfacecolor=markerfacecolor,
                             markeredgewidth = markeredgewidth,
                             ls=ls,
                             zorder=zOrder,
                             dashes = dashes)
        self.plotCount += 1
        self.plotList.append(tempPlot)
        return tempPlot
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
            
    def setLabel(self, xLabel=None, yLabel=None, labelpad=None):
        """set labels"""
        labelpad = labelpad or self.axesLabelpad
        if xLabel is not None:
            self.ax.set_xlabel(xLabel, labelpad=labelpad)
        if yLabel is not None:
            self.ax.set_ylabel(yLabel, labelpad=labelpad+1)
        
    def setTick( self, tickLength=None, tickWidth=None, majorDx=None, 
                majorDy=None, minorDx=None, minorDy=None, tickFontsize=None,
                tickPad=None):
        """modify ticks"""
        tickLength = tickLength or self.majorTickLength
        tickWidth = tickWidth or self.majorTickWidth
        tickFontsize = tickFontsize or self.tickFontSize
        tickPad = tickPad or self.tickPad
        # Tick Size
        self.ax.xaxis.set_tick_params(length=tickLength, width=tickWidth, 
                                      labelsize=tickFontsize)
        self.ax.yaxis.set_tick_params(length=tickLength, width=tickWidth, 
                                      labelsize=tickFontsize)
        self.ax.xaxis.set_tick_params(which='minor', length=0.5*tickLength,
                                      width=0.8*tickWidth)
        self.ax.yaxis.set_tick_params(which='minor', length=0.5*tickLength,
                                      width= 0.8*tickWidth)
        self.ax.xaxis.set_tick_params(which='major', length=tickLength, 
                                      width=tickWidth, pad=tickPad )
        self.ax.yaxis.set_tick_params(which='major', length=tickLength, 
                                      width=tickWidth, pad=tickPad)
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
            
    def legend(self, legendText,  handle=None, bbox_to_anchor=None, loc='upper right', 
               frameon=False, fancybox=False, shadow = False, ncol=1,
               mode=None, handletextpad=None, framealpha = 1.):
        self.legendText = legendText
        handle = handle or self.plotList
        handletextpad = handletextpad or self.legendHandleTextPad
        self.legend = self.ax.legend(handle, legendText,
                                     loc=loc,
                                     bbox_to_anchor = bbox_to_anchor,
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
                                     handleheight=self.legendHandleHeight,
                                     framealpha= framealpha)
                                     
        self.legend.get_frame().set_linewidth(self.axesLineWidth)
        self.legend.get_frame().set_edgecolor(self.axesColor)
        tempCount = 0
        for legobj in self.legend.legendHandles:
            legobj.set_linewidth(self.legendLineWidth[tempCount])
            tempCount += 1
        return self.legend   
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
                
    def setLimit(self, xLim=None, yLim=None):
        if xLim is not None:
            self.ax.set_xlim(xLim)
        if yLim is not None:
            self.ax.set_ylim(yLim)

    
