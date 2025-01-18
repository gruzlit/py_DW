import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.epic("DW")
@allure.feature("Отработка кнопки - Просмотр фильма")
class WatchMovie:

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


    @allure.step("Ввести название фильма")
    def search_input(self):
        """
        Эта функция вводит в поле название фильма.
        :return: "Огниво"
        """
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.NAME, "kp_query"))
        )
        self._driver.find_element(By.NAME, "kp_query").send_keys("Огниво", Keys.ENTER)




    @allure.step("Найти фильм из списка")
    def choice_movie(self):
        """
        Эта функция находит фильм из списка.
        :return: Фильм найден.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#block_left_pad > div > div:nth-child(3) > div > div.info > p > a").click()



    @allure.step("Начать просмотр")
    def view_movie(self):
        """
        Эта функция позволяет найти кнопку для начала просмотра.
        :return: Просмотр фильма.
        """
        self._driver.find_element(By.CSS_SELECTOR, "[data-tid='712957ef']").click()




    @allure.step("Закрыть браузер")
    def close_driver(self):
        """
        Эта функция выхода.
        :return:quit
        """
        self._driver.quit()

 #