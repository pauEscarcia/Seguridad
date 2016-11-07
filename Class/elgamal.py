from modInv import *

def elgamal(x):
	p,a,d,ke,b =29,2,12,5,7

	print "Entradas:"
	print "p =", p,"a =", a,"d =", d,"b=", b , "ke=", ke
	
	e=egcd(p-1,ke)
	print "MCD (", p-1, ke, ") = " , e[0]
	print "x = " , x
	r= a ** ke % p
	
	s= (x-d*r)* modinv(ke,p-1) % (p-1)

	t= (b**r)*(r**s) % p
	print "Salidas:"
	print"r =" , r, "s=", s, "t=", t
	 


elgamal(26)
