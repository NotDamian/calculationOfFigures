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

def circle():
	pront("Podaj promien: ")
	r = int(input())
	print("Podaj środek koła: ")
	print("x: ")
	x = int(input())
	print("y: ")
	y = int(input())
	a = (x, y)
	p = 3.14 * r * r
	o = 2 * 3.14 * r
	circle1 = plt.Circle(a, r, colour = "red")
	fig, ax = plt.subplots()
	ax.add_patch(circle1)
	fig.savefig('plotcircles.png')
	print("P= ", p)
	print("O= ", o)

def trapeze():
	p = ((a + b) * h) / 2
	o = (a + b + c + d)

def square():
	p = a * a
	o =  a * 4

def rectangle():
	p = a * b
	o = (2 * a) + (2 * b)

def triangle():
	p = (a * h) / 2
	o = a + b + c

def information():
	print("My name is Damian")
def switch(x):
	return {
		1: triangle(),
		2: rectangle(),
		3: square(),
		4: circle(),
		5: trapeze(),
		6: information(),
		7: exit()
	}.get(x,"not found")

show()
print("Menu")
print("Wybierz jaka figure chcesz obliczyc lub inna opcje")
print("1. Trojkat")
print("2. Prostokat")
print("3. Kwadrat")
print("4. Kolo")
print("5. Trapez")
print("6. Informacje o tworcy")
print("7. Exit")