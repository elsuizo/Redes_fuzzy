#! /usr/bin/env python
#-*- coding utf-8 -*-

#***********************************************************************

# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#***********************************************************************
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

line, = ax.plot(np.random.rand(100), 'o', picker=5)  # 5 points tolerance

def on_pick(event):
    thisline = event.artist
    xdata, ydata = thisline.get_data()
    ind = event.ind
    print('on pick line:', zip(xdata[ind], ydata[ind]))

cid = fig.canvas.mpl_connect('pick_event', on_pick)
plt.show()