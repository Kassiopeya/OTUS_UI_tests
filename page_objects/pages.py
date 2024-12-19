import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def wait_until_displayed_by_id(browser, locator):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, f"{locator}")))

def wait_until_displayed_by_xpath(browser, locator):
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, f"{locator}")))

class MainPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Кликаем по первой карточке товара на странице")
    def click_mac_book_item_card(self, browser):
        my_locator = "//*[@id=\"content\"]/div[2]/div[1]/div/div[1]/a"
        wait_until_displayed_by_xpath(browser, my_locator)
        item_card_clickable = browser.find_element(By.XPATH, my_locator)
        item_card_clickable.click()

    @allure.step("Проверяем, изменилась ли сумма покупок")
    def check_sum_changed(self, browser):
        sum_text = browser.find_element(By.XPATH, "//*[@id=\"header-cart\"]/div/button")
        return sum_text.text

# тут бага - тыкаешь кнопку checout - попадаешь на страницу Shopping Cart
    @allure.step("Кликаем кнопку Checkout")
    def click_checkout_button(self, browser):
        checkout_button = browser.find_element(By.CSS_SELECTOR, "#top>div>div.nav.float-end>ul>li:nth-child(5)>a>span")
        checkout_button.click()

    @allure.step("Проверяем, есть ли надпись Checkout")
    def check_content_text(self, browser):
        browser.find_element(By.XPATH, "//*[@id=\"content\"]/h1[contains(text(), 'Checkout')]")

    @allure.step("Кликаем кнопку Wishlist")
    def click_wishlist_button(self, browser):
        my_locator = "//*[@id=\"wishlist-total\"]/span"
        checkout_button = browser.find_element(By.XPATH, my_locator)
        wait_until_displayed_by_xpath(browser, my_locator)
        checkout_button.click()

    @allure.step("Кликаем кнопку Continue")
    def click_new_customer_continue(self, browser):
        my_locator = "//*[@id=\"content\"]/div/div[1]/div/div/a"
        wait_until_displayed_by_xpath(browser, my_locator)
        continue_button = browser.find_element(By.XPATH, my_locator)
        continue_button.click()

class ItemCard:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Добавляем товар в корзину")
    def click_add_to_cart(self, browser):
        my_locator = "button-cart"
        wait_until_displayed_by_id(browser, my_locator)
        add_to_cart_button = browser.find_element(By.ID, my_locator)
        add_to_cart_button.click()

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Проверяем, что отобразился блок входа и регистрации")
    def account_login_block_is_displayed(self, browser):
        my_locator = "account-login"
        wait_until_displayed_by_id(browser, my_locator)
        account_login_block = browser.find_element(By.ID, my_locator)
        return account_login_block.is_displayed()

class RegistrationPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Проверяем, что отобразилась форма регистрации")
    def account_register_block_is_displayed(self, browser):
        my_locator = "account-register"
        wait_until_displayed_by_id(browser, my_locator)
        account_register_block = browser.find_element(By.ID, my_locator)
        return account_register_block.is_displayed()

    @allure.step("Вводим имя")
    def fill_in_name(self, browser, name):
        my_locator = "input-firstname"
        input_first_name = browser.find_element(By.ID, my_locator)
        input_first_name.send_keys(name)

    @allure.step("Вводим фамилию")
    def fill_in_last_name(self, browser, lastname):
        my_locator = "input-lastname"
        input_first_name = browser.find_element(By.ID, my_locator)
        input_first_name.send_keys(lastname)

    @allure.step("Вводим адрес почты")
    def fill_in_email(self, browser, email):
        my_locator = "input-email"
        input_first_name = browser.find_element(By.ID, my_locator)
        input_first_name.send_keys(email)

    @allure.step("Вводим пароль")
    def fill_in_password(self, browser, password):
        my_locator = "input-password"
        input_first_name = browser.find_element(By.ID, my_locator)
        input_first_name.send_keys(password)

    @allure.step("Включаем свитч - согласиться с политикой приватности")
    def click_switch_privacy_policy(self, browser):
        my_locator = "//*[@id=\"form-register\"]/div/div/input"
        switch_privacy_policy = browser.find_element(By.XPATH, my_locator)
        switch_privacy_policy.click()

    @allure.step("Отправляем форму резистрации")
    def click_submit(self, browser):
        submit_button = browser.find_element(By.XPATH, "//*[@id=\"form-register\"]/div/button")
        submit_button.click()

    @allure.step("Проверяем, что отобразился текст об успешной регистрации")
    def success_registration_text_is_displayed(self, browser):
        my_locator = "common-success"
        wait_until_displayed_by_id(browser, my_locator)
        success_registration_text = browser.find_element(By.ID, my_locator)
        return success_registration_text.is_displayed()

    @allure.step("Проверяем, наличие ошибки валидации поля email")
    def check_email_error(self, browser):
        my_locator = "error-email"
        wait_until_displayed_by_id(browser, my_locator)
        error_text = browser.find_element(By.ID, my_locator)
        return error_text.is_displayed()

    @allure.step("Проверяем, наличие ошибки валидации поля Name")
    def check_firstname_error(self, browser):
        my_locator = "error-firstname"
        wait_until_displayed_by_id(browser, my_locator)
        error_text = browser.find_element(By.ID, my_locator)
        return error_text.is_displayed()

    @allure.step("Проверяем, наличие ошибки валидации поля Last Name")
    def check_lastname_error(self, browser):
        my_locator = "error-lastname"
        wait_until_displayed_by_id(browser, my_locator)
        error_text = browser.find_element(By.ID, my_locator)
        return error_text.is_displayed()

    @allure.step("Проверяем, наличие ошибки валидации поля password")
    def check_password_error(self, browser):
        my_locator = "error-password"
        wait_until_displayed_by_id(browser, my_locator)
        error_text = browser.find_element(By.ID, my_locator)
        return error_text.is_displayed()