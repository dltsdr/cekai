import pytest,yaml
from pythoncode.calc import Calculator

#读取yml文件数据
with open("./c.yml") as f:
    datas = yaml.safe_load(f)

print(datas["addyml"])

class Testcal:
    def setup(self):
        self.cal = Calculator()
        print("setup")

    def teardown(self):
        print("teardown")


    #加法
    @pytest.mark.parametrize("a, b, result",datas["addyml"])
    def test_add(self, a, b, result):
        assert result == self.cal.add(a,b)

    #减法
    @pytest.mark.parametrize("a, b, result",datas["subyml"])
    def test_sub(self, a, b, result):
        assert result == self.cal.sub(a,b)

    #c乘法
    @pytest.mark.parametrize("a, b, result",datas["multml"])
    def test_mult(self, a, b, result):
        assert result == self.cal.mult(a,b)

    #除法
    @pytest.mark.parametrize("a, b, result",datas["divyml"])
    def test_div(self, a, b, result):
        assert result == self.cal.div(a,b)
