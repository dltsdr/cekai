# 测试文件

import sys, pytest

print(sys.path.append('..'))

from pythoncode.calc import Calculator


def setup_module():
	print("模块级别setup")

def teardown_module():
	print("函数级别teardown")
#函数级别
def setup_function():
	print("函数级别setup")

def teardown_function():
	print("函数级别teardown")


class TestCalc():
	def setup_class(self):
		self.cal = Calculator
		print("类级别setup")

	def teardown_class(self):
		print("类级别teardowns")

	def setup(self):
		print("setup")

	def teardown(self):
		print("teardown")

	@pytest.mark.add
	@pytest.mark.parametrize('a,b,result',[(1,1,2),(2,2,4)])
	def test_add(self, a, b, result):
		#cal = Calculator()
		assert result == self.cal.add(a, b)


	@pytest.mark.add
	def test_add1(self):
		#cal = Calculator()
		assert 3 == self.cal.add(1, 2)


	@pytest.mark.div
	def test_div(self):
		#cal = Calculator()
		assert 1 == self.cal.div(1, 1)