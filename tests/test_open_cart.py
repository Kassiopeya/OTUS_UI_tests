import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_objects.pages import MainPage, ItemCard, LoginPage, RegistrationPage

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
browser1_ = webdriver.Chrome(options)
opencart_url = "https://127.0.0.1/"
time_sleep_value = 1

main_page = MainPage(browser1_)
item_card = ItemCard(browser1_)
login_page = LoginPage(browser1_)
registration_page = RegistrationPage(browser1_)
random_number = random.randint(100, 900)

def test_header_appeared():
    browser1_.get(opencart_url)
    assert "Your Store" in browser1_.title, "Название 'Your Store' не найдено"

def test_item_card_clickable():
    browser1_.get(opencart_url)
    main_page.click_mac_book_item_card(browser1_)
    time.sleep(time_sleep_value)
    assert "MacBook" in browser1_.title, "Название 'MacBook' не найдено"

def test_add_to_cart():
    browser1_.get(opencart_url)
    main_page.click_mac_book_item_card(browser1_)
    item_card.click_add_to_cart(browser1_)
    time.sleep(time_sleep_value)
    assert main_page.check_sum_changed(browser1_)=="1 item(s) - $602.00"

def test_wishlist_button_unauth():
    browser1_.get(opencart_url)
    main_page.click_wishlist_button(browser1_)
    assert login_page.account_login_block_is_displayed(browser1_) == True

def test_register_form_displayed():
    browser1_.get(opencart_url)
    main_page.click_wishlist_button(browser1_)
    main_page.click_new_customer_continue(browser1_)
    assert  registration_page.account_register_block_is_displayed(browser1_)==True

def test_registration_happy_path():
    browser1_.get(opencart_url)
    main_page.click_wishlist_button(browser1_)
    main_page.click_new_customer_continue(browser1_)
    registration_page.fill_in_name(browser1_, f"Victoria{random_number}")
    registration_page.fill_in_last_name(browser1_, f"Ivanova{random_number}")
    registration_page.fill_in_email(browser1_, f"test@test{random_number}.ru")
    registration_page.fill_in_password(browser1_, f"123{random_number}")
    registration_page.click_switch_privacy_policy(browser1_)
    registration_page.click_submit(browser1_)
    assert registration_page.success_registration_text_is_displayed(browser1_) == True

def test_negative_registration_empty_email():
    browser1_.get(opencart_url)
    main_page.click_wishlist_button(browser1_)
    main_page.click_new_customer_continue(browser1_)
    registration_page.fill_in_name(browser1_, f"Victoria{random_number}")
    registration_page.fill_in_last_name(browser1_, f"Ivanova{random_number}")
    registration_page.fill_in_password(browser1_, f"123{random_number}")
    registration_page.click_switch_privacy_policy(browser1_)
    registration_page.click_submit(browser1_)
    assert registration_page.check_email_error(browser1_) == True

def test_negative_registration_empty_name():
    browser1_.get(opencart_url)
    main_page.click_wishlist_button(browser1_)
    main_page.click_new_customer_continue(browser1_)
    registration_page.fill_in_last_name(browser1_, f"Ivanova{random_number}")
    registration_page.fill_in_email(browser1_, f"test@test{random_number}.ru")
    registration_page.fill_in_password(browser1_, f"123{random_number}")
    registration_page.click_switch_privacy_policy(browser1_)
    registration_page.click_submit(browser1_)
    assert registration_page.check_firstname_error(browser1_) == True


def test_negative_registration_empty_last_name():
    browser1_.get(opencart_url)
    main_page.click_wishlist_button(browser1_)
    main_page.click_new_customer_continue(browser1_)
    registration_page.fill_in_name(browser1_, f"Victoria{random_number}")
    registration_page.fill_in_email(browser1_, f"test@test{random_number}.ru")
    registration_page.fill_in_password(browser1_, f"123{random_number}")
    registration_page.click_switch_privacy_policy(browser1_)
    registration_page.click_submit(browser1_)
    assert registration_page.check_lastname_error(browser1_) == True

def test_negative_registration_empty_password():
    browser1_.get(opencart_url)
    main_page.click_wishlist_button(browser1_)
    main_page.click_new_customer_continue(browser1_)
    registration_page.fill_in_name(browser1_, f"Victoria{random_number}")
    registration_page.fill_in_last_name(browser1_, f"Ivanova{random_number}")
    registration_page.fill_in_email(browser1_, f"test@test{random_number}.ru")
    registration_page.click_switch_privacy_policy(browser1_)
    registration_page.click_submit(browser1_)
    assert registration_page.check_password_error(browser1_) == True

def test_checkout_button_unauth():
    # тест падает - в опенкарте баг - жмешь чекаут - попадаешь в корзину - пример для проверки скриншота
    browser1_.get(opencart_url)
    time.sleep(time_sleep_value)
    main_page.click_checkout_button(browser1_)
    time.sleep(time_sleep_value)
    checkout_register_element = browser1_.find_element(By.ID, "checkout-register")
    assert checkout_register_element.is_displayed()