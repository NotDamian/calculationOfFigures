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

def circleField(r):
	return (3.14 * r * r)
def circumferenceOfACircle(r):
	return (2 * 3.14 * r)

def ctrapezeField(a,b,h):
	return ((a + b) * h) / 2
def circumferenceOfATrapeze(a, b, c, d):
	return (a + b + c + d)

def squareField(a):
	return a * a
def circumferenceOfASquare(a):
	return a * 4

def rectangleField(a, b):
	return a * b
def circumferenceOfARectangle(a, b):
	return (2 * a) + (2 * b)

def triangleField(a, h):
	return (a * h) / 2
def circumferenceOfATriangle(a, b, c):
	return a + b + c