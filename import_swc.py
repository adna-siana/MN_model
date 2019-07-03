### this file imports an swc 3d morphology file after which we add individual cell properties 

import sys 
sys.path.append('/Applications/NEURON-7.7/nrn/lib/python')
import os
wdir=os.getcwd()

'''
cell imported from this link: http://neuromorpho.org/neuron_info.jsp?neuron_name=CaP
2dpf CaP MN 
NeuroMorpho.Org ID : 	NMO_09367
'''

from netpyne.support import morphology
from neuron import h
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import platform
import neuron as nrn
if platform.system() == 'Windows':
    nrn.load_mechanisms(os.path.join(wdir + 'Morph_practice', 'modfiles'))
    import sys
    sys.path.append('C:', 'nrn', 'lib', 'python')
    sys.path.append('D:', 'Okinawa', 'Python')
    sys.path.append(wdir + 'Morph_practice', 'modfiles')


#load cell as mycell
myCell= morphology.Cell()
morphology.load(filename=os.path.join(wdir, 'MN_morphology.swc'), cell=myCell)

#plot loaded cell
fig = plt.figure()
ax = plt.axes(projection='3d')
morphology.shapeplot(h, ax)

#get the sections from the cell
secs=list(h.allsec());
secs_all = secs
soma = []
axon = []
dend = []

    
    #get the sections from soma, axon and dend
for sec in secs:
    name = sec.name()   
    if name[0:4] == 'soma':
        soma.append(sec)
    if name[0:4] == 'axon':
        axon.append(sec)
    if name[0:4] == 'dend':
        dend.append(sec)
          
#def __init__(self):
    #self.add_biophys

    #give the cell biphys props
def add_biophys_soma(soma):       
    for sec in soma:
        sec.insert('hh')
        #sec.insert('na')
    
def add_biophys_axon(axon):   
    for sec in axon:
        sec.insert('hh')
        
def add_biophys_dend(dend):       
    for sec in dend:
        sec.insert('pas')
        
        
        
        