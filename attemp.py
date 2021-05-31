import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import math

xA=1
yA = 1
xB =4
yB = 1
xC = 3
yC = 3
xD=2
yD=3


fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
x = [xA,xB,xC,xD]
y = [yA,yB,yC,yD]
plt.xlim((xA-2),(xB+2))
plt.ylim((yA-2),(yB+4))
ax.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=False))
plt.show()