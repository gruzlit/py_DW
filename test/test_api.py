import requests
import allure

my_headers = {'X-API-KEY': '2XTMWWY-976408P-JN68P94-S8QTJ4Q'}
base_url = "https://api.kinopoisk.dev/"


@allure.epic("Кинопоиск API")
@allure.severity("blocker")
@allure.step("Получение названия фильма")
def test_get_movie():
    """
    Эта функция находит фильм по названию.
    Проверяет статус-код.
    :return: "Холоп 2", status_code == 200.
    """
    resp = requests.get(base_url + 'v1.4/movie/search?page=1&limit=1&query=Холоп 2', headers=my_headers)
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 200


@allure.epic("Кинопоиск API")
@allure.severity("critical")
@allure.step("Получение фильма по id")
def test_get_movie_id():
    """
    Эта функция находит фильм по id.
    Проверяет статус-код.
    :return: status_code == 200
    """
    resp = requests.get(base_url + 'v1.4/movie/666?limit=1', headers=my_headers)
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 200


@allure.epic("Кинопоиск API")
@allure.severity("normal")
@allure.step("Получение рейтинга")
def test_get_rating():
    """
    Эта функция находит фильм по рейтингу.
    Проверяет статус-код.
    :return: status_code == 200
    """
    resp = requests.get(base_url + 'v1.4/movie?type=movie&year=2021&rating.kp=7-8&limit=5', headers=my_headers)
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 200


@allure.epic("Кинопоиск API")
@allure.severity("blocker")
@allure.step("Получение фильма по жанру")
def test_get_genres():
    """
    Эта функция находит фильм по жанру.
    Проверяет статус-код.
    :return: status_code == 200
    """
    resp = requests.get(base_url + 'v1.4/movie/random?type=movie&year=2019&genres.name=комедия&countries.name=Франция&limit=3', headers=my_headers)
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 200


@allure.epic("Кинопоиск API")
@allure.severity("critical")
@allure.step("Получение актеров по id")
def test_get_person():
    """
    Эта функция находит актеров по id .
    Проверяет статус-код.
    :return: status_code == 200
    """
    resp = requests.get(base_url + 'v1.4/person/592532', headers=my_headers)
    assert resp.headers["Content-Type"] == 'application/json; charset=utf-8'
    assert resp.status_code == 200
