import sys
sys.path.append("..")
from po.browser_engine import BrowserEngine
from po.baidu_homepage import BaiduHomePage
import pytest
import allure


@allure.feature("百度搜索")
class TestBaiduSearch:
    @classmethod
    def setup_class(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.get_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.story("测试百度搜索，验证标题是否正确")
    @pytest.mark.parametrize("search_char, verify_char", [('龙珠', '龙珠_百度搜索'), ('火影忍者', '火影_百度搜索')])
    def test_baidu_search(self, search_char, verify_char):
        baidu_homepage = BaiduHomePage(self.driver)
        baidu_homepage.open_homepage()
        baidu_homepage.search(search_char)
        baidu_homepage.verify(verify_char)


if __name__ == '__main__':
    pytest.main()
