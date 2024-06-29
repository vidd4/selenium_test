from selenium.webdriver.common.by import By
import time
import allure


@allure.description("Prueba de un voto")
@allure.severity(allure.severity_level.CRITICAL)
def test_vote(browser, username="1730285472", password="64e79ae8756e33a1f0f2c65c"):
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

    with allure.step("Click en el Ingresar para votar"):
        time.sleep(2)
        browser.find_element(by=By.CSS_SELECTOR, value="button").click()

    with allure.step("Seleccionar un candidato"):
        time.sleep(2)
        browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div[2]/div/div[1]/div/div/button").click()

    with allure.step("Click en Ver Resultado"):
        time.sleep(2)
        browser.find_element(by=By.CSS_SELECTOR, value="button").click()

    with allure.step("Comprobar aparición de Resultados"):
        time.sleep(2)
        assert browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div/div[2]")

    with allure.step("Comprobar botón Imprimir"):
        time.sleep(2)
        print_div = browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div/div[3]")
        browser.execute_script("arguments[0].scrollIntoView();", print_div)
        time.sleep(2)
        assert browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div/div[3]/button")


@allure.description("Prueba comprobación de solamente votar una vez")
@allure.severity(allure.severity_level.CRITICAL)
def test_vote2(browser, username="1730285472", password="64e79ae8756e33a1f0f2c65c"):
    with allure.step("Ingresar a la página principal"):
        browser.get("http://localhost:3000")
        browser.implicitly_wait(10)

    with allure.step("Ingresar Cédula de Identidad y Código Secreto del votante"):
        time.sleep(1)
        browser.find_element(by=By.ID, value="ci").send_keys(username)
        time.sleep(1)
        browser.find_element(by=By.ID, value="code").send_keys(password)

    with allure.step("Comprobar que solo se puede votar una vez"):
        current_url = browser.current_url
        assert current_url == "http://localhost:3000/"
