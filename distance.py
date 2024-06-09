from math import sqrt

# third iteration for any no. of dimensions
def calc(a: list[float], b: list[float]) -> tuple[list[float],list[float],float]:  
    point = [abs(i-j) for i, j in zip(a, b)].sort()
    roots = [sqrt(i) for i in range(1,len(a)+1)][::-1]

    vector = [point[0]] + [point[i+1]-point[i] for i in range(len(point)-1)]

    return point, vector, sum([i*j for i, j in zip(vector, roots)])
