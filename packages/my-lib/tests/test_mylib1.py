from mylib1 import hello, add, subtract


def test_hello():
    """Test that the hello function returns the expected string."""
    assert hello() == "Hello from my-lib!"


def test_add():
    """Test the add function with various inputs."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 3.5) == 6.0


def test_subtract():
    """Test the subtract function with various inputs."""
    assert subtract(3, 2) == 1
    assert subtract(1, 1) == 0
    assert subtract(0, 0) == 0
    assert subtract(2.5, 1.5) == 1.0
    assert subtract(-1, -1) == 0
