import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.epic("DW")
@allure.feature("Отработка кнопки - Билеты в кино")
class CinemaTicket:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(5)

    @allure.step("Открыть страницу.")
    def open_pages(self):
        """
        Эта функция открывает страницу.
        :return: Страница открыта.
        """
        self._driver.get("https://www.kinopoisk.ru/")
        self._driver.maximize_window()


    @allure.step("Нажать кнопку - Билеты в кино")
    def choice_ticket(self):
        """
        Эта функция позволяет найти кнопку "Билеты в кино".
        :return: Кнопка отрабатывает.
        """
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Билеты в кино"))
        )
        self._driver.find_element(By.LINK_TEXT,  'Билеты в кино').click()


    @allure.step("Закрыть браузер")
    def close_driver(self):
        """
        Эта функция выхода.
        :return:quit
        """
        self._driver.quit()