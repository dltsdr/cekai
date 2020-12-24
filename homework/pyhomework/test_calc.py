import pytest
from func.Calc import Calculator

class Testcal:
    def setup_class(self):
        self.cal = Calculator()


    @pytest.mark.add
    #加法运算
    def test_add(self,login):
        assert 2 == self.cal.add(1,1)


    @pytest.mark.sub
    #减法运算
    def test_sub(self,login):
        assert 0 == self.cal.sub(1,1)


    @pytest.mark.mult
    #乘法运算
    def test_mult(self,login):
        assert 1 == self.cal.mult(1,1)


    @pytest.mark.div
    #除法运算
    def test_div(self,login):
        assert 1 == self.cal.div(1,1)