import pytest
#
#
#执行测试用例之前，先执行login方法
def  test_case1(login):
    print(f"case1 login = {login}")

def test_case2():
    print("case2")

def test_case3():
    print("case3")