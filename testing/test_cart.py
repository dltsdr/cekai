import pytest
def test_cart1(login):
    print("购物车用例1")


def test_cart2(login):
    print("购物车用例2")

@pytest.fixture()
def fun():
    print("这是另一个fixture")

@pytest.fixture()
def fun1():
    print("这是另一个fixture1")

#参数化解和fixture使用
#情况一：传入值和数据
#情况二：传入一个fixture方法，将数据传入到fixture方法中
#fixture方法使用request参数来接手这组数据，在方法体里面使用
#request.param来使用这个数据

@pytest.mark.parametrize('login',[(1,2),(3,4)],indirect=True)#加indirect=True将参数传入conftest中的fixture
def test_cart3(login, fun,fun1):
    print("购物车用例3")
    print(login)