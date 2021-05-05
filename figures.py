import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

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
	print("Ob= ", o)

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

	p = ((a + b) * h) / 2
	o = (a + b + c + d)

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
	p = a * a
	o = a * 4

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
	p = a * b
	o = (2 * a) + (2 * b)

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
switch(x)