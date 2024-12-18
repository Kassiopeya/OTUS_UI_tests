from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class MainPage:
    def __init__(self, browser):
        self.browser = browser

    def wait_mac_book_item_card(self, browser):
        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[1]/a")))

    def click_mac_book_item_card(self, browser):
        item_card_clickable = browser.find_element(By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[1]/a")
        item_card_clickable.click()

    def click_add_to_cart(self, browser):
        add_to_cart_button = browser.find_element(By.ID, "button-cart")
        add_to_cart_button.click()

    def check_sum_changed(self, browser):
        sum_text = browser.find_element(By.XPATH, "//*[@id=\"header-cart\"]/div/button")
        return sum_text.text
