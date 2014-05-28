#! /usr/bin/env python
#-*- coding utf-8 -*-

#***********************************************************************

# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#***********************************************************************

class Cursor:
    def __init__(self, ax):
        self.ax = ax
        self.lx = ax.axhline(color='r')  # the horiz line
        self.ly = ax.axvline(color='r')  # the vert line
        self.x = 0
        self.y = 0
        self.pixel = []
        # text location in axes coords
        self.txt = ax.text( 0.7, 0.9, '', transform=ax.transAxes)

    def mouse_move(self, event):
        if not event.inaxes: return
        
       
        self.x, self.y = event.xdata, event.ydata
        # update the line positions
            
        self.lx.set_ydata(self.y )
        self.ly.set_xdata(self.x )
            
        self.pixel.append(self.x)
        self.txt.set_text( 'x=%1.2f, y=%1.2f'%(self.x,self.y) )
        plt.draw()


    
    


        
fig, ax = plt.subplots()
#fig = plt.figure()
#ax = fig.add_subplot(111)        

cur = Cursor(ax)

img = mpimg.imread('T1.png')

cid = fig.canvas.mpl_connect('button_press_event', cur.mouse_move)
    
print 'pixel (%s,%s)' % (cur.x,cur.y)
plt.imshow(img)

plt.show()
   
print cur.pixel