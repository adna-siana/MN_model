#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:14:36 2019

@author: adna.dumitrescu
"""

### this file imports an swc 3d morphology file after which we add individual cell properties 

import sys 
sys.path.append('/Applications/NEURON-7.7/nrn/lib/python')
import os
wdir=os.getcwd()

'''
cell imported from this link: http://neuromorpho.org/neuron_info.jsp?neuron_name=CaP-WT-Kv3-3
2dpf CaP MN 
NeuroMorpho.Org ID : 	NMO_09364
'''

from netpyne.support import morphology
from netpyne import sim
from neuron import h
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import platform
import neuron as nrn

#load cell as mycell
#def getmorph(self):
myCell= morphology.Cell()
morphology.load(filename=os.path.join(wdir, 'MN2_morphology.swc'), cell=myCell)

#plot loaded cell
fig = plt.figure()
ax = plt.axes(projection='3d')
morphology.shapeplot(h, ax)
           
#get the sections from the cell
secs=list(h.allsec());
secs_all = secs
soma = []
axon = []
#dend = []


    #get the sections fro soma, axon and dend
    #def getset(self):
for sec in secs:
    name = sec.name()   
    if name[0:4] == 'soma':
        soma.append(sec)
    if name[0:4] == 'axon':
        axon.append(sec)
    #if name[0:4] == 'dend':
        #dend.append(sec)



class TC_cell():

    def __init__(self):
            
            self.add_biophys_axon()
            self.add_biophys_soma()
            #self.add_biophys_dend()
            self.add_biophys_all()
            #self.getmorph()
            #self.getset()
    

    #give the cell biphys props
    def add_biophys_soma(self):       
        for sec in soma:
            sec.insert('hh')
            #sec.insert('na')
            #sec.insert('kv')
            
        #sec.insert('na')
    
    def add_biophys_axon(self):   
        for sec in axon:
            sec.insert('hh')
            #sec.insert('na')
            #ßsec.insert('kv')
        
    #def add_biophys_dend(self):       
      #  for sec in dend:
       #     sec.insert('pas')
    
    def add_biophys_all(self):  
        for sec in h.allsec():
            sec.Ra = 100    # Axial resistance in Ohm * cm
            sec.cm = 0.01      # Membrane capacitance in micro Farads / cm^2
        
        
    add_biophys_soma(soma)
    add_biophys_axon(axon)
    #add_biophys_dend(dend)


def MakeCell():
    TC = TC_cell()
    return TC
