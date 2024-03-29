import matplotlib.pyplot as plt
import os
import json
import numpy as np
wdir=os.getcwd()

#ts = Trace(sim.allSimData.V_soma['cell_20'], sim.allSimData.t)

    

fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True)

fn = 'MN_model_test.json'
with open(os.path.join(wdir, fn)) as json_file:  
    result = json.load(json_file)
t=np.array(result['simData']['t'])
v=np.array(result['simData']['V_soma']['cell_0'])
gna=np.array(result['simData']['i_nav_soma']['cell_0'])
gk=np.array(result['simData']['i_kv_soma']['cell_0'])
spkt=result['simData']['spkt']
axes[0].plot(t, v)
axes[1].stackplot(t, gna, gk)
axes[1].legend(['g_Na', 'g_K'])
relgk=gk/[gna+gk]
relgna=gna/[gna+gk]
axes[2].stackplot(t, relgna, relgk)
axes[2].legend(['g_Na (% of total)', 'g_K (% of total)'])