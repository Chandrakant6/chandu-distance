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

def plot_3d_lines(lines, colors, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i, line in enumerate(lines):
        x, y, z = line
        ax.plot3D(x, y, z, color=colors[i], label=labels[i])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Line Plot')
    ax.legend()

    plt.show()


# Example usage:
if __name__ == '__main__':
    lines = [
        (np.linspace(6, 4), np.linspace(6, 8), np.linspace(0, 2)),
        (np.linspace(4, 4), np.linspace(8, 8), np.linspace(2, 7)),
    ]
    
    colors = ['gray', 'blue']
    labels = ['Line 1', 'Line 2']
    
    plot_3d_lines(lines, colors, labels)
