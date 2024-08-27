from math import sqrt
from math import floor
from millerRabinPrime import is_prime

# !! exponential runtime complexity 
# no better method exists; this is what makes RSA algorithm, etc. secure
def get_prime_factors(n):
	factors = []

	limit = floor(sqrt(n))

	for i in range(2, limit):
		if n % i == 0:
			if (is_prime(i)):
				factors.append(i)

	if (len(factors) > 0):
		return factors
	else:
		return [1, n]

if __name__ == '__main__':
	factors = get_prime_factors(210)
	if (factors[0] == 1):
		print('PRIME:', factors)
	else:
		print('COMPOSITE:', factors)
