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


class Test_Calc:
    def setup(self):
        self.cal = Calculator
        print("类级别setup")
    def teardown(self):
        print("类级别teardowns")



	@pytest.mark.add
	def test_add(self):
		#cal = Calculator()
		assert 2 == self.cal.add(1, 1)


	@pytest.mark.add
	def test_add1(self):
		#cal = Calculator()
		assert 3 == self.cal.add(1, 2)


	@pytest.mark.div
	def test_div(self):
		#cal = Calculator()
		assert 1 == self.cal.div(1, 1)