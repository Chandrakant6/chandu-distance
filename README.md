# Chandu Distance

A custom distance calculation algorithm that combines elements of Manhattan and Euclidean distance for multi-dimensional spaces. Perfect for grid-based games where diagonal movement has different costs than axial movement.

## Features

- **Multi-dimensional support**: Works with any number of dimensions (1D, 2D, 3D, etc.)
- **Custom weighting**: Uses square root-based weights for different movement directions
- **Game-optimized**: Ideal for pathfinding in grid-based games
- **Robust validation**: Comprehensive input validation with clear error messages
- **Modular design**: Clean, testable, and maintainable code structure

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

# No additional dependencies required - uses only Python standard library
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

## API Reference

### `calc(a: list[float], b: list[float]) -> tuple[list[float], list[float], float]`

Calculate custom distance between two points in n-dimensional space.

**Parameters:**
- `a`: First point coordinates as list of floats
- `b`: Second point coordinates as list of floats

**Returns:**
- `vector`: Sorted absolute differences between coordinates
- `path`: Incremental differences for weighted calculation  
- `distance`: Final calculated distance value

**Raises:**
- `ValueError`: If inputs are invalid (empty, different lengths, etc.)

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

## License

[MIT License](LICENSE)

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.
