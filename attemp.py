import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import math
import numpy as np

xA=1
yA = 1
xB =6
yB = 1
xC = 3
yC = 3

# pts = np.array([[xA,yA], [xB,yB], [xC,yC]])
# triangle = patches(pts, closed=False)
# t1 = plt.triplot()
# ax = plt.gca()
# ax.add_patch(triangle)
# ax.set_xlim(1,7)
# ax.set_ylim(1,8)
# plt.show()



x=np.array([xA,xB,xC,xA])
y=np.array([yA,yB,yC,yA])
# Figure and Axes
fig1=plt.figure(1)
ax1=fig1.add_subplot(111)
# Plot Triangle 1 
ax1.axis('square')
plt.plot(x,y,color=[0/255,176/255,80/255])
# Axes Limits
plt.xlim([-1,7])
plt.ylim([-1,7])
# Grid
plt.grid(axis='both',which='major',color=[166/255,166/255,166/255], linestyle='-', linewidth=2)
plt.minorticks_on()
plt.grid(axis='both',which='minor',color=[166/255,166/255,166/255], linestyle=':', linewidth=1)