# System Modules
import sys
import os

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_area_of_circle_negative_radius():
    """Test with a negative radius (should raise ValueError)."""
    radius = -1
    try:
        area_of_circle(radius)
        assert False, "Expected ValueError for negative radius"
    except ValueError:
        pass


def test_area_of_circle_non_numeric():
    """Test with a non-numeric radius (should raise TypeError)."""
    radius = "abc"
    try:
        area_of_circle(radius)
        assert False, "Expected TypeError for non-numeric radius"
    except TypeError:
        pass


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 55


def test_get_nth_fibonacci_negative():
    """Test with a negative n (should raise ValueError)."""
    n = -5
    try:
        get_nth_fibonacci(n)
        assert False, "Expected ValueError for negative n"
    except ValueError:
        pass


def test_get_nth_fibonacci_non_integer():
    """Test with a non-integer n (should raise TypeError)."""
    n = 2.5
    try:
        get_nth_fibonacci(n)
        assert False, "Expected TypeError for non-integer n"
    except TypeError:
        pass

