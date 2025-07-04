# Chandu Distance

A custom distance calculation algorithm that combines elements of Manhattan and Euclidean distance for multi-dimensional spaces. Perfect for grid-based games where diagonal movement has different costs than axial movement.

## Features

- **Multi-dimensional support**: Works with any number of dimensions (1D, 2D, 3D, etc.)
- **Custom weighting**: Uses square root-based weights for different movement directions
- **Game-optimized**: Ideal for pathfinding in grid-based games
- **Robust validation**: Comprehensive input validation with clear error messages
- **Modular design**: Clean, testable, and maintainable code structure
- **Visualization tools**: Built-in plotting capabilities for analysis and demonstration

## Use Cases

- **2D Grid Games**: Calculate distance between points where players can move in 1 or 2 axes at once
- **3D Games**: Handle diagonal movement on stairs or ramps (movement in 3 axes simultaneously)
- **Pathfinding**: Custom distance metrics for A* or other pathfinding algorithms
- **Game AI**: Distance calculations for enemy movement or targeting systems

## Installation

```bash
# Clone the repository
git clone https://github.com/chandrakant6/chandu-distance.git
cd chandu-distance

# Install dependencies (for plotting functionality)
pip install -r requirements.txt
```

## Usage

### Basic Example

```python
from distance import calc

# 2D distance calculation
point_a = [0, 0]
point_b = [3, 4]
vector, path, distance = calc(point_a, point_b)

print(f"Distance: {distance:.2f}")
print(f"Vector: {vector}")
print(f"Path: {path}")
```

### 3D Example

```python
# 3D distance calculation
point_a = [1, 2, 3]
point_b = [4, 1, 6]
vector, path, distance = calc(point_a, point_b)

print(f"3D Distance: {distance:.2f}")
```

### Error Handling

```python
try:
    # This will raise a ValueError
    calc([1, 2], [1, 2, 3])  # Different dimensions
except ValueError as e:
    print(f"Error: {e}")
```

## Visualization

The `plotting.py` module provides simple visualization tools:

### Distance Comparison
```python
from plotting import plot_comparison

# Compare Manhattan, Euclidean, and Chandu distance
plot_comparison(center=[0, 0], max_dist=5)
```

### Analysis
```python
from plotting import plot_analysis

# Analyze the components of distance calculation
plot_analysis([0, 0], [3, 4])
```

### 3D Visualization
```python
from plotting import plot_path

start = [0, 0, 0]
end = [1, 2, 3]

# Compute Chandu path data (assuming compute_chandu_path_data and expand_path are available)
_, _, _, chandu_dist, segments = compute_chandu_path_data(start, end)
path_points = expand_path(start, segments)

print("Directional Segments:")
for direction, step in segments:
    print(f"-> {direction} x {step}")

print("\nTurning Points:")
for point in path_points:
    print(point)

print("\nChandu Distance:", chandu_dist)

plot_path(path_points, start, end)  # Plots Chandu, Euclidean (dashed), and Manhattan (dotted) lines
```

- The plot will show the Chandu path, a dashed Euclidean line, and a dotted Manhattan line between the start and end points.
- Output for directional segments now uses ASCII arrows and 'x' (e.g., `-> (1, 1, 1) x 1`).

### Bar Chart Comparison
```python
from plotting import plot_bar

# Compare different distance metrics
plot_bar([0, 0], [3, 4])
```

### Run All Examples
```python
# Run all visualization examples
python plotting.py
```

## API Reference (no API yet)

### `chandu_len(a: list[float], b: list[float]) -> tuple[list[float], list[float], float]`
Calculate the custom Chandu distance between two points in n-dimensional space.
- Returns: (vector, path, distance)

### `compute_segments(start, end) -> list[tuple[tuple[int], int]]`
Compute a minimal-turn, run-length encoded path between two nD points.
- Returns: List of (direction_vector, length) steps.

### `get_keypoints(start, segments) -> list[list[int]]`
Expand the run-length path to a full list of keypoints (turning points) along the path.

### `get_path_length(segments) -> int`
Sum the total length of all segments in the run-length encoded path.

### `plot_path(points)`
Plot the path in 2D or 3D depending on the dimensionality of the points.

## Usage Example

```python
from distance import chandu_len, compute_segments, get_keypoints, get_path_length
from plotting import plot_path

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
```

## Notes
- **Chandu Distance**: A custom metric combining elements of Manhattan and Euclidean distances, useful for grid-based games.
- **Path Length**: The total number of steps along the minimal-turn path (may differ from Chandu distance).
- **Run-Length Encoding**: Efficiently represents straight segments in the path.

## Algorithm Details

The algorithm works by:

1. **Weight Generation**: Creates weights using square roots of descending integers
2. **Difference Calculation**: Computes absolute differences between corresponding coordinates
3. **Sorting**: Sorts differences in ascending order
4. **Path Calculation**: Creates incremental differences for weighted calculation
5. **Weighted Sum**: Multiplies path increments by weights to get final distance

For 2D points `[0,0]` to `[3,4]`:
- Manhattan distance: 7
- Euclidean distance: 5
- Chandu distance: ~6.61 (provides middle ground)

## Testing

```bash
# Run tests (if test file exists)
python test_distance.py
```

## Dependencies

- **Core**: No external dependencies (uses Python standard library)
- **Visualization**: 
  - `matplotlib>=3.5.0` - For plotting and visualization
  - `numpy>=1.21.0` - For numerical operations

## License

[MIT License](LICENSE)

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.
