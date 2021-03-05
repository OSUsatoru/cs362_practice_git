import pytest

import sys
sys.path.append('..')

from cs362_coverage.fibonacci import fibonacci_class


def test_fib1():
    assert fibonacci_class(10).fib() == 89

def test_fib2():
    assert fibonacci_class(-5).fib() == "Invalid input (sign error)"

def test_fib3():
    with pytest.raises(ValueError) as excinfo:
        fibonacci_class(1.2).fib()
    assert str(excinfo.value) == "Invalid input (type error)"

def test_fib4():
    with pytest.raises(ValueError) as excinfo:
        fibonacci_class("input string").fib()
    assert str(excinfo.value) == "Invalid input (type error)"


def test_fac1():
    assert fibonacci_class(10).fac() == 3628800

def test_fac2():
    assert fibonacci_class(-5).fac() == "Invalid input (sign error)"

def test_fac3():
    with pytest.raises(ValueError) as excinfo:
        fibonacci_class(1.2).fac()
    assert str(excinfo.value) == "Invalid input (type error)"

def test_fac4():
    with pytest.raises(ValueError) as excinfo:
        fibonacci_class("input string").fac()
    assert str(excinfo.value) == "Invalid input (type error)"
