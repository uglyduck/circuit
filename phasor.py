# In the command prompt, type python
# and press Enter. The IDLE shell will
# be displayed. 
#
# Navigate to location of the script.
# and type the following:
# command to run this script
# "phasor.py" 
# exec(open('phasor.py').read())

import cmath
e=cmath.e
pi=cmath.pi

def pol2rec(R,PHI):
	V=cmath.rect(R,PHI*pi/180)
	return (round(V.real,3)+round(V.imag,3)*1j)
	

def rec2pol(Z):
	cmath.polar(Z)
	V=(cmath.polar(Z)[0],cmath.polar(Z)[1]*180/pi)
	print ("Amplitude =",round(V[0],3), "Angle =",(round(V[1],3)))
	if round(V[1],3) >0:
		print ("Amplitude =",round(V[0],3), "Angle =",(360-round(V[1],3)))
	else: 
		print ("Amplitude =",round(V[0],3), "Angle =",(360+round(V[1],3)))
	return (round(V[0],3),round(V[1],3))

#def alternate_polar(*(r,phi)):
	
#	# x=(r,phi)
#	if phi >0:
#		phi2=phi-360
#	else :
#		phi2=phi+360
#	return ((r,phi2))	
	

#a=1+1.5j
#b=2.5j
#c=11
#d=15
# a = input ("a =")
# b = input ("b =")
# c = input ("c =")
# d = input ("d =")
# e = input ("e =")
# f = input ("f =")


#a = complex(input ("a =") )
#b = complex(input ("b =") )
#c = complex(input ("c =") )
#d = complex(input ("d =") )
#e = complex(input ("e =") )
#f = complex(input ("f =") )

delta = (a*d) - (b*c)
# e=cmath.rect(120,45*pi/180)
# e=20
# f=0

delta1=e*d-f*b
delta2=a*f-e*c

I1=delta1/delta
I2=delta2/delta


I1_pol=rec2pol(I1)
I2_pol=rec2pol(I2)

print (I1_pol,I2_pol)
#print (type (I1_pol))
#print (type (I2_pol))

#I1_alt=alternate_polar(I1_pol)
#print (I1_alt)

#I2_alt=alternate_polar(I2_pol)
#print (I2_alt)

# print (alternate_polar(rec2pol(I1)), alternate_polar(rec2pol(I2)))











