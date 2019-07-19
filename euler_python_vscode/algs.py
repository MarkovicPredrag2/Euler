# Library to export functions (for test suite)
import inspect
# Random library
from random import random
# Library for colored output
#from colorama import Fore
#from colorama import Style
# Librarys for complex numbers and mathematical functions/operations
from functools import reduce
import cmath
import math
# Library to plot diagrams
#import matplotlib.pyplot as plt
#import numpy as np
import sys

class p1_multiples_of_3_or_5_below_n():
    # Simple solution with basic iteration
	@classmethod
	def solution_1(cls, n):
		sum = 0
		for i in range(1, n):
			if i % 3 == 0 or i % 5 == 0:
				sum += i
		return sum

    # Solution only with a mathematical formula
	@classmethod
	def solution_2(cls, n):
		limSuperior = n - 1
		sum_multiples_of_3_below_n = (int(limSuperior / 3) + 1) * 3 * (int(limSuperior / 3) / 2)
		sum_multiples_of_5_below_n = (int(limSuperior / 5) + 1) * 5 * (int(limSuperior / 5) / 2)
		multiples_of_3_and_5_below_n = 5 * 3 * int(limSuperior / (5 * 3))
		return int(sum_multiples_of_3_below_n + sum_multiples_of_5_below_n - multiples_of_3_and_5_below_n)

class p2_even_fibonacci_numbers():
	# Simple solution with basic iteration
	@classmethod
	def solution_1(cls, n):
		secondValue = 0
		firstValue = 1
		sum = 0
		while n >= firstValue:
			if firstValue % 2 == 0:
				sum += firstValue
			firstValue += secondValue
			secondValue = firstValue - secondValue
		return sum

class p3_largest_prime_factor():
    # Simple solution
	@classmethod
	def solution_1(self, n):
		highestPrime = 0
		for i in range(int(n / 2)):
			if n % i == 0 and self.isPrimeNumber(i):
				highestPrime = i
		return highestPrime

    # Helper function for solution_1
	@classmethod
	def isPrimeNumber(self, i):
		if i == 1:
			return False
		for n in range(2, i):
			if i % n == 0:
				return False
		return True

	# Prime Number test divisor
	# Very slow (2^n)
	@classmethod
	def primeNumberDivisonTest(self, number):
		for n in range(2, number):
			if self.primeNumberDivisonTest(n) and number % n == 0:
				return False
		return True

	# Faster algorithm to check, if a number is a prime
	@classmethod
	def isPrimeNumberFaster(self, i):
		if i == 2:
			return True
		if i % 2 == 0:
			return False
		for n in range(3, int(math.sqrt(i)) + 1, 2):
			if i % n == 0:
				return False
		return True

	@classmethod
	def integerFactorization(self, integer):
		integers = []
		for n in range(2, int(integer / 2) + 1):
			if integer % n == 0 and self.isPrimeNumberFaster(n):
				pow = 1
				while integer % n**pow == 0:
					integers.append(n)
					pow += 1
		return integers
	
	# Prime number generator: get all primes till n
	@classmethod
	def primeGenerator(self, n):
		return [m for m in range(2, n) if self.isPrimeNumberFaster(m)]

class p4_largest_palindrome_product():
    # Simple solution
	@classmethod
	def solution_1(self, digits):
		maxrange = 10**digits
		largestPalindrome = 0
		for product_1 in range(maxrange):
			for product_2 in product_1:
				product = product_1 * product_2
				productStr = str(product)
				productStrLen = len(productStr)
				for char_pos in range(int(productStrLen / 2)):
					if productStr[char_pos] != productStrLen[(productStrLen - 1) - char_pos]:
						break
				else:
					largestPalindrome = product_1 * product_2
		return largestPalindrome

    # Extended problem with n amount of products
	# @classmethod
	# def solution_2(self, digits, products):
	# 	productSet = [0] * products
	# 	index = len(productSet) - 1
	# 	largestPalindrome = 0
	# 	permutation = 10**(digits * products)

	# 	# =======================================
	# 	# Go through the entire permutation
	# 	# =======================================

	# 	for count in range(permutation):

	# 		# =======================================
	# 		# Check, if the product is a palindrome
	# 		# =======================================
			
	# 		productStr = str(prod(productSet))
	# 		productStrLen = len(productStr)
	# 		productRange = int(productStrLen / 2)

	# 		for char_pos in range(productRange):
	# 			if productStr[char_pos] != productStrLen[(productStrLen - 1) - char_pos]:
	# 				break
	# 		else:
	# 			largestPalindrome = prod(productSet)

	# 		# =======================================
	# 		# Reset the index of the product set
	# 		# =======================================

	# 		productSet[index] += 1

	# 		if productSet[index] < 10**digits:
	# 			if index < len(productSet) - 1:
	# 				index += 1
	# 		else:
	# 			productSet[index] = 0
	# 			index -= 1

class p5_smallest_multiple():
	# KGV Implementation for the problem
	@classmethod
	def solution_1(self, numberrange):
		smallestMultiple = 1
		primes = {}
		for n in numberrange:
			number = 1
			while n > number:
				if n % number == 0 and p3_largest_prime_factor.isPrimeNumber(number):
					primes.get(number, [0])[len(primes[number]) - 1] += 1
				else:
					number += 2
		for prime, exponent in primes.items():
			smallestMultiple *= prime**max(exponent)
		return smallestMultiple

class p6_sum_square_difference():
	# Solution 1 with only formula
	@classmethod
	def solution_1(self, n):
		return int(((n * (n + 1)) / 2)**2 - (n * (n + 1) * (2*n + 1) / 6))

class p7_10001st_prime():
	# Simple solution with iteration
	@classmethod
	def solution_1(self, n):
		number = 2
		lastPrime = number
		while n > 0:
			if p3_largest_prime_factor.isPrimeNumber(number):
				n = n - 1
				lastPrime = number
			number = number + 1
		return lastPrime

class p8_largest_product_in_a_series():
	# Number from Project Euler:
	# 	"73167176531330624919225119674426574742355349194934"
	# 	"96983520312774506326239578318016984801869478851843"
	# 	"85861560789112949495459501737958331952853208805511"
	# 	"12540698747158523863050715693290963295227443043557"
	# 	"66896648950445244523161731856403098711121722383113"
	# 	"62229893423380308135336276614282806444486645238749"
	# 	"30358907296290491560440772390713810515859307960866"
	# 	"70172427121883998797908792274921901699720888093776"
	# 	"65727333001053367881220235421809751254540594752243"
	# 	"52584907711670556013604839586446706324415722155397"
	# 	"53697817977846174064955149290862569321978468622482"
	# 	"83972241375657056057490261407972968652414535100474"
	# 	"82166370484403199890008895243450658541227588666881"
	# 	"16427171479924442928230863465674813919123162824586"
	# 	"17866458359124566529476545682848912883142607690042"
	# 	"24219022671055626321111109370544217506941658960408"
	# 	"07198403850962455444362981230987879927244284909188"
	# 	"84580156166097919133875499200524063689912560717606"
	# 	"05886116467109405077541002256983155200055935729725"
	# 	"71636269561882670428252483600823257530420752963450"
	# 	)

	# Simple solution with basic iteration
	@classmethod
	def solution_1(self, strnumber, adjacents):
		if adjacents > len(strnumber):
			return reduce(lambda x, y: int(x) * int(y), strnumber, 1)
		highestAdjacent = ""
		highestProduct = 1
		for n in range(len(strnumber) - adjacents):
			current_adjacents = strnumber[n: n + adjacents]
			current_product = reduce(lambda x, y: int(x) * int(y), strnumber[n: n + adjacents], 1)
			if current_product > highestProduct:
				highestProduct = current_product
				highestAdjacent = current_adjacents
		return { highestAdjacent: highestProduct }
	
	# Faster solution:
	# Checks the distance between 0's
	@classmethod
	def solution_2(self, strnumber, adjacents):
		highestAdjacent = ""
		highestProduct = 1
		# Get all positions of the 0's
		zeroPositions = [index for index, char in enumerate(strnumber) if char == "0"]
		for n in range(len(zeroPositions) - 2):
			startPosition = zeroPositions[n] + 1
			endPosition = zeroPositions[n + 1]
			distanceBetweenTwoZeros = endPosition - startPosition
			if distanceBetweenTwoZeros > adjacents:
				# Check for the highest adjacents and product within the gap
				for m in range((distanceBetweenTwoZeros - adjacents) + 1):
					current_adjacents = strnumber[(startPosition + m): (startPosition + m) + adjacents]
					current_product = reduce(lambda x, y: int(x) * int(y), strnumber[(startPosition + m): (startPosition + m) + adjacents], 1)
					if current_product > highestProduct:
						highestProduct = current_product
						highestAdjacent = current_adjacents
		return { highestAdjacent: highestProduct }
	
	# Function to generate test numbers
	@classmethod
	def generateNumberWithNDigits(self, n):
		return ''.join([str(int(10 * random())) for x in range(n)])

class p9_special_pythagorean_triplet():
	# Function to dump all pythagorean triplets in an infinite loop
	# Emphasizes the right result in green
	@classmethod
	def solution_1(self):
		n = 1
		while True:
			m = 1
			while (n - m)**2 > (n**2)/2:
				# Solve quadratic function
				x = self.solveQuadraticFunction(1, -2*n, (n**2 - sum([2*(n-x) - 1 for x in range(0, m)])), True)
				if float(x[0].real).is_integer() and float(x[1].real).is_integer():
					a = int(n - x[0].real) if (n - x[0].real)**2 == n**2 - (n - m)**2 else int(n - x[1].real)
					b = (n - m)
					c = n
					if a + b + c == 1000:
						# Colored output to emphasize the result
						print(f'{Fore.GREEN}')
						print('Pythagorean triplet: {0}^2 + {1}^2 = {2}^2'.format(a, b, c))
						print('Sum: {0} + {1} + {2} = {3}'.format(a, b, c, a + b + c))
						print('Product: {0} * {1} * {2} = {3}'.format(a, b, c, a * b * c))
						print(f'{Style.RESET_ALL}')
					else:
						# Normal output
						print('Pythagorean triplet: {0}^2 + {1}^2 = {2}^2'.format(a, b, c))
				m = m + 1
			n = n + 1
	
	# Same solution, just with information about
	# the occurencies of a certain pythagorean triplet
	# and with termination threshold
	@classmethod
	def solution_2(self, threshold):
		n = 1
		occurencies = {}
		while threshold > n:
			m = 1
			occurencies[n] = 0
			while (n - m)**2 > (n**2)/2:
				# Solve quadratic function
				x = self.solveQuadraticFunction(1, -2*n, (n**2 - sum([2*(n-x) - 1 for x in range(0, m)])), True)
				if float(x[0].real).is_integer() and float(x[1].real).is_integer():
					occurencies[n] = occurencies[n] + 1
				m = m + 1
			n = n + 1
		return occurencies
	
	@classmethod
	def solveQuadraticFunction(self, a, b, c, noncomplexflag = False):
		d = (b**2) - (4*a*c)
		sol1 = (-b-cmath.sqrt(d))/(2*a)
		sol2 = (-b+cmath.sqrt(d))/(2*a)
		solutions = []

		if noncomplexflag:
			if sol1.imag == 0:
				solutions.append(sol1)
			if sol2.imag == 0:
				solutions.append(sol2)
		else:
			solutions = [sol1, sol2]
			
		return solutions
	
	# Simple bruteforce O(n^3)
	@classmethod
	def tripletFinder(self, n):
		for c in range(1, n):
			for a in range(1, n):
				for b in range(1, n):
					if math.pow(c, 2) == math.pow(a, 2) + math.pow(b, 2):
						print("{0}^2 = {1}^2 + {2}^2".format(c, a, b))

	# Dynamic programming, where the result is saved in a list
	@classmethod
	def dynamictripletFinder(self, n):
		Q = [1]
		firstElement = len(Q) - 1
		for i in range(2, n):
			c_pow2 = math.pow(i, 2)
			a_pow2 = Q[-1]
			b_pow2 = c_pow2 - a_pow2
			if b_pow2 in Q:
				print("{0}^2 = {1}^2 + {2}^2".format(i, int(math.sqrt(a_pow2)), int(math.sqrt(b_pow2))))
			Q.append(int(c_pow2))
	
	# Solution in linear time
	@classmethod
	def lineartripletFinder(self, n):
		counter = 0
		for c in range(1, n):
			# print("============== {0} ==============".format(c))
			a = 1
			b = 2*c*c
			n1 = a + b + 2*c
			n2 = a + b - 2*c
			# if (n1 - a) > 0 and (n1 - b) > 0:
			# print("{0}^2 = {1}^2 + {2}^2".format(n1, n1 - a, n1 - b))
			counter += 1
			# if (n2 - a) > 0 and (n2 - b) > 0:
			# print("{0}^2 = {1}^2 + {2}^2".format(n2, n2 - a, n2 - b))
			#counter += 1

			a = 2
			b = c*c
			n1 = a + b + 2*c
			n2 = a + b - 2*c
			# if (n1 - a) > 0 and (n1 - b) > 0:
			# print("{0}^2 = {1}^2 + {2}^2".format(n1, n1 - a, n1 - b))
			counter += 1
			# if (n2 - a) > 0 and (n2 - b) > 0:
			# print("{0}^2 = {1}^2 + {2}^2".format(n2, n2 - a, n2 - b))
			#counter += 1

			a = 2*c
			b = c
			n1 = a + b + 2*c
			n2 = a + b - 2*c
			# if (n1 - a) > 0 and (n1 - b) > 0:
			# print("{0}^2 = {1}^2 + {2}^2".format(n1, n1 - a, n1 - b))
			counter += 1
			# if (n2 - a) > 0 and (n2 - b) > 0:
			# print("{0}^2 = {1}^2 + {2}^2".format(n2, n2 - a, n2 - b))
			#counter += 1
		return counter

class p10_summation_of_primes():
	# Solution with the
	# Primzahlsieb des Eratosthenes
	# (too slow for all primes below 2.000.000)
	@classmethod
	def solution_1(self, n):
		numbers = list(range(2, n + 1))
		offsetindex = 1
		for m in range(2, int(math.sqrt(n)) + 1):
			for i in numbers[offsetindex:]:
				if i % m == 0:
					numbers.remove(i)
			offsetindex = offsetindex + 1
		return sum(numbers)
	
	# Simple iteration
	@classmethod
	def solution_2(self, n):
		sum = 2
		for number in range(3, n, 2):
			if p3_largest_prime_factor.isPrimeNumberFaster(number):
				sum += number
		return sum
	
	# Function to list the differences between primes to n
	@classmethod
	def primeDifferences(self, n):
		primes = []
		for number in range(2, n + 1):
			if p3_largest_prime_factor.isPrimeNumberFaster(number):
				primes.append(number)
		differences = []
		for index in range(len(primes) - 1):
			differences.append(primes[index + 1] - primes[index])
		return differences

class p11_largest_product_in_a_grid():
	grid = (
		(8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8),
		(49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0),
		(81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65),
		(52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91),
		(22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80),
		(24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50),
		(32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70),
		(67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21),
		(24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72),
		(21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95),
		(78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92),
		(16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57),
		(86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58),
		(19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40),
		(4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66),
		(88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69),
		(4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36),
		(20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16),
		(20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54),
		(1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48),
	)
	# Solution which iterates through every dimension
	# separately (4 fixed adjacents and dynamic grid)
	@classmethod
	def solution_1(self, adjacents):
		highestProduct = 1

		# 135° degree
		for row in range(len(self.grid) - adjacents, -1, -1):
			x = 0
			y = 0
			while (x + 3) < len(self.grid) and (y + row + 3) < len(self.grid):
				product = self.grid[y + row][x] * self.grid[(y + row) + 1][x + 1] * self.grid[(y + row) + 2][x + 2] * self.grid[(y + row) + 3][x + 3]
				if product > highestProduct:
					highestProduct = product
				x += 1
				y += 1
		for column in range(len(self.grid) - adjacents, 0, -1):
			x = 0
			y = 0
			while (x + column + 3) < len(self.grid) and (y + 3) < len(self.grid):
				product = self.grid[y][x + column] * self.grid[y + 1][(x + column) + 1] * self.grid[y + 2][(x + column) + 2] * self.grid[y + 3][(x + column) + 3]
				if product > highestProduct:
					highestProduct = product
				x += 1
				y += 1

		# 90° degree
		for column in range(0, len(self.grid)):
			y = 0
			while (y + 3) < len(self.grid):
				product = self.grid[y][column] * self.grid[y + 1][column] * self.grid[y + 2][column] * self.grid[y + 3][column]
				if product > highestProduct:
					highestProduct = product
				y += 1
		
		# 45° degrees
		for row in range(adjacents - 1, len(self.grid)):
			x = 0
			y = 0
			while (x + 3) < len(self.grid) and (y + row - 3) > 0:
				product = self.grid[y + row][x] * self.grid[(y + row) - 1][x + 1] * self.grid[(y + row) - 2][x + 2] * self.grid[(y + row) - 3][x + 3]
				if product > highestProduct:
					highestProduct = product
				x += 1
				y -= 1
		for column in range(1, len(self.grid) - adjacents):
			x = 0
			y = 0
			while (x + column + 3) < len(self.grid) and (y - 3) > 0:
				product = self.grid[y][x + column] * self.grid[y - 1][x + column + 1] * self.grid[y - 2][x + column + 2] * self.grid[y - 3][x + column + 3]
				if product > highestProduct:
					highestProduct = product
				x += 1
				y -= 1
		# 0° degree
		for row in range(0, len(self.grid)):
			x = 0
			while (x + 3) < len(self.grid):
				product = self.grid[row][x] * self.grid[row][x + 1] * self.grid[row][x + 2] * self.grid[row][x + 3]
				if product > highestProduct:
					highestProduct = product
				x += 1
		return highestProduct

class p12_highly_divisible_triangular_number():
	# Simple solution with iteration
	# Too slow for 500 divisors
	@classmethod
	def solution_1(self, divisorthreshold):
		n = 0
		divisors = 0
		triangleNumber = 0
		while divisorthreshold >= divisors:
			divisors = 0
			triangleNumber = (n + 1) * n/2
			for i in range(2, int(triangleNumber / 2) + 1):
				if triangleNumber % i == 0:
					divisors += 1
			divisors += 2
			n += 1
		return { int(triangleNumber): divisors }

	# Faster solution with sqrt
	@classmethod
	def solution_2(self, divisorthreshold):
		n = 0
		divisors = 0
		triangleNumber = 0
		while divisorthreshold >= divisors:
			divisors = 0
			triangleNumber = (n + 1) * n/2
			for i in range(2, int(math.sqrt(triangleNumber)) + 1):
				if triangleNumber % i == 0:
					# Adding +2 since every divisor has its counter-part
					divisors += 2
			# Adding +2 since 1 and n are always divisors
			divisors += 2
			n += 1
		return { int(triangleNumber): divisors }

	# Function to return all divisors for each number
	# (no actual solution to the problem)
	@classmethod
	def returnDivisorsForNumbers(self, n, primefilter = False):
		divisors = {}
		for number in range(0, n + 1):
			divisors[number] = []
			for i in range(2, int(number / 2) + 1):
				if number % i == 0:
					divisors[number].append(i)
			if primefilter and len(divisors[number]) == 0:
				divisors.pop(number)
		return divisors

class p13_large_sum():
	grid = (
		"37107287533902102798797998220837590246510135740250",
		"46376937677490009712648124896970078050417018260538",
		"74324986199524741059474233309513058123726617309629",
		"91942213363574161572522430563301811072406154908250",
		"23067588207539346171171980310421047513778063246676",
		"89261670696623633820136378418383684178734361726757",
		"28112879812849979408065481931592621691275889832738",
		"44274228917432520321923589422876796487670272189318",
		"47451445736001306439091167216856844588711603153276",
		"70386486105843025439939619828917593665686757934951",
		"62176457141856560629502157223196586755079324193331",
		"64906352462741904929101432445813822663347944758178",
		"92575867718337217661963751590579239728245598838407",
		"58203565325359399008402633568948830189458628227828",
		"80181199384826282014278194139940567587151170094390",
		"35398664372827112653829987240784473053190104293586",
		"86515506006295864861532075273371959191420517255829",
		"71693888707715466499115593487603532921714970056938",
		"54370070576826684624621495650076471787294438377604",
		"53282654108756828443191190634694037855217779295145",
		"36123272525000296071075082563815656710885258350721",
		"45876576172410976447339110607218265236877223636045",
		"17423706905851860660448207621209813287860733969412",
		"81142660418086830619328460811191061556940512689692",
		"51934325451728388641918047049293215058642563049483",
		"62467221648435076201727918039944693004732956340691",
		"15732444386908125794514089057706229429197107928209",
		"55037687525678773091862540744969844508330393682126",
		"18336384825330154686196124348767681297534375946515",
		"80386287592878490201521685554828717201219257766954",
		"78182833757993103614740356856449095527097864797581",
		"16726320100436897842553539920931837441497806860984",
		"48403098129077791799088218795327364475675590848030",
		"87086987551392711854517078544161852424320693150332",
		"59959406895756536782107074926966537676326235447210",
		"69793950679652694742597709739166693763042633987085",
		"41052684708299085211399427365734116182760315001271",
		"65378607361501080857009149939512557028198746004375",
		"35829035317434717326932123578154982629742552737307",
		"94953759765105305946966067683156574377167401875275",
		"88902802571733229619176668713819931811048770190271",
		"25267680276078003013678680992525463401061632866526",
		"36270218540497705585629946580636237993140746255962",
		"24074486908231174977792365466257246923322810917141",
		"91430288197103288597806669760892938638285025333403",
		"34413065578016127815921815005561868836468420090470",
		"23053081172816430487623791969842487255036638784583",
		"11487696932154902810424020138335124462181441773470",
		"63783299490636259666498587618221225225512486764533",
		"67720186971698544312419572409913959008952310058822",
		"95548255300263520781532296796249481641953868218774",
		"76085327132285723110424803456124867697064507995236",
		"37774242535411291684276865538926205024910326572967",
		"23701913275725675285653248258265463092207058596522",
		"29798860272258331913126375147341994889534765745501",
		"18495701454879288984856827726077713721403798879715",
		"38298203783031473527721580348144513491373226651381",
		"34829543829199918180278916522431027392251122869539",
		"40957953066405232632538044100059654939159879593635",
		"29746152185502371307642255121183693803580388584903",
		"41698116222072977186158236678424689157993532961922",
		"62467957194401269043877107275048102390895523597457",
		"23189706772547915061505504953922979530901129967519",
		"86188088225875314529584099251203829009407770775672",
		"11306739708304724483816533873502340845647058077308",
		"82959174767140363198008187129011875491310547126581",
		"97623331044818386269515456334926366572897563400500",
		"42846280183517070527831839425882145521227251250327",
		"55121603546981200581762165212827652751691296897789",
		"32238195734329339946437501907836945765883352399886",
		"75506164965184775180738168837861091527357929701337",
		"62177842752192623401942399639168044983993173312731",
		"32924185707147349566916674687634660915035914677504",
		"99518671430235219628894890102423325116913619626622",
		"73267460800591547471830798392868535206946944540724",
		"76841822524674417161514036427982273348055556214818",
		"97142617910342598647204516893989422179826088076852",
		"87783646182799346313767754307809363333018982642090",
		"10848802521674670883215120185883543223812876952786",
		"71329612474782464538636993009049310363619763878039",
		"62184073572399794223406235393808339651327408011116",
		"66627891981488087797941876876144230030984490851411",
		"60661826293682836764744779239180335110989069790714",
		"85786944089552990653640447425576083659976645795096",
		"66024396409905389607120198219976047599490197230297",
		"64913982680032973156037120041377903785566085089252",
		"16730939319872750275468906903707539413042652315011",
		"94809377245048795150954100921645863754710598436791",
		"78639167021187492431995700641917969777599028300699",
		"15368713711936614952811305876380278410754449733078",
		"40789923115535562561142322423255033685442488917353",
		"44889911501440648020369068063960672322193204149535",
		"41503128880339536053299340368006977710650566631954",
		"81234880673210146739058568557934581403627822703280",
		"82616570773948327592232845941706525094512325230608",
		"22918802058777319719839450180888072429661980811197",
		"77158542502016545090413245809786882778948721859617",
		"72107838435069186155435662884062257473692284509516",
		"20849603980134001723930671666823555245252804609722",
		"53503534226472524250874054075591789781264330331690"
	)
	@classmethod
	def solution_1(self, digits):
		firstTenDigits = ""
		remainder = 0
		for n in range(digits):
			digitsum = remainder
			for number in self.grid:
				digitsum += int(number[49 - n:50 - n])
			quotient = digitsum / 10
			remainder = int(quotient)
			firstTenDigits += str(quotient)[-1]
		# [::-1] used to reverse (mirror) the string (extended slice syntax)
		return firstTenDigits[::-1]

class p14_longest_collatz_sequence():
	# Simple solution with iteration
	@classmethod
	def solution_1(self, n):
		maxSequence = 0
		for sequence in range(1, n):
			counter = 0
			while sequence > 1:
				if sequence % 2 == 0:
					sequence = sequence / 2
				else:
					sequence = (3 * sequence + 1) / 2
					counter += 1
				counter += 1
			if counter > maxSequence:
				maxSequence = counter
		return maxSequence
	
	# Same solution just to display the sequences
	@classmethod
	def solution_2(self, n, oddFlag = False):
		sequenceList = []
		for sequence in range(1, n):
			subSequence = [sequence]
			while sequence > 1:
				if sequence % 2 == 0:
					sequence = int(sequence / 2)
				else:
					sequence = (3 * sequence + 1)
				subSequence.append(sequence)
			if oddFlag:
				sequenceList.append(list(filter(lambda x: x % 2 != 0, subSequence)))
			else:
				sequenceList.append(subSequence)
		return sequenceList

	# Function to find a integer divider of 2^m for m in 3n + 1
	@classmethod
	def findDivider(self, threshold):
		dividers = {}
		for n in range(1, threshold + 1):
			m = math.log2(3 * n + 1)
			if float.is_integer(m):
				dividers[n] = int(m)
		return dividers

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

print(p9_special_pythagorean_triplet.lineartripletFinder(100000000))