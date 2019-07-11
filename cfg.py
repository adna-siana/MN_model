# this is the configuration file for what you want to record and analyse 
import sys 
sys.path.append('/Applications/NEURON-7.7/nrn/lib/python')
from neuron import h


from netpyne import specs

# Simulation options
cfg = specs.SimConfig()		# object of class SimConfig to store simulation configuration
cfg.duration = 500			# Duration of the simulation, in ms
cfg.dt = 0.025 				# Internal integration timestep to use
cfg.verbose = True	# Show detailed messages
cfg.recordStim = True		
cfg.recordTraces = {'V_soma':{'sec':'soma_0','loc':0.5,'var':'v'}, }# Dict with traces to record

'''  
                    'i_nav_soma':{'sec':'soma_0','loc':0.5,'mech':'nav1p6', 'var':'gna'}, 
                    'i_kv_soma':{'sec':'soma_0','loc':0.5,'mech':'kv2', 'var':'gk'} 
                    
'''

#cfg.recordTraces ['i_gap'] = {'sec' :'soma_0', 'loc':0.5, 'synMech':'gap', 'var': 'i'}
#cfg.recordTraces ['iClamp'] = {'sec' :'soma_0', 'loc':0.5, 'synMech':'gap', 'var': 'i'}
cfg.recordStep = 0.1 			# Step size in ms to save data (eg. V traces, LFP, etc)
cfg.filename = 'MN_model_1st_test'  # Set file output name
cfg.saveJson = True
cfg.printPopAvgRates = True
#cfg.analysis['plotRaster'] = {'saveFig': True} 			# Plot a raster
cfg.analysis['plotTraces'] = {'include': [0,1,2,3], 'saveFig': True} 			# Plot recorded traces for this list of cells
# Variable parameters (used in netParams)
cfg.synMechTau2 = 3 # original 5
cfg.connWeight = 0.01
cfg.hParams.celsius = 24 # change temperature at which sim is made 
cfg.hParams.v_init = -70 # change v init 

# Variable parameters (used in netParams)
# multipliers
cfg.gbar_nav_scale = 1
cfg.gbar_kv_scale = 1