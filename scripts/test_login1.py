import sys
import os
sys.path.append(os.getcwd())

import pytest
from page.page_login import PageLogin
from base.get_driver import get_driver


class TestLogin():

    def setup_class(self):
        self.login = PageLogin(get_driver())

    def teadown_class(self):
        self.login.driver.quit()

    @pytest.mark.parametrize("username,password", [("1850000000","123456")])
    def test_login(self,username,password):
        self.login.page_login_input_username(username)
        self.login.page_login_input_password(password)
        self.login.page_login_click()


