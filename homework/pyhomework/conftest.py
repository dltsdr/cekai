import pytest
@pytest.fixture(scope='module')
def login():
    print("开始计算")
    yield
    print('结束计算')