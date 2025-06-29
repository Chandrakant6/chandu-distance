from math import sqrt
from typing import Tuple, List

def _validate_inputs(a: List[float], b: List[float]) -> None:
    """Validate input parameters for distance calculation."""
    if not a or not b or len(a) != len(b):
        raise ValueError("Input lists must be non-empty and have the same length")

def _generate_weights(dimensions: int) -> List[float]:
    """Generate weight factors for distance calculation."""
    return [sqrt(i) for i in range(dimensions+1, 1, -1)]

def _calculate_differences(a: List[float], b: List[float]) -> List[float]:
    """Calculate and sort absolute differences between coordinates."""
    return sorted([abs(i-j) for i, j in zip(a, b)])

def _calculate_path(vector: List[float]) -> List[float]:
    """Calculate incremental differences for weighted path."""
    return [vector[0]] + [vector[i+1]-vector[i] for i in range(len(vector)-1)] if vector else []

def _calculate_weighted_distance(path: List[float], weights: List[float]) -> float:
    """Calculate the final weighted distance by multiplying path increments with weights."""
    return sum(i*j for i, j in zip(path, weights))

def calc(a: list[float], b: list[float]) -> Tuple[list[float], list[float], float]:
    """
    Calculate custom distance between two points in n-dimensional space.
    
    This algorithm combines elements of Manhattan and Euclidean distance,
    useful for grid-based games where diagonal movement has different costs.
    
    Args:
        a: First point coordinates as list of floats
        b: Second point coordinates as list of floats
        
    Returns:
        Tuple containing:
        - vector: Sorted absolute differences between coordinates
        - path: Incremental differences for weighted calculation
        - distance: Final calculated distance value
        
    Raises:
        ValueError: If inputs are invalid (empty, different lengths, etc.)
        
    Example:
        >>> calc([0, 0], [3, 4])
        ([3, 4], [3, 1], 6.61...)
        
        >>> calc([1, 2, 3], [4, 1, 6])
        ([1, 3, 3], [1, 2, 0], 5.18...)
    """
    _validate_inputs(a, b)
    
    roots = _generate_weights(len(a))
    vector = _calculate_differences(a, b)
    path = _calculate_path(vector)
    distance = _calculate_weighted_distance(path, roots)
    
    return vector, path, distance
