import sys 
sys.path.append('/Applications/NEURON-7.7/nrn/lib/python')

from netpyne import sim

# read cfg and netParams from command line arguments if available; otherwise use default
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='cfg.py', netParamsDefault='netParams.py')					

# Create network and run simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)

