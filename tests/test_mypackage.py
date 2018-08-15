import mypackage
import pytest


def test_hello():
    mypackage.hello()


def test_simple_add():
    assert mypackage.add(1, 2) == 3
    assert mypackage.add(1, 1) == 2
    assert mypackage.add(105, 321) == 426


def test_add_with_exception():
        with pytest.raises(ValueError):
            assert mypackage.add_with_exception(-5, 5)
