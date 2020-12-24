import pytest,sys
from func.Calc import Calculator

@pytest.mark.add
def test_add():
    cal = Calculator()
    print("判断成功")
    assert 2 == cal.add(1,1)