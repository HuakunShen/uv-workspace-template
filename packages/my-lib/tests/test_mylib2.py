import io
import pytest
from contextlib import redirect_stdout
from mylib2 import hello, multiply, divide


def test_hello():
    """Test that the hello function prints the expected string."""
    f = io.StringIO()
    with redirect_stdout(f):
        hello()
    assert f.getvalue().strip() == "lib2"


def test_multiply():
    """Test the multiply function with various inputs."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
    assert multiply(2.5, 2) == 5.0
    assert multiply(-2, -3) == 6


def test_divide():
    """Test the divide function with various inputs."""
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3
    assert divide(0, 5) == 0
    assert divide(-6, -2) == 3


def test_divide_by_zero():
    """Test that dividing by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)
