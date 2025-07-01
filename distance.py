from math import sqrt
from typing import Tuple

def chandu_len(a: list[float], b: list[float]) -> Tuple[list[float], list[float], float]:
    """
    Calculate custom distance between two points in n-dimensional space.
    
    This algorithm combines elements of Manhattan and Euclidean distance,
    useful for grid-based games where diagonal movement has different costs.
    """
    if not a or not b or len(a) != len(b):
        raise ValueError("Input lists must be non-empty and have the same length")
    
    roots = [sqrt(i) for i in range(len(a)+1, 1, -1)]
    vector = sorted([abs(i-j) for i, j in zip(a, b)])
    path = [vector[0]] + [vector[i+1]-vector[i] for i in range(len(vector)-1)] if vector else []
    distance = sum(i*j for i, j in zip(path, roots))
    
    return vector, path, distance

def compute_segments(start, end): # or psuedo run length encoding
    """Minimal-turn run-length path between two nD points."""
    if len(start) != len(end):
        raise ValueError("Start and end points must have the same number of dimensions")
    delta = [e - s for s, e in zip(start, end)]
    signs = [1 if d > 0 else -1 if d < 0 else 0 for d in delta]
    remaining = [abs(d) for d in delta]
    non_zero = [r for r in remaining if r > 0]
    if len(non_zero) > 1 and all(v == non_zero[0] for v in non_zero):
        return [(tuple(signs), non_zero[0])]
    directions = []
    while any(remaining):
        dir_vec = tuple(signs[i] if remaining[i] else 0 for i in range(len(delta)))
        steps = min([remaining[i] for i in range(len(delta)) if dir_vec[i]])
        directions.append((dir_vec, steps))
        for i in range(len(remaining)):
            if dir_vec[i]:
                remaining[i] -= steps
    return directions

def get_keypoints(start, directions):
    """Expand run-length path to full list of points."""
    path = [list(start)]
    current = list(start)
    for direction, steps in directions:
        current = [c + d * steps for c, d in zip(current, direction)]
        path.append(current[:])
    return path

def get_path_length(segments):
    """Sum the total length of all segments."""
    return sum(length for _, length in segments)

# Example usage:
if __name__ == "__main__":
    start = (3, -7, 0)
    end = (9, -14, 6)
    path_steps = compute_segments(start, end)
    path_len = get_path_length(path_steps)
    full_path = get_keypoints(start, path_steps)
    _, _, chandu_length = chandu_len(start, end)

    print("Directional Steps:")
    for step in path_steps:
        print(f"Move {step[0]} for {step[1]} steps")

    print("\nIntermediate Points:")
    for point in full_path:
        print(point)

    print("\nChandu Length:", chandu_length)
    print("Path Length (segments):", path_len)  