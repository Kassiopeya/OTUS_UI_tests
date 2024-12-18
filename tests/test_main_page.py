import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.MainPage import MainPage

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
browser1_ = webdriver.Chrome(options)
opencart_url = "https://127.0.0.1/"

main_page = MainPage(browser1_)

def test_header_appeared():
    browser1_.get(opencart_url)
    assert "Your Store" in browser1_.title, "Название 'Your Store' не найдено"

def test_item_card_clickable():
    browser1_.get(opencart_url)
    main_page.wait_mac_book_item_card(browser1_)
    main_page.click_mac_book_item_card(browser1_)
    time.sleep(2)
    assert "MacBook" in browser1_.title, "Название 'MacBook' не найдено"

def test_add_to_cart():
    browser1_.get(opencart_url)
    main_page.wait_mac_book_item_card(browser1_)
    main_page.click_mac_book_item_card(browser1_)
    time.sleep(2)
    main_page.click_add_to_cart(browser1_)
    time.sleep(2)
    assert main_page.check_sum_changed(browser1_)=="1 item(s) - $602.00"

@pytest.mark.parametrize( "number", [1, 2, 3, 8])
def test_dropdown_shown(number):
    browser1_.get(opencart_url)
    navbar_button = browser1_.find_element(By.XPATH, f"//*[@id=\"narbar-menu\"]/ul/li[{number}]/a/ya-tr-span")
    dropdown_menu = browser1_.find_element(By.XPATH, f"//*[@id=\"narbar-menu\"]/ul/li[{number}]/div")
    navbar_button.click()
    assert dropdown_menu.is_displayed()