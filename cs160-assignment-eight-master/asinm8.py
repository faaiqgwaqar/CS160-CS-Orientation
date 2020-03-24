from collections import deque

def palindrome(word):
	for i in range(len(word)//2):
		if word[i] != word[-1-i]:
			return False
	return True

def countStairs(n):
	count = 0
	
	def calculate(x):
		if x < 2:
			nonlocal count
			count += 1
			return
	
		deque((calculate(x-i)
			for i in range(1, min(4, x+1))), maxlen=0)
	calculate(n)
	return count

