import yaml
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


#取yml文件数据
with open("datas/calc.yml") as f:
	datas = yaml.safe_load(f)
	myids = datas.keys()
	mydatas = datas.values()
	print(myids,mydatas)

def get_steps():
	with open("steps/add.yml") as f:
		steps = yaml.safe_load(f)
	return steps

cal = Calculator()

def steps(a,b,result):
	steps1 = get_steps()
	for step in steps1:
		if 'add' == step:
			assert result == cal.add(a,b)
		elif 'add1' ==step:
			assert result == cal.add1(a, b)
		elif 'add2' == step:
			assert result == cal.add2(a, b)





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




	#@pytest.mark.add
	@pytest.mark.parametrize('a, b, result',mydatas,ids=myids)
	def test_add(self, a, b, result):
		steps(a,b,result)

	def test_add1(self):
		assert 3 == self.cal.add(1, 2)

	@pytest.mark.div
	def test_div(self):
		assert 1 == self.cal.div(1, 1)

