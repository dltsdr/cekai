import pytest,yaml
from func.Calc import Calculator

#读取yml文件数据
with open("./c.yml") as f:
    datas = yaml.safe_load(f)
    #计算的数据类型
    myids = datas.keys()
    print(myids)
    #计算的数值
    mydatas = datas.values()
    print(mydatas)


class Testcal:
    def setup(self):
        self.cal = Calculator()
        print("setup")

    def teardown(self):
        print("teardown")


    #加法
    @pytest.mark.parametrize('a, b, result',mydatas,ids=myids)
    def test_add(self, a, b, result):
         assert result == self.cal.add(a,b)

    @pytest.mark.parametrize('a, b, result',mydatas,ids=myids)
    def test_add(self, a, b, result):
        assert result == self.cal.sub(a,b)

    @pytest.mark.parametrize('a, b, result',mydatas,ids=myids)
    def test_add(self, a, b, result):
        assert result == self.cal.mult(a,b)

    @pytest.mark.parametrize('a, b, result',mydatas,ids=myids)
    def test_add(self, a, b, result):
        assert result == self.cal.div(a,b)
