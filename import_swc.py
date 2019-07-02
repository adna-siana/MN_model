#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:30:54 2019

@author: adna.dumitrescu
"""

import sys 
sys.path.append('/Applications/NEURON-7.7/nrn/lib/python')



from netpyne.support import morphology
from neuron import h
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import neuron as nrn



myCell= morphology.Cell()
morphology.load(filename='/Users/adna.dumitrescu/Documents/Wyart_Postdoc/OIST_2019/MN_model/MN_morphology.swc', cell=myCell)

fig = plt.figure()
ax = plt.axes(projection='3d')
morphology.shapeplot(h, ax)


fig = plt.figure()
ax = plt.axes(projection='3d')
secs=list(h.allsec());
axon=h.Section(name='axon')
axon=[h.Section(name='axon[%d]' % i) for i in range(1,5)]
morphology.shapeplot(h, ax, axon)
