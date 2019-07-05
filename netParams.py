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
#netParams.popParams['S'] = {'cellType': 'PYR', 'numCells': 20, 'cellModel': 'HH'}
#netParams.popParams['M'] = {'cellType': 'PYR', 'numCells': 20, 'cellModel': 'HH'}

netParams.popParams['import_swc'] = {'cellType': 'DET', 'numCells': 1, 'cellModel': 'HH'}
netParams.popParams['MN2'] = {'cellType': 'PMN', 'numCells': 1, 'cellModel': 'HH'}

#netParams.popParams['CA_229hoc'] = {'cellType': 'DET', 'numCells': 1, 'cellModel': 'blank'}




## Cell property rules

cellRule = netParams.importCellParams(label = 'import_swc', conds = {'pop': 'import_swc'} , fileName = '/Users/adna.dumitrescu/Documents/Wyart_Postdoc/OIST_2019/MN_model/import_swc.py', cellName = 'MakeCell', importSynMechs=True)
cellRule = netParams.importCellParams(label = 'PMN', conds = {'pop': 'MN2'} , fileName = '/Users/adna.dumitrescu/Documents/Wyart_Postdoc/OIST_2019/MN_model/MN2_morphology.py', cellName = 'MakeCell', importSynMechs=True)

#cellRule = netParams.importCellParams(label = 'CA_229hoc', conds = {'pop': 'CA_229hoc'} , fileName = 'cells/CA_229.hoc', cellName = '', importSynMechs=False)


#cellRule = {'conds': {'cellType': 'PYR'},  'secs': {}} 	# cell rule dict, make an new matrix called secs, in which the data will be spit
#cellRule['secs']['soma'] = {'geom': {}, 'mechs': {}}  														# soma params dict
#cellRule['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0}  			# big dictionary with all the values we want to add into the model						# soma geometry
#cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}  		# soma hh mechanism
#netParams.cellParams['PYRrule'] = cellRule  												# add dict to list of cell params

## Synaptic mechanism parameters, most of them get imported from somewhere else
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': cfg.synMechTau2, 'e': 0}  # excitatory synaptic mechanism

# Stimulation parameters
#netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5}#intrinsic noise is also included
#netParams.stimTargetParams['bkg->PYR'] = {'source': 'bkg', 'conds': {'cellType': 'PYR'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}

netParams.stimSourceParams['pulse1'] = {'type': 'IClamp', 'del':200, 'dur':10, 'amp':0.4} #ms  nA
netParams.stimSourceParams['pulse2'] = {'type': 'IClamp', 'del':300, 'dur':10, 'amp':0.4} #ms  nA

netParams.stimTargetParams['pulse1->MN'] = {'source': 'pulse1', 'conds': {'cellType': 'DET'}, 'sec':'soma_0', 'loc':0.5}
netParams.stimTargetParams['pulse2->MN2'] = {'source': 'pulse2', 'conds': {'cellType': 'PMN'}, 'sec':'soma_0', 'loc':0.5}



## Cell connectivity rules
netParams.connParams['MN1->MN2'] = { 	#  S -> M label
	'preConds': {'pop': 'import_swc'}, 	# conditions of presyn cells
	'postConds': {'pop': 'MN2'}, # conditions of postsyn cells
	'probability': 0.6, 			# probability of connection
	'weight': cfg.connWeight, 		# synaptic weight
	'delay': 5,						# transmission delay (ms)
	'synMech': 'exc'}   			# synaptic mechanism
