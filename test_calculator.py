from operator import add, sub, mul

def test_addition():
    assert add(2, 3) == 5

def test_subtraction():
    assert sub(5, 3) == 2

def test_multiplication():
    assert mul(3, 3) == 9

def test_invalid_operation():
    try:
        add("invalid", 3)
    except TypeError:
        assert True
