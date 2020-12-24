import pytest
from pythoncoad.calculator import Calculator
class TestCalc:
    def setup_method(self):
        print("\n每个用例执行前打印")
    def teardown_method(self):
        print("\n每个用例执行后打印")

    def setup_class(self):
            self.calc = Calculator()

    @pytest.mark.parametrize("a,b,expect",[(3,5,8),(-1,-2,-3),(10000,10000,20000)])
    def test_add(self,a,b,expect):
        print("正在执行test_add")
        result=self.calc.add(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",[(8,3,5),(3,2,1),(10000,10000,0)])
    def test_sub(self,a,b,expect):
        print("正在执行test_sub")
        result = self.calc.sub(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",[(2,2,4),(-3,-4,12),(10,15,150)])
    def test_mul(self,a,b,expect):
        print("正在执行test_mul")
        result = self.calc.mul(a,b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",[(8,8,1),(25,5,5),(30,5,6)])
    def test_div(self,a,b,expect):
        print("正在执行test_div")
        result = self.calc.div(a,b)
        assert result == expect



