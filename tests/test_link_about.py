import time
from selenium import webdriver
from pages.login_page import Login_page
from pages.main_page import Main_page
from selenium.webdriver.chrome.options import Options

def test_link_about():  # в файле с тестами метод обязательно должен начинаться с test!
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # options - для очищения консоли от
    # лишних сервисных сообщений при запуске теста
    driver = webdriver.Chrome(executable_path='C:\\resource\\chromedriver.exe', chrome_options=options)
    print('Start Test')

    login = Login_page(driver)
    login.authorization()

    main = Main_page(driver)
    main.select_menu_about()

    print('Finish test')
    time.sleep(5)
    driver.quit()





