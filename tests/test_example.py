import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(options)
opencart_url = "https://127.0.0.1/"


def test_header_appeared():
    browser.get(opencart_url)
    assert "Your Store" in browser.title, "Название 'Your Store' не найдено"

def test_item_card_clickable():
    browser.get(opencart_url)
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[1]/a")))
    item_card_clickable = browser.find_element(By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[1]/a")
    item_card_clickable.click()
    time.sleep(2)
    assert "MacBook" in browser.title, "Название 'MacBook' не найдено"

def test_add_to_cart():
    browser.get(opencart_url)
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[2]/form/div/button[1]")))
    add_to_cart_button = browser.find_element(By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[2]/form/div/button[1]")
    add_to_cart_button.click()
    time.sleep(5)
    browser.get("https://demo.opencart.com/en-gb?route=checkout/cart")
    item_in_cart = browser.find_element(By.XPATH,"//*[@id=\"shopping-cart\"]/div/table/tbody/tr/td[2]/a")
    assert item_in_cart.is_displayed()

@pytest.mark.parametrize( "number", [1, 2, 3, 8])
def test_dropdown_shown(number):
    browser.get(opencart_url)
    navbar_button = browser.find_element(By.XPATH, f"//*[@id=\"narbar-menu\"]/ul/li[{number}]/a/ya-tr-span")
    dropdown_menu = browser.find_element(By.XPATH, f"//*[@id=\"narbar-menu\"]/ul/li[{number}]/div")
    navbar_button.click()
    assert dropdown_menu.is_displayed()



