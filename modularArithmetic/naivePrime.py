from math import floor
from math import sqrt

# !! exponential runtime complexity
def naive_is_prime(n):
	# one and negative numbers are not a prime or composite numbers
	if n < 2:
		return False
	
	# two is the only even prime number
	if n == 2:
		return True
	
	# even numbers (except 2) are not prime
	if n % 2 == 0:
		return False
	
	# if odd number && less than or equal to square root
	# range [3, sqrt(n)] and increment by 2 
	for i in range(3, floor(sqrt(n))+1, 2):
		if n % i == 0:
			return False
		
	return True

def batch_is_prime(r1,r2, func):
	for i in range (r1,r2,1):
		print(i, func(i))

if __name__ == '__main__':
	batch_is_prime(423,437, naive_is_prime)

