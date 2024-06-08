from math import sqrt

# calculated diatances btw 2 points in 2D space (in grid space)
def calc(a, b, K=math.sqrt(2)) 
	ax, ay = a
	bx, by = b
	
	x, y = abs(ax-bx), abs(ay, by)
	return max(x, y) + min(x, y) * (k - 1)
