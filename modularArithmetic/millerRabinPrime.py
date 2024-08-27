import random
from naivePrime import batch_is_prime

# logarithmic runtime complexity

# Miller-Rabin primality test is probabilistic based on k iterations; optimal k = 40
# Note: higher probability than Fermat's primality test
def miller_rabin(d, n):
	# [2, n - 2]
	a = random.randint(2, n - 2)

	# a ^ d % n
	x = pow(a, d, n)

	if (x == 1 or x == n - 1):
		return True
	
	while (d != n - 1):
		x = (x**2) % n
		d *= 2

		if (x == 1):
			return False
		if (x == n - 1):
			return True
		
	return False

def is_prime(n, k=40):
	# 1 = false
	if n < 2:
		return False
	# 2, 3 = true
	if n < 4:
		return True
	# even number (excluding 2) = false
	if n % 2 == 0:
		return False
	
	d = n - 1
	while d % 2 == 0:
		# divide and round down
		d //= 2

	for _ in range(k):
		if (miller_rabin(d, n)):
			return True
		
	return False

if __name__ == '__main__':
	batch_is_prime(0,20, is_prime)