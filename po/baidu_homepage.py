import time
from po.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class BaiduHomePage(BasePage):
    # 个人感觉不太喜欢把页面元素，和操作脚本再单独分开，因为读起来累。
    search_box_loc = (By.ID, "kw")
    search_button_loc = (By.ID, "su")

    @allure.step('打开百度首页')
    def open_homepage(self):
        self.driver.get('https://www.baidu.com/')

    @allure.step('输入内容进行搜索')
    def search(self, search_char):
        search_box = self.find_element(*self.search_box_loc)
        search_box.send_keys(search_char)
        search_button = self.find_element(*self.search_button_loc)
        search_button.click()
        time.sleep(3)

    @allure.step('验证标题是否正确')
    def verify(self, verify_char):
        title = self.driver.title
        print(title)
        assert verify_char == title


