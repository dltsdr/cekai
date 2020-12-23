import pytest,sys
import calc.Calculator

def test_add():
    a = Calculator()
    assert 2 == a.add(1,1)