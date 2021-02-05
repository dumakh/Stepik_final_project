from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_KORZ = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    NAME_TOVAR = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) strong')
    CENA_TOVAR = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info.fade.in strong')


#class LoginPageLocators():