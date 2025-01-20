import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.epic("DW")
@allure.feature("Авторизация")
class Authlogin:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(5)
        self._driver.execute_script("window.scrollBy(0, 400)")


    @allure.step("Открыть страницу.")
    def open_pages(self):
        """
        Эта функция открывает страницу.
        :return: Страница открыта.
        """
        self._driver.get("https://www.kinopoisk.ru/")
        self._driver.maximize_window()


    @allure.step("Нажать на кнопку 'Войти'.")
    def login_button(self):
        """
        Эта функция находит кнопку 'Войти'
        :return: Кнопка отработала.
        """
        self._driver.find_element(By.CSS_SELECTOR, "button.styles_loginButton__LWZQp").click()


    @allure.step("Ввести данные в поле 'Логин'")
    def user_name(self):
        """
        Эта функция принимает значение логина.
        :return: Логин принят.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#passp-field-login").send_keys("ahalkatsivladimir", Keys.ENTER)


    @allure.step("Ввести данные в поле 'Пароль'")
    def password(self):
        """
        Эта функция принимает значение пароля.
        :return: Пароль принят.
        """
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id = passp-field-passwd]'))
        )
        self._driver.find_element(By.CSS_SELECTOR, "[id = passp-field-passwd]").send_keys("Abf4122$", Keys.ENTER)


    @allure.step("Закрыть браузер")
    def close_driver(self):
        """
        Эта функция выхода.
        :return:quit
        """
        self._driver.quit()
