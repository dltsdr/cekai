#实现计算机
import sys,pytest
sys.path.append('..')
from pythoncode.calc import Calculator

@pytest.mark.add
def test_add():
	cal = Calculator()
	assert 2 == cal.add(1,1)

def test_add1():
	cal = Calculator()
	assert 3 == cal.add(1,2)

@pytest.mark.div
def test_div():
	cal = Calculator()
	assert 3 == cal.div(1,1)