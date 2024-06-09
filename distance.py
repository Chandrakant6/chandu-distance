from math import sqrt

# calculated diatances btw 2 points in 2D space (in grid space)
def calc(a, b, K=math.sqrt(2)) 
	ax, ay = a
	bx, by = b
	
	x, y = abs(ax-bx), abs(ay, by)
	return max(x, y) + min(x, y) * (k - 1)

# for nD space 
def calc_general(a: list[float], b: list[float]): 
    p = []
    roots: list[float] = [sqrt(i+1) for i,_ in enumerate(a)][::-1]

    for i, j in zip(a, b):
        p.append(abs(i-j))
    p.sort()
    
    dist = 0
    while len(p) > 0 :
        for i, j in zip(p, roots):
            dist += p[0]*roots[0]
            p = np.subtract(p[1:], p[0])
            roots.pop(0)
    return dist

# third iteration for any no. of dimensions
def calc_gen2(a: list[float], b: list[float]):  
    point = [abs(i-j) for i, j in zip(a, b)].sort()
    roots = [sqrt(i) for i in range(1,len(a)+1)][::-1]

    vector = [point[0]] + [point[i+1]-point[i] for i in range(len(point)-1)]

    return point, vector, sum([i*j for i, j in zip(vector, roots)])
