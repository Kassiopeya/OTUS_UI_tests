import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

def test_header_appeared():
    browser.get("https://demo.opencart.com/")
    assert "Your Store" in browser.title, "Название 'Your Store' не найдено"

def test_item_card_clickable():
    browser.get("https://demo.opencart.com/")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[1]/a")))
    item_card_clickable = browser.find_element(By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[1]/a")
    item_card_clickable.click()
    time.sleep(2)
    assert "MacBook" in browser.title, "Название 'MacBook' не найдено"

def test_add_to_cart():
    browser.get("https://demo.opencart.com/")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[2]/form/div/button[1]")))
    add_to_cart_button = browser.find_element(By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[2]/form/div/button[1]")
    add_to_cart_button.click()
    time.sleep(5)
    browser.get("https://demo.opencart.com/en-gb?route=checkout/cart")
    item_in_cart = browser.find_element("//*[@id=\"shopping-cart\"]/div/table/tbody/tr/td[2]/")
    assert item_in_cart.is_displayed()


