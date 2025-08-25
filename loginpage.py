from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Just store locators here
        self.username_input_locator = (By.ID, "user-name")
        self.password_input_locator = (By.ID, "password")
        self.login_button_locator = (By.ID, "login-button")
        self.burger_menu_button_locator = (By.ID, "react-burger-menu-btn")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input_locator).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input_locator).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button_locator).click()

    def open_burger_menu(self):
        self.driver.find_element(*self.burger_menu_button_locator).click()
