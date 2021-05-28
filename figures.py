import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import math

def show():
	verts = [
	(0., 0.),  # left, bottom
	(0., 1.),  # left, top
	(1., 1.),  # right, top
	(1., 0.),  # right, bottom
	(0., 0.),  # ignored
	]

	codes = [
		Path.MOVETO,
		Path.LINETO,
		Path.LINETO,
		Path.LINETO,
		Path.CLOSEPOLY,
	]

	path = Path(verts, codes)

	fig, ax = plt.subplots()
	patch = patches.PathPatch(path, facecolor='orange', lw=2)
	ax.add_patch(patch)
	ax.set_xlim(-2, 2)
	ax.set_ylim(-2, 2)
	plt.show()

def circle():
	print("Podaj promien: ")
	r = float(input())
	print("Podaj srodek kola: ")
	print("x: ")
	x = float(input())
	print("y: ")
	y = float(input())
	a = (x, y)
	p = 3.14 * r * r
	o = 2 * 3.14 * r
	print("P= ", p)
	print("Ob= ", o)
	#rysowanie kola
	circle1 = plt.Circle((x, y), r, color='r')
	fig, ax = plt.subplots()
	plt.xlim((x-r-2),(x+r+2))
	plt.ylim((y-r-2),(y+r+2))
	plt.grid(linestyle='--')
	ax.set_aspect(1)
	ax.add_artist(circle1)
	plt.title('Circle', fontsize=8)
	plt.show()


def trapeze():
	print("Podaj wierzcholek A: ")
	print("x: ")
	xA = int(input())
	print("y: ")
	yA = int(input())
	print("Podaj wierzcholek B: ")
	print("x: ")
	xB = int(input())
	print("y: ")
	yB = int(input())
	print("Podaj wierzcholek C: ")
	print("x: ")
	xC = int(input())
	print("y: ")
	yC = int(input())
	print("Podaj wierzcholek D: ")
	print("x: ")
	xD = int(input())
	print("y: ")
	yD = int(input())


	#obliczany bok a
	if xA == xB:
		a = yA - yB
	if yA == yB:
		a = xA - xB
	if a < 0:
		a = -a
	if xA != xB and yA != yB:
		a = sqr((xA - xB)**2 + (yA - yB)**2)
	
	#obliczany bok b
	if xB == xC:
		b = yB - yC
	if yB == yC:
		b = xB - xC
	if b < 0:
		b = -b
	if xB != xC and yB != yC:
		b = sqr((xB - xC)**2 + (yB - yC)**2)

	#obliczany bok c
	if xC == xD:
		c = yC - yD
	if yC == yD:
		c = xC - xD
	if c < 0:
		c = -c
	if xC != xD and yC != yD:
		c = sqr((xC - xD)**2 + (yC - yD)**2)

	#obliczany bok d
	if xD == xA:
		d = yD - yA
	if yD == yA:
		d = xD - xA
	if d < 0:
		d = -d
	if xD != xA and yD != yA:
		d = sqr((xD - xA)**2 + (yD - yA)**2)

		
	verts = [
	(xA, yA),  # left, bottom
	(xB, yB),  # left, top
	(xC, yC),  # right, top
	(xD, yD),  # right, bottom
	(0., 0.),  # ignored
	]
	
	pp = (xA + xB) * (yB - yA) + (xB + xC) * (yC - yB) - (xC + xD) * (yD - yC) - (xC + xA) * (yA - yC)
	o = (a + b + c + d)
	p = pp / 2
	print("P= ", p)
	print("Ob= ", o)

def square():
	print("Podaj wierzcholek A: ")
	print("x: ")
	xA = int(input())
	print("y: ")
	yA = int(input())
	print("Podaj wierzcholek B: ")
	print("x: ")
	xB = int(input())
	print("y: ")
	yB = int(input())
	print("Podaj wierzcholek C: ")
	print("x: ")
	xC = int(input())
	print("y: ")
	yC = int(input())
	print("Podaj wierzcholek D: ")
	print("x: ")
	xD = int(input())
	print("y: ")
	yD = int(input())
	if xA == xB:
		a = yA - yB
	else:
		a = xA - xB
	if a < 0:
		a = -a

	verts = [
	(xA, yA),  # left, bottom
	(xB, yB),  # left, top
	(xC, yC),  # right, top
	(xD, yD),  # right, bottom
	(0., 0.),  # ignored
	]

	p = a * a
	o = a * 4
	print("P= ", p)
	print("Ob= ", o)

def rectangle():
	print("Podaj wierzcholek A: ")
	print("x: ")
	xA = int(input())
	print("y: ")
	yA = int(input())
	print("Podaj wierzcholek B: ")
	print("x: ")
	xB = int(input())
	print("y: ")
	yB = int(input())
	print("Podaj wierzcholek C: ")
	print("x: ")
	xC = int(input())
	print("y: ")
	yC = int(input())
	print("Podaj wierzcholek D: ")
	print("x: ")
	xD = int(input())
	print("y: ")
	yD = int(input())
	if xA == xB:
		a = yA - yB
	else:
		a = xA - xB
	if yB == yC:
		a = xB - xC
	else:
		b = yB - yC
	if a < 0:
		a = -a
	if b < 0:
		b = -b

	verts = [
	(xA, yA),  # left, bottom
	(xB, yB),  # left, top
	(xC, yC),  # right, top
	(xD, yD),  # right, bottom
	(0., 0.),  # ignored
	]

	p = a * b
	o = (2 * a) + (2 * b)
	print("P= ", p)
	print("Ob= ", o)

def triangle():
	print("Podaj wierzcholek A: ")
	print("x: ")
	xA = int(input())
	print("y: ")
	yA = int(input())
	print("Podaj wierzcholek B: ")
	print("x: ")
	xB = int(input())
	print("y: ")
	yB = int(input())
	print("Podaj wierzcholek C: ")
	print("x: ")
	xC = int(input())
	print("y: ")
	yC = int(input())

	#obliczany bok a
	if xA == xB:
		a = yA - yB
	if yA == yB:
		a = xA - xB
	if a < 0:
		a = -a
	if xA != xB and yA != yB:
		a = sqr((xA - xB)**2 + (yA - yB)**2)
		
	#obliczany bok b
	if xA == xC:
		b = yA - yC
	if yA == yC:
		b = xA - xC
	if b < 0:
		b = -b
	if xA != xC and yA != yC:
		b = sqr((xA - xC)**2 + (yA - yC)**2)

	#obliczany bok c
	if xC == xB:
		c = yC - yB
	if yC == yB:
		c = xC - xB
	if c < 0:
		c = -c
	if xC != xB and yC != yB:
		c = sqr((xC - xB)**2 + (yC - yB)**2)

	#rysowanie trojkata
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


	o = a + b + c
	#obliczamy pole trojkata z wzoru herona
	p = sqr(o * (o - a) * (o - b) * (o -c)) 
	print("P= ", p)
	print("Ob= ", o)

def information():
	print("My name is Damian")
	switch()
	

def switch():
	'''show()'''
	print("Menu")
	print("Wybierz jaka figure chcesz obliczyc lub inna opcje")
	print("1. Trojkat")
	print("2. Prostokat")
	print("3. Kwadrat")
	print("4. Kolo")
	print("5. Trapez")
	print("6. Informacje o tworcy")
	print("7. Exit")
	x = int(input())

	if x == 1:
		triangle()
	elif x == 2:
		rectangle()
	elif x == 3:
		square()
	elif x == 4:
		circle()
	elif x == 5:
		trapeze()
	elif x == 6:
		information()
	elif x == 7:
		exit()
	else:
		print("blad ")
		print("exit ")
		exit()



switch()