import random
from naivePrime import batch_is_prime

# logarithmic runtime complexity
# !! can produce false-positives

# Fermat's primality test is probabilistic based on k iterations
# Note: false-positives are produced with Carmichael numbers
def fermats_is_prime(n, k=10):
	if n < 2:
		return False
	
	if n == 2:
		return True

	# "_" => not using the iteration counter
	for _ in range(k):
		# [2, n - 1]
		a = random.randint(2, n - 1)
		# if a ^ n % n != a then is not prime
		if pow(a, n, n) != a:
			return False

	return True

if __name__ == '__main__':
	batch_is_prime(0,20, fermats_is_prime)

# pow(x, y, z)
# x = base number
# y = exponent
# z = (optional) modulus