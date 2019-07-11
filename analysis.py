#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:57:50 2019

@author: adna.dumitrescu
"""

import matplotlib.pyplot as plt
import os
wdir=os.getcwd()

import json
import numpy as np
import seaborn as sns

file = 'MN_model_1st_test.json'

with open(os.path.join(wdir, file)) as json_file:  
    result = json.load(json_file)
t=np.array(result['simData']['t'])
v_C1=np.array(result['simData']['V_soma']['cell_0'])
v_C2=np.array(result['simData']['V_soma']['cell_1'])
v_C3=np.array(result['simData']['V_soma']['cell_2'])
v_C4=np.array(result['simData']['V_soma']['cell_3'])


t_AP1 = t[500:1500]
V_AP1 = v_C1[500:1500]

t_AP2 = t[500:1500]
V_AP2 = v_C2[500:1500]


t_AP3 = t[500:1500]
V_AP3 = v_C3[500:1500]


t_AP4 = t[500:1500]
V_AP4 = v_C4[500:1500]



plt.plot(t_AP1,V_AP1, linewidth=0.7, color = 'k')
plt.ylim(-80,40)
plt.xlabel('time (ms)')
plt.ylabel('voltage (mV)')
plt.title('MN 1')
sns.despine()


plt.plot(t_AP2,V_AP2, linewidth=1, color = 'b')
plt.ylim(-80,40)
plt.xlabel('time (ms)')
plt.ylabel('voltage (mV)')
plt.title('MN 2')
sns.despine()

plt.plot(t_AP3,V_AP3, linewidth=0.7, color = 'r')
plt.ylim(-80,40)
plt.xlabel('time (ms)')
plt.ylabel('voltage (mV)')
plt.title('MN 3')
sns.despine()

plt.plot(t_AP4,V_AP4, linewidth=0.7, color = 'm')
plt.ylim(-80,40)
plt.xlabel('time (ms)')
plt.ylabel('voltage (mV)')
plt.title('Mini network response')
sns.despine()



"""
fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True)


#gna=np.array(result['simData']['i_nav']['cell_0'])
#gk=np.array(result['simData']['i_kv']['cell_0'])
spkt=result['simData']['spkt']
axes[0].plot(t, v)
axes[1].stackplot(t, gna, gk)
axes[1].legend(['g_Na', 'g_K'])
#relgk=gk/[gna+gk]
#relgna=gna/[gna+gk]
axes[2].stackplot(t, relgna, relgk)
axes[2].legend(['g_Na (% of total)', 'g_K (% of total)'])

"""