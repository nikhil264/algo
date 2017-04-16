#Nikhil Reddy Chalamalla
#2014AAPS264H



import random

n = input("enter a number: ")
#factorization takes a number n and finds s and d such that it satisfies n-1 = 2^s * d
def factorization(n):
    n = n-1
    s = 0
    while(n%2==0):
        n = n/2
        s = s+1
    return n, s

#is_composite checks for the Miller-Rabin primality test
# a witness for the compositeness of n
def is_composite(n,a,d,s):
    if pow(a, d, n) == 1:
        return False
    for i in xrange(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True


no_of_trails = 5

#is_probably_prime checks for compositeness of n no_of_trails times
#returns false if we found a witness in any trail otherwise returns true
#When the number n to be tested is small, trying all a < 2(ln n)2 is not necessary,
#as much smaller sets of potential witnesses are known to suffice.
def is_prime(n):
	d, s = factorization(n)

	#if n < 2,047, it is enough to test a = 2;
	if n < 2047:
		if(is_composite(n, 2,d,s)==False):
			return True
		else:
			return False
	
	#if n < 1,373,653, it is enough to test a = 2 and 3;
	if n < 1373653:
		if(is_composite(n, 2,d,s)==False & is_composite(n, 3,d,s)==False) :
			return True
		else:
			return False

	for i in xrange(no_of_trails):
		a = random.randrange(2,n)
		if is_composite(n, a, d, s):
			return False
	return True


#checks whether 2^n - 1 is a prime number for prime n (3,4000)
# for i in xrange(3,4000,2):
#     if is_prime(i) & is_prime(2**i-1):
#         print(i,2**i-1)

print(is_prime(n))