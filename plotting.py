import matplotlib.pyplot as plt

from distance import *

def plot_path(points):
    """
    Plot the path in 2D or 3D depending on dimensionality.
    """
    dim = len(points[0])
    if dim == 2:
        x, y = zip(*points)
        plt.plot(x, y, marker='o')
        plt.title("2D Path")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()
    elif dim == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x, y, z = zip(*points)
        ax.plot(x, y, z, marker='o')
        ax.set_title("3D Path")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.show()
    else:
        raise ValueError("Only 2D and 3D plotting is supported")


# Example usage:
if __name__ == "__main__":
    start = (3, -7, 0)
    end = (9, -12, 6)
    segments = compute_segments(start, end)
    turning_points = get_keypoints(start, segments)
    total_length = get_path_length(segments)
    vector, path_dist, chandu_dist = chandu_len(start, end)

    print("Directional Segments:")
    for step in segments:
        print(f"Move {step[0]} for {step[1]} steps")

    print("\nTurning Points:")
    for point in turning_points:
        print(point)

    print("\nTotal Path Length:", total_length)
    print("Chandu Distance:", chandu_dist)
    print("Path Vector:", vector)
    print("Path Distance:", path_dist)

    # Plot the path
    plot_path(turning_points)
