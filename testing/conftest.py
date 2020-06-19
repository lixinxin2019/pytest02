from typing import List

import pytest
import yaml


@pytest.fixture(scope="session")
def cmdoption(request):
    # return request.config.getoption("--env", default='test')
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        print("获取test数据")
        with open("datas/testdatas/testdatas.yaml") as f:
            datas = yaml.safe_load(f)
            print(datas)
    elif myenv == 'dev':
        print("获取dev数据")
        with open("datas/devdatas/devdatas.yaml") as f:
            datas = yaml.safe_load(f)
            print(datas)

    elif myenv == 'st':
        print("获取st数据")
        with open("datas/stdatas/stdatas.yaml") as f:
            datas = yaml.safe_load(f)
            print(datas)




# @pytest.fixture(scope="session", autouse=True)
# def login():
#     print("开始计算")
#     yield "yield"
#     print("计算结束")


# 自定义的hook函数，pytest_collection_modifyitems，将收集上来的测试用例进行改写：
# 控制执行顺序，自动添加标签，解决测试用例的编码问题
# items是所有测试用例集合，item代表每个测试用例
def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    # 将测试用例顺序反转后执行
    items.reverse()
    # for item in items:
    #     item.name = item.name.encode('utf-8').decode('unicode-escape')
    #     item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    #
    #       if 'add' in item.nodeid:
    #         item.add_marker(pytest.mark.add)
    #       elif 'div' in item.nodeid:
    #         item.add_marker(pytest.mark.div)


def pytest_addoption(parser: "Parser") -> None:
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env')
