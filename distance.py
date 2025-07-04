from math import sqrt
from typing import List, Tuple

def compute_chandu_path_data(
    start: List[float], end: List[float]
) -> Tuple[List[float], List[float], int, float, List[Tuple[Tuple[int, ...], int]]]:
    """
    Compute:
    - Sorted axis differences
    - Path deltas (run-length encoded)
    - Max single-axis distance
    - Weighted Chandu distance
    - Directional segments (minimal-turn path)
    """
    if len(start) != len(end):
        raise ValueError("Start and end must have same dimensions")

    delta = [e - s for s, e in zip(start, end)]
    abs_deltas = [abs(d) for d in delta]
    signs = [1 if d > 0 else -1 if d < 0 else 0 for d in delta]

    # Chandu Length
    sorted_deltas = sorted(abs_deltas)
    path_deltas = [sorted_deltas[0]] + [
        sorted_deltas[i+1] - sorted_deltas[i] for i in range(len(sorted_deltas)-1)
    ] if sorted_deltas else []
    roots = [sqrt(i) for i in range(len(start)+1, 1, -1)]
    weighted_distance = sum(p * r for p, r in zip(path_deltas, roots))
    max_axis_step = sorted_deltas[-1] if sorted_deltas else 0

    # Directional segments (minimal-turn steps)
    if len(set(v for v in abs_deltas if v > 0)) == 1:
        segments = [(tuple(signs), abs_deltas[0])]
    else:
        remaining = abs_deltas[:]
        segments = []
        while any(remaining):
            direction = tuple(signs[i] if remaining[i] else 0 for i in range(len(delta)))
            step = min(remaining[i] for i, d in enumerate(direction) if d)
            segments.append((direction, step))
            for i, d in enumerate(direction):
                if d:
                    remaining[i] -= step

    return sorted_deltas, path_deltas, max_axis_step, weighted_distance, segments


def expand_path(start: List[int], segments: List[Tuple[Tuple[int, ...], int]]) -> List[List[int]]:
    """Expand directional segments into list of keypoints (actual path)."""
    path = [start[:]]
    current = start[:]
    for direction, step in segments:
        current = [c + d * step for c, d in zip(current, direction)]
        path.append(current[:])
    return path


# Example
if __name__ == "__main__":
    start = [0,0,0]
    end = [1,2,3]

    sorted_deltas, path_deltas, max_step, chandu_dist, segments = compute_chandu_path_data(start, end)
    path_points = expand_path(start, segments)

    print("Directional Segments:")
    for direction, step in segments:
        print(f"-> {direction} x {step}")

    print("\nPath Keypoints:")
    for point in path_points:
        print(point)

    print("\nChandu Length:", chandu_dist)
    print("Max Axis Step:", max_step)
