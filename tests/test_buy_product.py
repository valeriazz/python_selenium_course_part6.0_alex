import time

import pytest
from selenium import webdriver
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.payment_page import Payment_page
from pages.finish_page import Finish_page
from selenium.webdriver.chrome.options import Options

# если хотим запустить только 1 тест из файла, выполнить python -m pytest -s -v -k test_buy_product_1
# @pytest.mark.run(order=3)  # задаём порядок выполнения



def test_buy_product_1(set_up, set_group):  # в файле с тестами метод обязательно должен начинаться с test!
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # options - для очищения консоли от
    # лишних сервисных сообщений при запуске теста
    driver = webdriver.Chrome(executable_path='C:\\resource\\chromedriver.exe', chrome_options=options)
    # print('Start Test1')

    login = Login_page(driver)
    login.authorization()

    main = Main_page(driver)
    main.select_1_product_1()

    cart = Cart_page(driver)
    cart.confirm_product()

    # client_info = Client_info_page(driver)
    # client_info.enter_client_info()
    #
    # payment = Payment_page(driver)
    # payment.finish_shopping()
    #
    # finish = Finish_page(driver)
    # finish.finish()

    # print('Finish Test1')
    # time.sleep(5)
    driver.quit()


# @pytest.mark.run(order=1)
def test_buy_product_2(set_up, set_group):  # в файле с тестами метод обязательно должен начинаться с test!
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # options - для очищения консоли от
    # лишних сервисных сообщений при запуске теста
    driver = webdriver.Chrome(executable_path='C:\\resource\\chromedriver.exe', chrome_options=options)
    # print('Start Test2')

    login = Login_page(driver)
    login.authorization()

    main = Main_page(driver)
    main.select_2_product_2()

    cart = Cart_page(driver)
    cart.confirm_product()

    # print('Finish Test2')
    # time.sleep(5)
    driver.quit()


# @pytest.mark.run(order=1)
def test_buy_product_3(set_up):  # в файле с тестами метод обязательно должен начинаться с test!
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # options - для очищения консоли от
    # лишних сервисных сообщений при запуске теста
    driver = webdriver.Chrome(executable_path='C:\\resource\\chromedriver.exe', chrome_options=options)
    # print('Start Test3')

    login = Login_page(driver)
    login.authorization()

    main = Main_page(driver)
    main.select_3_product_3()

    cart = Cart_page(driver)
    cart.confirm_product()

    # print('Finish Test3')
    # time.sleep(5)
    driver.quit()
