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

#	n=11 g=8 (8 is a primitive root of 11) returns [1, 10]; all integers from 1 to n-1
	# print(modularExponentiation(8, 2, 11))
	# print(modularExponentiation(8, 3, 11))
	# print(modularExponentiation(8, 4, 11))
	# print(modularExponentiation(8, 5, 11))
	# print(modularExponentiation(8, 6, 11))
	# print(modularExponentiation(8, 7, 11))
	# print(modularExponentiation(8, 8, 11))
	# print(modularExponentiation(8, 9, 11))
	# print(modularExponentiation(8, 10, 11))

#	n=11 g=10 (10 is NOT a primitive root of 11) returns 1s && 10s
	# print(modularExponentiation(10, 2, 11))
	# print(modularExponentiation(10, 3, 11))
	# print(modularExponentiation(10, 4, 11))
	# print(modularExponentiation(10, 5, 11))
	# print(modularExponentiation(10, 6, 11))
	# print(modularExponentiation(10, 7, 11))
	# print(modularExponentiation(10, 8, 11))
	# print(modularExponentiation(10, 9, 11))
	# print(modularExponentiation(10, 10, 11))
