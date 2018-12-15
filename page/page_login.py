import page
from base.base import Base


class PageLogin(Base):

    def page_login_input_username(self,username ):
        self.base_input(page.loc_input_username, username)

    def page_login_input_password(self,password):
        self.base_input(page.loc_input_password,password)

    def page_login_click(self):
        self.baes_click(page.loc_click)
