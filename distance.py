from math import sqrt

def calc(a, b, K=math.sqrt(2)) # calculated diatances
	ax, ay = a
	bx, by = b
	
	x, y = abs(ax-bx), abs(ay, by)
	return max(x, y) + min(x, y) * (k - 1)
