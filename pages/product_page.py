from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*MainPageLocators.ADD_KORZ)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def name_tov(self):
        tovar = self.browser.find_element(*MainPageLocators.NAME_TOVAR).text
        assert tovar == "Coders at Work", "no kniga"
    def cena_tov(self):
        cena = self.browser.find_element(*MainPageLocators.CENA_TOVAR).text
        assert cena == "£19.99", "no cena"



 #   def should_be_name_tov(self):
 #       assert self.is_element_present(*MainPageLocators.NAME_TOVAR.text == "Coders at Work"), "no kniga"
 #   def should_be_cena_tov(self):
 #       assert self.is_element_present(*MainPageLocators.PRICE_TOVAR.text == "£19.99"), "no cena"

#.alert.alert-safe.alert-noicon.alert-info.fade.in strong

#.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) strong