# в файле conftest прописываются фикстуры. Т.е. везде, где мы передадим параметр set_up, выполнится данная фикстура
import pytest

# передача в фикстуру урла специфично и не так универсально, как если передавать урл конкретно в авторизации под
# конкретные тесты, эта практика лучше, ниже просто пример, как также может быть

# фикстура - маркер, который дает более удобную читабельность результатов теста

@pytest.fixture
def set_up():
    print('Start test')  # до теста
    # driver = webdriver.Chrome(executable_path='C:\\resource\\chromedriver.exe')  # до теста
    # url = 'https://www.saucedemo.com'  # до теста
    # driver.get(url)  # до теста
    # driver.maximize_window()   # до теста
    yield  # сам тест
    print('Finish test')  # после теста
    # driver.quit() # после теста


"""фикстура, относящаяся сразу ко всему модулю (параметр scope). Т.е. будет выполнена в начале ГРУППЫ тестов и в 
конце ГРУППЫ тестов, в отличие от верхней фикстуры для КАЖДОГО теста"""

@pytest.fixture(scope="module")
def set_group():
    print('Enter system')
    yield
    print('Exit system')