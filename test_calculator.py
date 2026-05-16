import pytest

from calculator import add, divide, multiply, percentage, power, square_root, subtract

# --- Basic tests ---


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5.0


# --- Edge cases ---


def test_add_negative_numbers():
    assert add(-5, -3) == -8


def test_add_zero():
    assert add(0, 100) == 100


def test_multiply_by_zero():
    assert multiply(999, 0) == 0


def test_divide_result_is_float():
    assert isinstance(divide(7, 2), float)


# --- Error cases ---


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_square_root_negative_raises_error():
    with pytest.raises(ValueError, match="Cannot take square root"):
        square_root(-9)


def test_percentage_zero_total_raises_error():
    with pytest.raises(ValueError):
        percentage(50, 0)


# --- Parametrize: test many inputs in one test ---


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (100, -50, 50),
        (1.5, 2.5, 4.0),
    ],
)
def test_add_multiple_inputs(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (4, 2.0),
        (9, 3.0),
        (0, 0.0),
        (2, 1.4142135623730951),
    ],
)
def test_square_root(n, expected):
    assert square_root(n) == pytest.approx(expected)


# --- Grouping tests with a class ---


class TestPercentage:
    def test_basic(self):
        assert percentage(50, 200) == 25.0

    def test_full_amount(self):
        assert percentage(200, 200) == 100.0

    def test_zero_part(self):
        assert percentage(0, 100) == 0.0

    def test_over_hundred(self):
        assert percentage(150, 100) == 150.0
