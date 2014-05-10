#!/usr/bin/env python

#  -*- coding: utf-8 -*-

# Imports
#*************************************************************************
import numpy as np
import matplotlib.pyplot as plt
#*************************************************************************

# Corriente
I_max = 0.2
# time constant
tau = 20. # ms
# input resistance
R = 10. # MOhms
# capacidad
C = tau / R
v_thres = 40 # mV
# integration time step
dt = 1 # ms
# simulation time
t_max = 1000
t_v = np.arange(0,t_max - dt + 1, dt,dtype=float)
nt_v = len(t_v)

# Compute constants to save time
dt_tau = dt / tau
one_dt_tau = 1 - dt_tau # forward Euler
m1_dt_tau = 1 / (1 + dt_tau) # backward Euler

# number of simulations

n_sims = 1 # debugging

# input current
# constant current for debugging purposes
Nt = len(t_v)
i_v_i = np.zeros_like(t_v) # nA

#i_v_i[(Nt*3/4.):(Nt*3/4.))
i_v_i[0:(Nt*3/4)] = I_max # nA

for j in xrange(0,n_sims):

    i_v_tot = i_v_i

    v_v = np.zeros_like(t_v)
    s_v = np.zeros_like(t_v)

    for i in xrange(1,nt_v):
        # forward Euler
        v_v[i] =((1 - dt / tau) * v_v[i-1] )+ (dt * i_v_tot[i-1] / C)

        # backward Euler
        v_v[i] = (m1_dt_tau * v_v[i-1] )+ (dt * (i_v_tot[i] / C))

        if (v_v[i] >= v_thres):
            v_v[i] = 0.
            s_v[i] = 1.

vteo = I_max*R*(1 - np.exp(-t_v / tau))

plt.plot(t_v, v_v,'b')
plt.plot(t_v, i_v_i, 'r')
plt.plot(t_v, vteo, 'k')
plt.show()
