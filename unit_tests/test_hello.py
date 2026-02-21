from unit_tests.hello import hello


def test_default():
    assert hello() == "hello, world"


def test_hello():
    assert hello("Alice") == "hello, Alice"
    assert hello() == "hello, world"


def test_integer():
    assert hello(123) == "hello, 123"
