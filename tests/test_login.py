from selenium.webdriver.common.by import By
import time
import allure


@allure.description("Prueba el acceso como votante.")
@allure.severity(allure.severity_level.BLOCKER)
def test_login_user(browser, username="1748392046", password="64e7a1e4756e33a1f0f2c65d"):
    with allure.step("Ingresar a la página principal"):
        browser.get("http://localhost:3000")
        browser.implicitly_wait(10)

    with allure.step("Ingresar Cédula de Identidad y Código Secreto del votante"):
        time.sleep(1)
        browser.find_element(by=By.ID, value="ci").send_keys(username)
        time.sleep(1)
        browser.find_element(by=By.ID, value="code").send_keys(password)

    with allure.step("Click en el botón Ingresar"):
        time.sleep(2)
        browser.find_element(by=By.CSS_SELECTOR, value="button").click()

    with allure.step("Comprobar que se ingresó al sistema"):
        time.sleep(2)
        current_url = browser.current_url
        assert current_url == "http://localhost:3000/ini"


@allure.description("Prueba el acceso como Administrador.")
@allure.severity(allure.severity_level.BLOCKER)
def test_login_admin(browser, username="1746392648", password="64e4f09abf630dec6a6e5fe5"):
    with allure.step("Ingresar a la página principal"):
        browser.get("http://localhost:3000")
        browser.implicitly_wait(10)

    with allure.step("Ingresar Cédula de Identidad y Código Secreto del administrador"):
        time.sleep(1)
        browser.find_element(by=By.ID, value="ci").send_keys(username)
        time.sleep(1)
        browser.find_element(by=By.ID, value="code").send_keys(password)

    with allure.step("Click en el botón Ingresar"):
        time.sleep(2)
        browser.find_element(by=By.CSS_SELECTOR, value="button").click()

    with allure.step("Comprobar que se ingresó al sistema"):
        time.sleep(2)
        current_url = browser.current_url
        assert current_url == "http://localhost:3000/admin"


@allure.description("Prueba el acceso fallido con datos erroneos.")
@allure.severity(allure.severity_level.BLOCKER)
def test_fail_login(browser, username="1035574816", password="64e9f521bf630dqc3a6e5fe9"):
    with allure.step("Ingresar a la página principal"):
        browser.get("http://localhost:3000")
        browser.implicitly_wait(10)

    with allure.step("Ingresar Cédula de Identidad y Código Secreto del administrador"):
        time.sleep(1)
        browser.find_element(by=By.ID, value="ci").send_keys(username)
        time.sleep(1)
        browser.find_element(by=By.ID, value="code").send_keys(password)

    with allure.step("Click en el botón Ingresar"):
        time.sleep(2)
        browser.find_element(by=By.CSS_SELECTOR, value="button").click()

    with allure.step("Comprobar que se ingresó al sistema"):
        time.sleep(2)
        current_url = browser.current_url
        assert current_url == "http://localhost:3000/"
