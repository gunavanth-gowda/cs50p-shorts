import pytest

from unit_tests.calculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-3) == 9
    assert square(-2) == 4


def test_zero():
    assert square(0) == 0


def test_string():
    with pytest.raises(TypeError):
        square("hello")
