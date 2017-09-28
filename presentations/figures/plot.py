import numpy as np
import matplotlib.pyplot as plt

SMALL_SIZE = 8
MEDIUM_SIZE = 20
BIGGER_SIZE = 24
linewidth=4

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

if False:
   t = np.arange(-1., 2., 0.01)
   x=2+3*t
   plt.xlabel("t")
   plt.ylabel("x")
   plt.axvline(0.0,lw=2,color='grey')
   plt.axhline(0.0,lw=2,color='grey')
   plt.plot(t,x,lw=linewidth)
   plt.grid()
   plt.show()

if True:
   soa = np.array([[0, 0, 6, 8]])
   X, Y, U, V = zip(*soa)
   plt.figure()
   ax = plt.gca()
   ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1,lw=2)
   ax.set_xlim([0, 10])
   ax.set_ylim([0, 10])
   plt.xlabel("x")
   plt.ylabel("y")
   plt.draw()
   plt.grid()
   plt.show()
