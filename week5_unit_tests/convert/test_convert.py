import pytest

from week5_unit_tests.convert.convert import convert


def test_int():
    assert convert(1) == 149597870700
    assert convert(2) == 299195741400


def test_type_error():
    with pytest.raises(TypeError):
        convert("test")


def test_float():
    assert convert(1.5) == 224396806050
    assert convert(0.001) == pytest.approx(149597870.691, abs=0.01)
