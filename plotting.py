import matplotlib.pyplot as plt

from distance import *

def plot_path(points, start=None, end=None):
    """
    Plot the path in 2D or 3D depending on dimensionality. Optionally plot a dashed Euclidean line and a dotted Manhattan line if start and end are provided.
    """
    dim = len(points[0])
    if dim == 2:
        x, y = zip(*points)
        plt.plot(x, y, marker='o', label='Chandu Path')
        if start is not None and end is not None:
            # Euclidean line
            plt.plot([start[0], end[0]], [start[1], end[1]], 'k--', label='Euclidean Line')
            # Manhattan line (axis-aligned: start to (end[0], start[1]) to end)
            plt.plot([start[0], end[0]], [start[1], start[1]], 'r:', label='Manhattan Line')
            plt.plot([end[0], end[0]], [start[1], end[1]], 'r:')
        plt.title("2D Path with Euclidean and Manhattan Lines" if start and end else "2D Path")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        if start and end:
            plt.legend()
        plt.show()
    elif dim == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x, y, z = zip(*points)
        ax.plot(x, y, z, marker='o', label='Chandu Path')
        if start is not None and end is not None:
            # Euclidean line
            ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], 'k--', label='Euclidean Line')
            # Manhattan line (axis-aligned: start -> (end[0], start[1], start[2]) -> (end[0], end[1], start[2]) -> end)
            ax.plot([start[0], end[0]], [start[1], start[1]], [start[2], start[2]], 'r:', label='Manhattan Line')
            ax.plot([end[0], end[0]], [start[1], end[1]], [start[2], start[2]], 'r:')
            ax.plot([end[0], end[0]], [end[1], end[1]], [start[2], end[2]], 'r:')
        ax.set_title("3D Path with Euclidean and Manhattan Lines" if start and end else "3D Path")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        if start and end:
            ax.legend()
        plt.show()
    else:
        raise ValueError("Only 2D and 3D plotting is supported")


# Example usage:
if __name__ == "__main__":
    start = (3, -7)
    end = (12, -12)
    segments = compute_segments(start, end)
    turning_points = get_keypoints(start, segments)
    vector, path_dist, _, chandu_dist = chandu_len(start, end)

    print("Directional Segments:")
    for step in segments:
        print(f"Move {step[0]} for {step[1]} steps")

    print("\nTurning Points:")
    for point in turning_points:
        print(point)

    print("\nChandu Distance:", chandu_dist)
    print("Path Vector:", vector)
    print("Path Distance:", path_dist)

    # Plot the path with Euclidean line
    plot_path(turning_points, start, end)
