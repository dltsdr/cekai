import pytest
#
# #conftest公用模块，在执行同级目录用例时，首先查看此目录否有可调用模块
#
# #scope可控制fixture的作用域   scope='session'整个项目执行一次，scope='module'每个项目执行一次,autouse=True自动每个测试用例都调用
# #@pytest.fixture(autouse=True,params=['user1','user2','user3'])
# @pytest.fixture(params=['user1','user2','user3'])
# #此处要接收request
# 如果方法中传入login，测试用例执行前先执行login
@pytest.fixture(params=['user1','user2','user3'])
def login(request):#需要用request调用params
    print("登录方法")
    print(request.param)
    #使用request.param获取参数
    #yield激活fixture teard的方法
    yield ['username','password']
    print('teardown')
