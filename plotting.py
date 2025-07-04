import matplotlib.pyplot as plt
from distance import compute_chandu_path_data, expand_path

def plot_path(points, start=None, end=None):
    """
    Plot Chandu path with optional Euclidean (dashed) and Manhattan (dotted) lines.
    Supports only 2D and 3D paths.
    """
    dim = len(points[0])
    
    if dim not in (2, 3):
        raise ValueError("Only 2D and 3D plotting is supported")
    
    # Unzip coordinates
    coords = list(zip(*points))

    # Plot
    fig = plt.figure()
    if dim == 2:
        plt.plot(*coords, marker='o', label='Chandu Path')
        if start and end:
            # Euclidean Line
            plt.plot([start[0], end[0]], [start[1], end[1]], 'k--', label='Euclidean Line')
            # Manhattan Path
            plt.plot([start[0], end[0]], [start[1], start[1]], 'r:', label='Manhattan Line')
            plt.plot([end[0], end[0]], [start[1], end[1]], 'r:')
            plt.legend()
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("2D Chandu Path")
        plt.grid(True)

    elif dim == 3:
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(*coords, marker='o', label='Chandu Path')
        if start and end:
            # Euclidean line
            ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], 'k--', label='Euclidean Line')
            # Manhattan-style axis-aligned lines
            x0, y0, z0 = start
            x1, y1, z1 = end
            ax.plot([x0, x1], [y0, y0], [z0, z0], 'r:', label='Manhattan Line')
            ax.plot([x1, x1], [y0, y1], [z0, z0], 'r:')
            ax.plot([x1, x1], [y1, y1], [z0, z1], 'r:')
            ax.legend()
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title("3D Chandu Path")

    plt.show()


# Example usage
if __name__ == "__main__":
    start = [0,0,0]
    end = [1,2,3]

    # Get all relevant data in one go
    _, _, _, chandu_dist, segments = compute_chandu_path_data(start, end)
    path_points = expand_path(start, segments)

    print("Directional Segments:")
    for direction, step in segments:
        print(f"-> {direction} x {step}")

    print("\nTurning Points:")
    for point in path_points:
        print(point)

    print("\nChandu Distance:", chandu_dist)

    plot_path(path_points, start, end)
