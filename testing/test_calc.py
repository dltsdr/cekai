#实现计算机
import sys,pytest
sys.path.append('..')
from pythoncode.calc import Calculator

#模块级别
def setup_module():
	print("模块级别setup")

def teardown_module():
	print("模块级别teardown")

#函数级别  类外面的使用def 定义叫做函数
#         在类里面的使用def 定义的叫方法
def setup_function():
	print("函数级别setup")

def teardown_function():
	print("函数级别teardown")


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
	assert 1 == cal.div(1,1)


class TestCalc:
	def setup_class(self):
		print("类级别setup")

	def teardown_class(self):
		print("类级别teardown")


	def setup(self):
		self.cal = Calculator()
		print("setup")

	def teardown(self):
		print("teardown")




	@pytest.mark.add
	@pytest.mark.parametrize('a, b, result',[
		(1,1,2),
		(2,2,4),
		(0.1,0.1,0.2),
		(-1,-1,-2)],ids=['int','int','float','fushu'])
	def test_add(self, a, b, result):
		assert result == self.cal .add(a, b)

	def test_add1(self):
		assert 3 == self.cal .add(1, 2)

	@pytest.mark.div
	def test_div(self):
		assert 1 == self.cal .div(1, 1)