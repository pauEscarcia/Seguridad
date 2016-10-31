def MCD(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a

def egcd(a, b):
	x=0
	y=1
	u=1
	v=1
	while a != 0:
		q, r = b // a, b % a
		m, n = x - u * q, y - v * q
		b, a, x, y, u, v = a, r, u, v, m, n
	return b, x, y

def modinv(a, b):
    gcd, x, y = egcd(a, b)
    if gcd != 1:
        return None  # inverso modular no existe
    else: 	
        return x % b

def rsa():
	p=47
	q=43
	e=17
	fi=(p-1)*(q-1)
	mcd=MCD(e,fi)
	print mcd
	d= modinv(e,fi)
	print d
	return d

rsa()

