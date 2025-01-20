import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from SearchMovie import SearchMovie
from AuthLogin import Authlogin
from WatchMovie import WatchMovie
from CinemaTicket import CinemaTicket
from BuyTicket import BuyTicket


@allure.severity("blocker")
@allure.title("Авторизация на сайте")
def test_auth():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    auth_login = Authlogin(driver)
    auth_login.open_pages()
    auth_login.login_button()
    auth_login.user_name()
    current_url = driver.current_url
    with allure.step("Проверяем , что получен  текущий URL текущей страницы"):
     assert "kinopoisk.ru" in current_url
    auth_login.close_driver()


@allure.severity("normal")
@allure.title("Поиск фильма на сайте")
def test_search():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    search_movie = SearchMovie(driver)
    search_movie.open_pages()
    search_movie.search_input()
    search_movie.choice_movie()
    with allure.step("Проверяем,что искомый фильм найден"):
     assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Огниво (2024)"
    search_movie.close_driver()


@allure.severity("critical")
@allure.title("Просмотр фильма")
def test_view():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    watch_movie = WatchMovie(driver)
    watch_movie.open_pages()
    watch_movie.search_input()
    watch_movie.choice_movie()
    watch_movie.view_movie()
    current_url = driver.current_url
    with allure.step("Проверяем , что получен  текущий URL текущей страницы"):
     assert "kinopoisk.ru" in current_url
    watch_movie.close_driver()


@allure.severity("normal")
@allure.title("Выбор билета в кино")
def test_ticket():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    cinema_ticket = CinemaTicket(driver)
    cinema_ticket.open_pages()
    cinema_ticket.choice_ticket()
    current_url = driver.current_url
    with allure.step("Проверяем , что получен  текущий URL текущей страницы"):
     assert "kinopoisk.ru" in current_url
    cinema_ticket.close_driver()


@allure.severity("normal")
@allure.title("Покупка билетов кино")
def test_buy():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    buy_ticket = BuyTicket(driver)
    buy_ticket.open_pages()
    buy_ticket.choice_ticket()
    buy_ticket.buy_ticket()
    current_url = driver.current_url
    with allure.step("Проверяем , что получен  текущий URL текущей страницы"):
     assert "kinopoisk.ru" in current_url
    buy_ticket.close_driver()