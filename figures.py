import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import math
import numpy as np

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

	#rysowanie	
	fig = plt.figure()
	ax = fig.add_subplot(111, aspect='equal')
	x = [xA,xB,xC,xD]
	y = [yA,yB,yC,yD]
	plt.xlim((xA-2),(xB+2))
	plt.ylim((yA-2),(yB+4))
	ax.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=False))
	plt.show()

	#obliczany bok a
	a = 0
	if xA == xB:
		a = yA - yB
	if yA == yB:
		a = xA - xB
	if xA != xB and yA != yB:
		a = math.sqrt((xA - xB)**2 + (yA - yB)**2)
	if a < 0:
		a = -a
	
	#obliczany bok b
	b = 0
	if xB == xC:
		b = yB - yC
	if yB == yC:
		b = xB - xC
	if xB != xC and yB != yC:
		b = math.sqrt((xB - xC)**2 + (yB - yC)**2)
	if b < 0:
		b = -b

	#obliczany bok c
	c = 0
	if xC == xD:
		c = yC - yD
	if yC == yD:
		c = xC - xD
	if xC != xD and yC != yD:
		c = math.sqrt((xC - xD)**2 + (yC - yD)**2)
	if c < 0:
		c = -c

	#obliczany bok d
	d = 0
	if xD == xA:
		d = yD - yA
	if yD == yA:
		d = xD - xA
	if xD != xA and yD != yA:
		d = math.sqrt((xD - xA)**2 + (yD - yA)**2)
	if d < 0:
		d = -d

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
	if xA != xB and yA != yB:
		a = math.sqrt((xA - xB)**2 + (yA - yB)**2)
	if a < 0:
		a = -a

	#rysowanie 
	fig = plt.figure()
	plt.axes()
	square= plt.Rectangle((xA,yA), xC-1, yC-1, fc='blue')
	plt.gca().add_patch(square)
	plt.xlim((xA-2),(xC+2))
	plt.ylim((yA-2),(yC+2))
	plt.show()

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

	#obliczamy bopk a
	if xA == xB:
		a = yA - yB
	if yA == yB:
		a = xA - xB
	if a < 0:
		a = -a
	if xA != xB and yA != yB:
		a = math.sqrt((xA - xB)**2 + (yA - yB)**2)
	#obliczamy bok b
	if xB == xC:
		b = yB - yC
	if yB == yC:
		b = xB - xC
	if b < 0:
		b = -b
	if xB != xC and yB != yC:
		b = math.sqrt((xB - xC)**2 + (yB - yC)**2)

	#rysowanie 
	fig = plt.figure()
	plt.axes()
	rectangle = plt.Rectangle((xA,yA), xC-1, yC-1, fc='blue')
	plt.gca().add_patch(rectangle)
	plt.xlim((xA-2),(xC+2))
	plt.ylim((yA-2),(yC+2))
	plt.show()

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
	if xA != xB and yA != yB:
		a = math.sqrt((xA - xB)**2 + (yA - yB)**2)
	if a < 0:
		a = -a
		
	#obliczany bok b
	if xB == xC:
		b = yB - yC
	if yB == yC:
		b = xB - xC
	if xB != xC and yB != yC:
		b = math.sqrt((xB - xC)**2 + (yB - yC)**2)
	if b < 0:
		b = -b

	#obliczany bok c
	if xC == xB:
		c = yC - yB
	if yC == yB:
		c = xC - xB
	if xC != xB and yC != yB:
		c = math.sqrt((xC - xB)**2 + (yC - yB)**2)
	if c < 0:
		c = -c

	#rysowanie trojkata
	from matplotlib.patches import Polygon
	pts = np.array([[xA,yA], [xB,yB], [xC,yC]])
	p = Polygon(pts, closed=False)
	ax = plt.gca()
	ax.add_patch(p)
	ax.set_xlim(xA-3,xB+3)
	ax.set_ylim(yA-3,yB+3)
	plt.show()


	o = a + b + c
	#obliczamy pole trojkata z wzoru herona
	p = math.sqrt(o * (o - a) * (o - b) * (o -c)) 
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