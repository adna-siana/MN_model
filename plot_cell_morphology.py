#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 21:27:34 2019

@author: adna.dumitrescu
"""

import sys 
sys.path.append('/Applications/NEURON-7.7/nrn/lib/python')
import os
wdir=os.getcwd()

from netpyne.support import morphology
from netpyne import sim
from neuron import h
import matplotlib.pyplot as plt
import matplotlib.cm
from mpl_toolkits import mplot3d
import platform
import neuron as nrn


#load cell as mycell
#    def getmorph(self):
#myCell_1= morphology.Cell()
#morphology.load(filename=os.path.join(wdir, 'MN1_morphology.swc'), cell=myCell_1)
 
#cell1_secs=list(h.allsec())

myCell_2= morphology.Cell()
morphology.load(filename=os.path.join(wdir, 'MN2_morphology.swc'), cell=myCell_2)

cell2_secs=list(h.allsec()

#plot loaded cell
fig = plt.figure()
ax = plt.axes(projection='3d')
morphology.shapeplot(h, ax, sections = cell2_secs, color='k' )
#morphology.shapeplot(h, ax, sections = cell2_secs, color='b' )




