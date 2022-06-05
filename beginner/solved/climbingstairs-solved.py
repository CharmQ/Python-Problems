'''
Climbing Stairs Problem

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

'''

def stairs(n):
	if n == 0:
		print(f'0')
	else:
		ways = 1
		curr = 1
		prev = 1
		for i in range(n - 1):
			ways = curr + prev
			prev = curr
			curr = ways
		return ways