# 创建Calculator类的实例
import pytest
import yaml

from pytestCode.calculator import Calculator

cal = Calculator()


# with open("./datas/datas.yaml") as f:
#     datas = yaml.safe_load(f)
#     @pytest.mark.parametrize("a,b,result", datas)

class TestCal:

    # 测试除法
    def test_div1(self):
        assert 1 == cal.div(1, 1)

    # 测试乘法
    def test_mul1(self):
        assert 1 == cal.mul(1, 1)

    # 测试减法
    def test_sub1(self):
        assert 0 == cal.sub(1, 1)

    # 测试加法
    @pytest.mark.parametrize("a,b,result", yaml.safe_load(open("./datas/datas.yaml")))
    def test_add1(self, a, b, result):
        assert result == cal.add(a, b)
