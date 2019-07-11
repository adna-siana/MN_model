'''
set up network parameters 
'''
import sys 
sys.path.append('/Applications/NEURON-7.7/nrn/lib/python')


from netpyne import specs, sim

try:
	from __main__ import cfg  # import SimConfig object with params from parent module
except:
	from cfg import cfg  # if no simConfig in parent module, import directly from tut8_cfg module

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

## Population parameters
netParams.popParams['MN1'] = {'cellType': 'PMN1', 'numCells': 1, 'cellModel': 'HH'}
netParams.popParams['MN2'] = {'cellType': 'PMN2', 'numCells': 1, 'cellModel': 'HH'}
netParams.popParams['MN3'] = {'cellType': 'PMN3', 'numCells': 1, 'cellModel': 'HH'}
netParams.popParams['MN4'] = {'cellType': 'PMN4', 'numCells': 1, 'cellModel': 'HH'}

#netParams.popParams['CA_229hoc'] = {'cellType': 'DET', 'numCells': 1, 'cellModel': 'blank'}


## Cell property rules

cellRule = netParams.importCellParams(label = 'PMN1', conds = {'pop': 'MN1'} , fileName = '/Users/adna.dumitrescu/Documents/Wyart_Postdoc/OIST_2019/MN_model/MN1_morphology.py', cellName = 'MakeCell', importSynMechs=True)
cellRule = netParams.importCellParams(label = 'PMN2', conds = {'pop': 'MN2'} , fileName = '/Users/adna.dumitrescu/Documents/Wyart_Postdoc/OIST_2019/MN_model/MN2_morphology.py', cellName = 'MakeCell', importSynMechs=True)
cellRule = netParams.importCellParams(label = 'PMN3', conds = {'pop': 'MN3'} , fileName = '/Users/adna.dumitrescu/Documents/Wyart_Postdoc/OIST_2019/MN_model/MN3_morphology.py', cellName = 'MakeCell', importSynMechs=True)
cellRule = netParams.importCellParams(label = 'PMN4', conds = {'pop': 'MN4'} , fileName = '/Users/adna.dumitrescu/Documents/Wyart_Postdoc/OIST_2019/MN_model/MN4_morphology.py', cellName = 'MakeCell', importSynMechs=True)


#cellRule = netParams.importCellParams(label = 'CA_229hoc', conds = {'pop': 'CA_229hoc'} , fileName = 'cells/CA_229.hoc', cellName = '', importSynMechs=False)


#cellRule = {'conds': {'cellType': 'PYR'},  'secs': {}} 	# cell rule dict, make an new matrix called secs, in which the data will be spit
#cellRule['secs']['soma'] = {'geom': {}, 'mechs': {}}  														# soma params dict
#cellRule['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0}  			# big dictionary with all the values we want to add into the model						# soma geometry
#cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}  		# soma hh mechanism
#netParams.cellParams['PYRrule'] = cellRule  												# add dict to list of cell params

## Synaptic mechanism parameters, most of them get imported from somewhere else
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': cfg.synMechTau2, 'e': 0}  # excitatory synaptic mechanism
# original netParams.synMechParams['gap'] = {'mod': 'ElectSyn', 'g': 0.000049999999999999996}  # excitatory synaptic mechanism
netParams.synMechParams['gap'] = {'mod': 'ElectSyn', 'g': 0.00000049999999999999996}  # excitatory synaptic mechanism

# Stimulation parameters
#netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5}#intrinsic noise is also included
#netParams.stimTargetParams['bkg->PYR'] = {'source': 'bkg', 'conds': {'cellType': 'PYR'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}

netParams.stimSourceParams['pulse1'] = {'type': 'IClamp', 'del':100, 'dur':5, 'amp':0.25} #ms  nA
"""
netParams.stimSourceParams['pulse2'] = {'type': 'IClamp', 'del':200, 'dur':100, 'amp':0.25} #ms  nA
netParams.stimSourceParams['pulse4'] = {'type': 'IClamp', 'del':140, 'dur':5, 'amp':0.25} #ms  nA
netParams.stimSourceParams['pulse5'] = {'type': 'IClamp', 'del':150, 'dur':5, 'amp':0.30} #ms  nA
netParams.stimSourceParams['pulse6'] = {'type': 'IClamp', 'del':160, 'dur':5, 'amp':0.35} #ms  nA
netParams.stimSourceParams['pulse7'] = {'type': 'IClamp', 'del':170, 'dur':5, 'amp':0.40} #ms  nA
"""


"""
netParams.stimSourceParams['pulse2'] = {'type': 'IClamp', 'del':200, 'dur':5, 'amp':0.25} #ms  nA
netParams.stimSourceParams['pulse3'] = {'type': 'IClamp', 'del':300, 'dur':5, 'amp':0.25} #ms  nA
netParams.stimSourceParams['pulse4'] = {'type': 'IClamp', 'del':400, 'dur':5, 'amp':0.25} #ms  nA
"""

netParams.stimTargetParams['pulse1->MN1'] = {'source': 'pulse1', 'conds': {'cellType': 'PMN1'}, 'sec':'soma_0', 'loc':0.5}
#netParams.stimTargetParams['pulse2->MN1'] = {'source': 'pulse2', 'conds': {'cellType': 'PMN1'}, 'sec':'soma_0', 'loc':0.5}

"""
netParams.stimTargetParams['pulse3->MN1'] = {'source': 'pulse3', 'conds': {'cellType': 'PMN1'}, 'sec':'soma_0', 'loc':0.5}
netParams.stimTargetParams['pulse4->MN1'] = {'source': 'pulse4', 'conds': {'cellType': 'PMN1'}, 'sec':'soma_0', 'loc':0.5}
netParams.stimTargetParams['pulse5->MN1'] = {'source': 'pulse5', 'conds': {'cellType': 'PMN1'}, 'sec':'soma_0', 'loc':0.5}
netParams.stimTargetParams['pulse6->MN1'] = {'source': 'pulse6', 'conds': {'cellType': 'PMN1'}, 'sec':'soma_0', 'loc':0.5}
netParams.stimTargetParams['pulse7->MN1'] = {'source': 'pulse7', 'conds': {'cellType': 'PMN1'}, 'sec':'soma_0', 'loc':0.5}
"""
"""
netParams.stimTargetParams['pulse2->MM2'] = {'source': 'pulse2', 'conds': {'cellType': 'PMN2'}, 'sec':'soma_0', 'loc':0.5}
netParams.stimTargetParams['pulse3->MN3'] = {'source': 'pulse3', 'conds': {'cellType': 'PMN3'}, 'sec':'soma_0', 'loc':0.5}
netParams.stimTargetParams['pulse4->MN4'] = {'source': 'pulse4', 'conds': {'cellType': 'PMN4'}, 'sec':'soma_0', 'loc':0.5}
"""


## Cell connectivity rules
netParams.connParams['MN1->MN2'] = { 	#  S -> M label
	'preConds': {'pop': 'MN1'}, 	# conditions of presyn cells
	'postConds': {'pop': 'MN2'}, # conditions of postsyn cells
	'weight': 2, 		# synaptic weight
	'delay': 0.1,						# transmission delay (ms)
	'synMech': 'gap',
    'gapJunction': True,
    'sec': 'axon',
    'loc': 0.5,
    'preSec': 'axon',
    'preLoc': 0.5
    }   			# synaptic mechanism

netParams.connParams['MN1->MN3'] = { 	#  S -> M label
	'preConds': {'pop': 'MN1'}, 	# conditions of presyn cells
	'postConds': {'pop': 'MN3'}, # conditions of postsyn cells
	'probability': 0.7 , 
    'weight': 0.001, 		# synaptic weight
	'delay': 10,						# transmission delay (ms)
	'synMech': 'exc',
    'sec': 'soma',
    'loc': 0.5,
    'preSec': 'soma',
    'preLoc': 0.5
    }   			# synaptic mechanism


netParams.connParams['MN1->MN4'] = { 	#  S -> M label
	'preConds': {'pop': 'MN1'}, 	# conditions of presyn cells
	'postConds': {'pop': 'MN4'}, # conditions of postsyn cells
	'weight': 4, 		# synaptic weight
	'delay': 0.1,						# transmission delay (ms)
	'synMech': 'gap',
    'gapJunction': True,
    'sec': 'soma',
    'loc': 0.5,
    'preSec': 'soma',
    'preLoc': 0.5
    }   			# synaptic mechanism


netParams.connParams['MN1->MN4'] = { 	#  S -> M label
	'preConds': {'pop': 'MN1'}, 	# conditions of presyn cells
	'postConds': {'pop': 'MN4'}, # conditions of postsyn cells
	'probability': 1 , 
    'weight': 0.01, 		# synaptic weight
	'delay': 10,						# transmission delay (ms)
	'synMech': 'exc',
    'sec': 'soma',
    'loc': 0.5,
    'preSec': 'soma',
    'preLoc': 0.5
    }   			# synaptic mechanism


