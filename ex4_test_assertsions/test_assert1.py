
# content of test_assert1.py
def f():
    return 3


def test_function():
    assert f() == 4


def test_function2():
    a = 3
    assert a % 2 == 0, "value was odd, should be even"
