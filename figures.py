'''
Projekt Python
Napisać skrypt który po uruchomieniu będzie umożliwiał nam obliczenie obwodu, pola takich figur jak:
- trójkąt
- prostokąt kk
- kwadrat kk
- koło kk
- trapez kk
oraz wyświetlenie figur na układzie współrzędnym. Układ współrzędny musi być przedstawiony graficznie, reszta może pokazywać w terminalu.


Przykład:
1. Wybieramy figurę do obliczenia
2. Podajemy dane figury A(x,y), B(x,y), C(x,y)
3. Wysiedla się nam graficzne przestawienie figury na układzie współrzędnym
4. Obliczamy długości potrzebne do podania obwodu i pola

Powinien mieć:
1. Menu
	a. Trójkąt
	b. Prostokąt
	c. Kwadrat
	d. Koło
	e. Trapez
	f. Informacje o twórcy
	g. Wyjście
'''
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def show(verts):
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

def circle(r):
	p = 3.14 * r * r
	o = 2 * 3.14 * r

def trapezeField(a,b, c, h):
	p = ((a + b) * h) / 2

	o = (a + b + c + d)

def square(a):
	p = a * a
	o =  a * 4

def rectangleField(a, b):
	p = a * b
	o = (2 * a) + (2 * b)

def triangleField(a, b, c, h):
	p = (a * h) / 2
	o = a + b + c

show()