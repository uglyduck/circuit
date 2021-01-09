import cmath
e=cmath.e
pi=cmath.pi

def pol2rec(R,PHI):
	V=cmath.rect(R,PHI*pi/180)
	return V
	

def rec2pol(Z):
	cmath.polar(Z)
	V=(cmath.polar(Z)[0],cmath.polar(Z)[1]*180/pi)
	return V
	






