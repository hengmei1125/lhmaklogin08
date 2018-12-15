from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self, driver):
        self.driver = driver

    # 封装查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll) \
            .until(lambda x: x.find_element(*loc))

    # 封装点击
    def baes_click(self, loc):
        self.base_find_element(loc).click()

    # 封装输入
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)
