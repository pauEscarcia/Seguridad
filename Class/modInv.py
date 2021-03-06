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
    gcd, a, y = egcd(a, b)
    if gcd != 1:
        return None  # inverso modular no existe
    else: 	
        return a % b