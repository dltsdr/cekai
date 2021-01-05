from typing import List

import pytest
#
# #conftest公用模块，在执行同级目录用例时，首先查看此目录否有可调用模块
#
# #scope可控制fixture的作用域   scope='session'整个项目执行一次，scope='module'每个项目执行一次,autouse=True自动每个测试用例都调用
# #@pytest.fixture(autouse=True,params=['user1','user2','user3'])
# @pytest.fixture(params=['user1','user2','user3'])
# #此处要接收request
# 如果方法中传入login，测试用例执行前先执行login
import yaml
from requests import Session


@pytest.fixture(params=['user1','user2','user3'])
def login(request):#需要用request调用params
    print("登录方法")
    print(request.param)
    #使用request.param获取参数
    #yield激活fixture teard的方法
    yield ['username','password']
    print('teardown')

def pytest_collection_modifyitems(
        session: "Session",config:"Config",items: List["Item"]
) -> None:
    print(items)
    print(len(items))
    #倒序执行items里面的测试用例
    items.reverse()
    #编码格式转换,item是用例名称
    for item in items:
        item.name=item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid=item.nodeid.encode('utf-8').decode('unicode-escape')
    if 'add' in item.nodeid:
        item.add_marker(pytest.mark.add)

    if 'div' in item.nodeid:
        item.add_marker(pytest.mark.div)


#命令行去添加一个参数
def pytest_addoption(parser):
    mygroup = parser.getgroup("dwg")     #group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",    #注册一个命令行选项
                      default='test',#默认入参
                      dest='env',
                      help='set your run env'
                      )
#可用于分环境进行操作。处理命令行传来的参数，设置成fixture
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv =  request.config.getoption("--env", default='test')
    if myenv == 'test':
        datapath = 'datas/test/data.yml'

    if myenv == 'dev':
        datapath = 'datas/dev/data.yml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)
    return myenv, datas

#动态生成测试用例
def pytest_generate_tests(metafunc:"Metafunc") -> None:
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.datas,
                             ids=metafunc.module.myids,
                             scope='function')