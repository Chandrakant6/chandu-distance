from math import sqrt
import random
random.seed(0)

# third iteration for any no. of dimensions
def calc(a: list[float], b: list[float]) -> list[list[float],list[float],float]:  
    roots = [sqrt(i) for i in range(len(a)+1,1,-1)]
    vector = [abs(i-j) for i, j in zip(a, b)]
    vector.sort()
    
    path = [vector[0]] + [vector[i+1]-vector[i] for i in range(len(vector)-1)]
    return vector, path, sum([i*j for i, j in zip(path, roots)])
