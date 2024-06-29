from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import allure


@allure.description("Prueba la creación, edición, lectura, edición y eliminación de un usuario")
@allure.severity(allure.severity_level.CRITICAL)
def test_crud_user(browser, username="1746392648", password="64e4f09abf630dec6a6e5fe5", ci="1234567890", name="test",
                   voted="true", role="admin", new_ci="0987654321", new_name="tested", new_voted="false", new_role="voter"):
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

    with allure.step("Ingresar a Administrar Usuarios"):
        time.sleep(2)
        browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div[2]/button[1]").click()

    with allure.step("Comprobar que aparecen los usuarios"):
        time.sleep(2)
        browser.find_element(by=By.XPATH, value="//div[@class='contenedor-U']")

    with allure.step("Ingresar un nuevo usuario"):
        time.sleep(2)
        browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div[3]/div[2]/div/div/div/div/button").click()
        time.sleep(2)
        browser.find_element(by=By.XPATH, value="//input[@id='ci']").send_keys(ci)
        time.sleep(1)
        browser.find_element(by=By.XPATH, value="//input[@id='name']").send_keys(name)
        time.sleep(1)
        select_element_vote = browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div[3]/div["
                                                                      "1]/div/form/div[3]/select")
        select_vote = Select(select_element_vote)
        select_vote.select_by_value(voted)
        time.sleep(1)
        select_element_role = browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div[3]/div["
                                                                      "1]/div/form/div[4]/select")
        select_role = Select(select_element_role)
        select_role.select_by_value(role)
        time.sleep(1)
        browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div[3]/div[1]/div/form/div[5]/button[1]").click()

    with allure.step("Editar un usuario"):
        time.sleep(2)
        edit_tr = browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div[3]/div[2]/div/div/table/tbody/tr[8]")
        browser.execute_script("arguments[0].scrollIntoView();", edit_tr)
        time.sleep(2)
        edit_button = browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div[3]/div["
                                                              "2]/div/div/table/tbody/tr[8]/td[6]/button[1]")
        browser.execute_script("arguments[0].click();", edit_button)
        time.sleep(1)
        browser.find_element(by=By.XPATH, value="//input[@id='ci']").clear()
        browser.find_element(by=By.XPATH, value="//input[@id='ci']").send_keys(new_ci)
        time.sleep(1)
        browser.find_element(by=By.XPATH, value="//input[@id='name']").clear()
        browser.find_element(by=By.XPATH, value="//input[@id='name']").send_keys(new_name)
        time.sleep(1)
        select_element_vote = browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div[3]/div["
                                                                      "1]/div/form/div[3]/select")
        select_vote = Select(select_element_vote)
        select_vote.select_by_value(new_voted)
        time.sleep(1)
        select_element_role = browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div[3]/div["
                                                                      "1]/div/form/div[4]/select")
        select_role = Select(select_element_role)
        select_role.select_by_value(new_role)
        time.sleep(1)
        browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div[3]/div[1]/div/form/div[5]/button[1]").click()

    with allure.step("Eliminar un usuario"):
        time.sleep(2)
        browser.find_element(by=By.XPATH, value="//*[@id='root']/div/div[3]/div[2]/div/div/table/tbody/tr[8]/td["
                                                "6]/button[2]").click()

    with allure.step("Comprobar que el usuario se ha eliminado"):
        time.sleep(2)
        WebDriverWait(browser, 5).until_not(
            ec.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div/table/tbody/tr[8]")))
