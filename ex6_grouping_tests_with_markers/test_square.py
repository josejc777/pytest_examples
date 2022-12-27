import math
# import the module
import pytest

@pytest.mark.square
def test_sqrt():
    num=25
    assert math.sqrt(num) == 5

@pytest.mark.square
def testsquare():
    num=7
    assert 7*7 == 40

@pytest.mark.webtest
def test_equality():
    assert 10 == 11

