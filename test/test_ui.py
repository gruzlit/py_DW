import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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
    watch_movie.close_driver()


@allure.severity("normal")
@allure.title("Выбор билета в кино")
def test_ticket():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    cinema_ticket = CinemaTicket(driver)
    cinema_ticket.open_pages()
    cinema_ticket.choice_ticket()
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
    buy_ticket.close_driver()