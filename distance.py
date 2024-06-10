from math import sqrt
import random
random.seed(0)

# third iteration for any no. of dimensions
def calc(a: list[float], b: list[float]) -> tuple[list[float],list[float],float]:  
    vector = [abs(i-j) for i, j in zip(a, b)]
    vector.sort()
    roots = [sqrt(i) for i in range(1,len(a)+1)][::-1]

    path = [vector[0]] + [vector[i+1]-vector[i] for i in range(len(vector)-1)]
    return vector, path, sum([i*j for i, j in zip(path, roots)])

def plotline2D(*args):
    plt.plot(*zip(*args))
    plt.show()


# testing
if __name__ == '__main__':
    D = 2 #domensions

    # points
    a = [random.randrange(0,10) for _ in range(D)] 
    b = [random.randrange(0,10) for _ in range(D)]
    print(distance(a,[2,6] b))
