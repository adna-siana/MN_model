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
myCell_1= morphology.Cell()
morphology.load(filename=os.path.join(wdir, 'MN1_morphology.swc'), cell=myCell_1)
 
cell1_secs=list(h.allsec())

lenght_1 = len (cell1_secs)

myCell_2= morphology.Cell()
morphology.load(filename=os.path.join(wdir, 'MN2_morphology.swc'), cell=myCell_2)

cell2_secs=list(h.allsec())
del cell2_secs[0:lenght_1]

lenght_2 = len (cell2_secs)

myCell_3= morphology.Cell()
morphology.load(filename=os.path.join(wdir, 'MN3_morphology.swc'), cell=myCell_2)

cell3_secs=list(h.allsec())
del cell3_secs[0:lenght_1]
del cell3_secs[0:lenght_2]

lenght_3 = len (cell3_secs)


myCell_4= morphology.Cell()
morphology.load(filename=os.path.join(wdir, 'MN4_morphology.swc'), cell=myCell_2)

cell4_secs=list(h.allsec())
del cell4_secs[0:lenght_1]
del cell4_secs[0:lenght_2]
del cell4_secs[0:lenght_3]

#plot loaded cell
fig = plt.figure()
ax = plt.axes(projection='3d')
morphology.shapeplot(h, ax, sections = cell1_secs, color='k' )
morphology.shapeplot(h, ax, sections = cell2_secs, color='b' )
morphology.shapeplot(h, ax, sections = cell3_secs, color='r' )
morphology.shapeplot(h, ax, sections = cell4_secs, color='m' )



