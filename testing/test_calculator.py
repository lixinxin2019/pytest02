# 创建Calculator类的实例
import pytest
import yaml

from pytestCode.calculator import Calculator

cal = Calculator()

with open("./datas/datas.yaml") as f:
    datas = yaml.safe_load(f)


@pytest.mark.parametrize("a,b,result", datas)
# @pytest.mark.parametrize("a,b,result", yaml.safe_load(open("./datas/datas.yaml")))
class TestCal:
    # 测试加法
    def test_add1(self, a, b, result):
        assert result == cal.add(a, b)

    # def test_add2(self):
    #     assert 2 == cal.add(2, 0)
    #
    # def test_add3(self):
    #     assert 3 == cal.add(1, 2)
    #
    # def test_add4(self):
    #     assert -2 == cal.add(-1, -1)
    #
    # def test_add5(self):
    #     assert -2 == cal.add(-3, 1)
    #
    # 测试减法
    # def test_sub1(self):
    #     assert 0 == cal.sub(1, 1)

    #
    # def test_sub2(self):
    #     assert 2 == cal.sub(3, 1)
    #
    # def test_sub3(self):
    #     assert -1 == cal.sub(1, 2)
    #
    # def test_sub4(self):
    #     assert 1 == cal.sub(-1, -2)
    #
    # def test_sub5(self):
    #     assert 4 == cal.sub(4, 0)

    # 测试乘法
    # def test_mul1(self):
    #     assert 1 == cal.mul(1, 1)

    # def test_mul2(self):
    #     assert 0 == cal.mul(0, 1)
    #
    # def test_mul3(self):
    #     assert 0 == cal.mul(1, 0)
    #
    # def test_mul4(self):
    #     assert 0 == cal.mul(0, 0)
    #
    # def test_mul5(self):
    #     assert 1 == cal.mul(-1, -1)

    # 测试除法
    # def test_div1(self):
    #     assert 1 == cal.div(1, 1)

    # def test_div2(self):
    #     assert 0 == cal.div(0, 1)
    #
    # # 这是一条错误的用例
    # def test_div3(self):
    #     assert 0 == cal.div(1, 0)
    #
    # # 这是一条错误的用例
    # def test_div4(self):
    #     assert 0 == cal.div(0, 0)
    #
    # def test_div5(self):
    #     assert 1 == cal.div(-1, -1)
    #
    # def test_div6(self):
    #     assert -1 == cal.div(1, -1)
    #
    # def test_div7(self):
    #     assert -1 == cal.div(-2, 2)
