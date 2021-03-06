# 创建Calculator类的实例
import pytest
import yaml

from pytestCode.calculator import Calculator

cal = Calculator()


# with open("./datas/datas.yaml") as f:
#     datas = yaml.safe_load(f)
#     @pytest.mark.parametrize("a,b,result", datas)

class TestCal:

    # 测试乘法
    @pytest.mark.dependency(name=["test_mul"])  # 创建依赖：test_mul
    @pytest.mark.run(order=3)
    def test_mul1(self):
        assert 1 == cal.mul(1, 1)

    # 测试除法
    @pytest.mark.dependency(depends=["test_mul"])  # 除法依赖乘法
    @pytest.mark.run(order=4)
    def test_div1(self):
        assert 1 == cal.div(1, 1)

    # 测试加法
    @pytest.mark.dependency(name=["test_add"])  # 创建依赖：test_add
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,result", yaml.safe_load(open("./datas/datas.yaml")), ids=["整数", "浮点数", "负数"])
    def test_add1(self, a, b, result):
        assert result == cal.add(a, b)

    # 测试减法
    @pytest.mark.dependency(depends=["test_add"])  # 减法依赖加法
    @pytest.mark.run(order=2)
    def test_sub1(self):
        assert 0 == cal.sub(1, 1)
