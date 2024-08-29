# linear runtime complexity
def modularExponentiation(b, c, m):
	# return: a = b ^ c (mod m)
	return pow(b, c, m)

# exponential runtime complexity
def discrete_logarithm(a, b, m):
	# brute for to find exponent c
	c = 1
	while pow(b, c, m) != a:
		c += 1

	return c

if __name__ == '__main__':
	print(modularExponentiation(5, 948603, 9048610007))
	print(discrete_logarithm(3668993056, 5, 9048610007))
