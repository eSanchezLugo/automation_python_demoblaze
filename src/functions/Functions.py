import os
import re
import time
import json
import allure
import pytest
Scenario = {}
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from functions.Initialize import Initialize
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, NoSuchWindowException, \
    TimeoutException

diaGlobal = time.strftime(Initialize.DateFormat)  # formato aaaa/mm/dd
horaGlobal = time.strftime(Initialize.HourFormat)  # formato 24 houras
NAVEGADOR = Initialize.Navegador


class Functions(Initialize):

    def open_browser(self, navegador=Initialize.Navegador):

        print("Directorio Base: " + Initialize.basedir)
        self.ventanas = {}
        print("----------------")
        print(navegador)
        print("---------------")

        if navegador == "Chrome":
            options = OpcionesChrome()
            options.add_argument('start-maximized')
            self.driver = webdriver.Chrome(chrome_options=options,
                                           executable_path=ChromeDriverManager().install())
            self.driver.implicitly_wait(10)
            self.driver.delete_all_cookies()
            self.nWindows = 0
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            return self.driver

        elif navegador == "Opera":
            self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.nWindows = 0
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            return self.driver

        elif navegador == "Firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.nWindows = 0
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            return self.driver

        elif navegador == "Edge":
            self.driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.delete_all_cookies()
            self.nWindows = 0
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            return self.driver

    def go_to_url(self, URL=Initialize.Url):
        self.driver.get(URL)

    def tearDown(self):
        print("Se cerrará  el DRIVER")
        self.driver.quit()

    # Json
    def get_json_file(self, file: object) -> object:

        json_path = Initialize.Json + "/" + file + '.json'
        try:
            with open(json_path, "r") as leer_archivo:
                self.json_strings = json.loads(leer_archivo.read())
                print("obtener_archivo_json :" + json_path)
                return self.json_strings
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"obtener_archivo_json : No se encontro el archivo" + file)
            Functions.tearDown(self)

    def get_entity(self, entity):
        if self.json_strings is False:
            print("Define el DOM para está prueba")
        else:
            try:
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                return True

            except KeyError:
                pytest.skip(u"get_entity : No se encontro la llave a la cual hace referencia :" + entity)
                Functions.tearDown(self)
                return None

    def get_elements(self, entity, MyTextElement=None):

        global elements
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is not None:
            try:

                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_link_text(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "css":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "class":
                    elements = self.driver.find_element_by_class_name(self.json_ValueToFind)

                print("get_elements :" + self.json_ValueToFind)
                return elements

            except NoSuchElementException:
                print("get_text : No se encontro el elemento: " + self.json_ValueToFind)
                self.driver.implicitly_wait(self)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                self.driver.implicitly_wait(self)
                Functions.tearDown(self)

        else:
            print(u'No se encontro el valor en el json definido')

    def get_text(self, entity, MyTextElement=None):

        global elements
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is not None:
            try:

                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_link_text(self.json_ValueToFind)

                elif self.json_GetFieldBy.lower() == "css":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                print("get_elements :" + self.json_ValueToFind)
                return elements.text

            except NoSuchElementException:
                print("get_text : No se encontro el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

        else:
            print("No se encontro el valor en el json definido")

    def wait(self, timeLoad=8):
        print("Esperar: Inicia (" + str(timeLoad) + ")")
        try:
            totalWait = 0
            while (totalWait < timeLoad):
                time.sleep(1)
                totalWait = totalWait + 1
        finally:
            print("Esperar: Carga Finalizada ... ")

    def wait_element(self, locator, MyTextElement=0):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is not None:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(u": Se visualizo el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(u"wait_element: Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)

                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                    print(u"wait_element: Se visualizo el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print(u"wait_element: Se visualizo el elemento " + locator)
                    return True

            except TimeoutException:
                print(u"wait_element: No presente " + locator)
                Functions.tearDown(self)
            except NoSuchElementException:
                print(u"wait_element: No presente " + locator)
                Functions.tearDown(self)
        else:
            return print(u'No se encontro el valor en el Json definido')

    def check_element(self, locator, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is not None:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    print(u'check_element: Se visualizo el elemento ' + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    print('check_element: Se visualizo el elemento ' + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    print(u'check_element: Se visualizo el elemento ' + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.LINK, self.json_ValueToFind)))
                    print(u"check_element: Se visualizo el elemento " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                    print(u"check_element: Se visualizo el elemento " + locator)
                    return True

            except NoSuchElementException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                return False
            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                return False
        else:
            print(u'No se encontro el valor en el Json definido')

    def assert_text(self, locator, TEXTO, MyTextElement=None):

        global ObjText
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is not None:
            if self.json_GetFieldBy.lower() == "id":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.ID, self.json_ValueToFind)))
                ObjText = self.driver.find_element_by_id(self.json_ValueToFind).text

            elif self.json_GetFieldBy.lower() == "name":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.NAME, self.json_ValueToFind)))
                ObjText = self.driver.find_element_by_name(self.json_ValueToFind).text

            elif self.json_GetFieldBy.lower() == "xpath":
                if MyTextElement is not None:
                    self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.XPATH, self.json_ValueToFind)))
                ObjText = self.driver.find_element_by_xpath(self.json_ValueToFind).text

            elif self.json_GetFieldBy.lower() == "link":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                ObjText = self.driver.find_element_by_partial_link_text(self.json_ValueToFind).text

            elif self.json_GetFieldBy.lower() == "css":
                if MyTextElement is not None:
                    self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                ObjText = self.driver.find_element_by_css_selector(self.json_ValueToFind).text
        else:
            print(u"No se encontro el valor en el Json definido")

        print("Verificar Texto: el valor mostrado en: " + locator + " es: " + ObjText + " el esperado es: " + TEXTO)
        assert TEXTO == ObjText, "Los valores comparados no coinciden"


    def get_select_elements(self, entity):
        global select
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is not None:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    select = Select(self.driver.find_element_by_id(self.json_ValueToFind))

                elif self.json_GetFieldBy.lower() == "name":
                    select = Select(self.driver.find_element_by_name(self.json_ValueToFind))

                elif self.json_GetFieldBy.lower() == "css":
                    select = Select(self.driver.find_element_by_css_selector(self.json_ValueToFind))

                elif self.json_GetFieldBy.lower() == "xpath":
                    select = Select(self.driver.find_element_by_xpath(self.json_ValueToFind))

                elif self.json_GetFieldBy.lower() == "link":
                    select = Select(self.driver.find_element_by_partial_link_text(self.json_ValueToFind))

                print("get_select_elements: " + self.json_ValueToFind)
                return select

            # USO

            #       select by visible text  #       select.select_by_visible_text('Banana')

            #       select by value  #       select.select_by_value('1')

            except NoSuchElementException:
                print("No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

            except TimeoutException:
                print("No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
        else:
            print(u'No se encontro el valor en el Json definido')

    def select_by_value(self, entity, text):
        Functions.get_select_elements(self, entity).select_by_value(text)

    def select_by_text(self, entity, text):
        Functions.get_select_elements(self, entity).select_by_visible_text(text)

    def send_key_text(self, entity: object, text: object, TextoJson: object = None) -> object:
        Functions.get_elements(self, entity, TextoJson).clear()
        Functions.get_elements(self, entity, TextoJson).send_keys(text)

    def send_especific_keys(self, element: object, key: object, MyTextElement: object = None) -> object:
        """

        :rtype: 
        """
        if key == 'Enter':
            Functions.get_elements(self, element).send_keys(Keys.ENTER)
        elif key == 'Enter' and MyTextElement is not None:
            Functions.get_elements(self, element, MyTextElement).send_keys(Keys.ENTER)

        elif key == 'Tab':
            Functions.get_elements(self, element).send_keys(Keys.TAB)
        elif key == 'Space':
            Functions.get_elements(self, element).send_keys(Keys.SPACE)
        time.sleep(3)

    def page_has_loaded(self):
        driver = self.driver
        print("Checking if {} page is loaded.".format(self.driver.current_url))
        page_state = driver.execute_script('return document.readyState;')
        yield
        WebDriverWait(driver, 30).until(lambda driver: page_state == 'complete')
        assert page_state == 'complete', "No se completo la carga"

    def js_clic(self, locator, MyTextElement=None):

        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is not None:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    localizador = self.driver.find_element(By.ID, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u'Se hizo click en: ' + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    localizador = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"Se hizo click en: " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "link":
                    localizador = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u'Se hizo click en: ' + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "name":
                    localizador = self.driver.find_element(By.NAME, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"Se hizo click en: " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "css":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    localizador = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].click();", localizador)
                    print(u"Se hizo click en: " + locator)
                    return True

            except TimeoutException:
                print(u'js_clic: No presente ' + locator)
                Functions.tearDown(self)
        else:
            return print("No se encontro el valor en el Json definido")

    def scroll_to(self, locator, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    localizador = self.driver.find_element(By.ID, self.json_ValueToFind)
                    self.driver.execute_script('arguments[0].scrollIntoView();', localizador)
                    print(u'scroll_to: ' + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "xpath":
                    localizador = self.driver.find_element(By.XPATH, self.json_ValueToFind)
                    self.driver.execute_script('arguments[0].scrollIntoView();', localizador)
                    print(u'scroll_to: ' + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "css":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                    localizador = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
                    print(u"scroll_to: " + locator)
                    return True

                elif self.json_GetFieldBy.lower() == "link":
                    localizador = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)
                    self.driver.execute_script("arguments[0].scrollIntoView();", localizador)
                    print(u"scroll_to: " + locator)
                    return True

            except TimeoutException:
                print(u"scroll_to: No presente " + locator)
                Functions.tearDown(self)

    def alert_windows(self, accept="accept"):
        try:
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.alert_is_present(), print("Esperando alerta..."))

            alert = self.driver.switch_to.alert

            print(alert.text)

            if accept.lower() == "accept":
                alert.accept()
                print("Click in Accept")
            else:
                alert.dismiss()
                print("Click in Dismiss")

        except NoAlertPresentException:
            print('Alerta no presente')
        except NoSuchWindowException:
            print('Alerta no presente')
        except TimeoutException:
            print("Alerta no presente")


    def screenshot(self, TestCase="Captura"):
        PATH = Functions.create_path(self)
        img = f'{PATH}/{TestCase}_(' + str(Functions.current_hour(self)) + ')' + '.png'
        self.driver.get_screenshot_as_file(img)
        print(img)
        return img

    def capture(self, Descripcion):
        allure.attach(self.driver.get_screenshot_as_png(), Descripcion, attachment_type=allure.attachment_type.PNG)


