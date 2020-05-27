from .browser_engine import BrowserEngine
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # 需要二次封装的方法都写在BasePage中
    def __init__(self, selenium_driver):
        self.driver = selenium_driver
        # 上面的driver是当参数传入的,因为没有变量声明,所以driver的方法不能自动获取,会比较麻烦,所以在写当前page
        # 的操作方法时,可以把上面一句注释掉,下面一句打开,写完之后再恢复。
        # self.driver = BrowserEngine.get_driver()

    # *loc任意数量的位置参数（带单个星号参数）
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("%s 页面未能找到 %s 元素" % (self, loc))
