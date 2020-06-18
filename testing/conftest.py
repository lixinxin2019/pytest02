from typing import List

import pytest


@pytest.fixture(scope="session", autouse=True)
def login():
    print("开始计算")
    yield "yield"
    print("计算结束")
#
# def pytest_collection_modifyitems(session:"Session", config:"Config", items:List["items"]) -> None:
#     pass


    """ called after collection has been performed, may filter or re-order
    the items in-place.

    :param _pytest.main.Session session: the pytest session object
    :param _pytest.config.Config config: pytest config object
    :param List[_pytest.nodes.Item] items: list of item objects
    """



