# -*- coding: utf-8 -*-

from behave import *
from functions.Functions import Functions as Selenium


use_step_matcher("re")


class StepsDefinitions:

    @given("Abro el navegador (.*)")
    def step_impl(self, Navegador):
        Selenium.open_browser(self, navegador=Navegador)

    @when("Navego a la pagina de prueba (.*)")
    def step_impl(self, URL):
        Selenium.go_to_url(self, URL=URL)
        Selenium.page_has_loaded(self)

    @step("Cargo los localizadores de (.*)")
    def step_impl(self, DOM):
        Selenium.get_json_file(self, DOM)
        Selenium.page_has_loaded(self)
        Selenium.wait(self, 2)

    @step("Capturo la pantalla (.*)")
    def step_impl(self, descripcion):
        Selenium.capture(self, descripcion)


    @step("Doy clic en el boton (.*)")
    def step_impl(self, button):
        Selenium.get_elements(self, button).click()

    @step("En el campo (.*)  ingreso (.*)")
    def step_impl(self,locator, usuario):
        Selenium.send_key_text(self,locator, usuario)


    @step("Espero (.*) segundos")
    def step_impl(self, time):
        Selenium.wait(self, int(time))


    @step("acepto la alerta")
    def step_impl(self):
        Selenium.alert_windows(self)


    @then("Se verifica que el (.*) sea igual a (.*)")
    def step_impl(self, localizador, textoAVerificar):
        Selenium.assert_text(self, localizador, textoAVerificar)

    @step("Hago un desplazamiento desde (.*)")
    def step_impl(self, locator):
        Selenium.scroll_to(self, locator)
