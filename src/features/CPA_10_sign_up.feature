Feature: Creación de un usuario.

  @test
  Scenario Outline: Crear un usuario nuevo en la pagina de demoblaze.
  Given
  """
        Como usuario financiero, quiero ingresar a la pagina de demoblaze y poder registrarme como un usuario nuevo.

  """

    Given Abro el navegador Chrome
      And  Cargo los localizadores de sign_up
    When Navego a la pagina de prueba https://www.demoblaze.com/index.html
      And Capturo la pantalla  principal
      And Doy clic en el boton sign in
      And En el campo nombre usuario  ingreso <nombre>
      And En el campo password  ingreso Prueba2304
      And Doy clic en el boton sign up
      And Capturo la pantalla se creo el usuario
      And acepto la alerta



    Examples:
        |    nombre        |
        | Lucia Hernandez  |




  @test
  Scenario: Crear un usuario nuevo en la pagina de demoblaze.
  Given
  """
        Como usuario financiero, quiero ingresar a la pagina de demoblaze y poder registrarme como un usuario nuevo.

  """

    Given Abro el navegador Chrome
      And  Cargo los localizadores de log_in
    When Navego a la pagina de prueba https://www.demoblaze.com/index.html
      And Doy clic en el boton menu log in
      And En el campo nombre del usuario  ingreso Lucia Hernandez
      And En el campo password del usuario  ingreso Prueba2304
      And Doy clic en el boton log in
      And Espero 5 segundos
    Then Se verifica que el usuario sea igual a Welcome Lucia Hernandez
      And Capturo la pantalla home page
      And Doy clic en el boton log out
      And Capturo la pantalla pagina principal
    
    
    
  @test
  Scenario: Crear un usuario nuevo en la pagina de demoblaze.
  Given
  """
        Como usuario financiero, quiero ingresar a la pagina de demoblaze y poder registrarme como un usuario nuevo.

  """

    Given Abro el navegador Chrome
      And  Cargo los localizadores de log_in
    When Navego a la pagina de prueba https://www.demoblaze.com/index.html
      And Doy clic en el boton menu log in
      And En el campo nombre del usuario  ingreso Lucia Hernandez
      And En el campo password del usuario  ingreso Prueba2304
      And Doy clic en el boton log in
      And Espero 5 segundos
    Then Se verifica que el usuario sea igual a Welcome Lucia Hernandez
      And Capturo la pantalla home page
      And Doy clic en el boton laptops
      And Hago un desplazamiento desde sony vaio i5
    Then Se verifica que el dell i7 sea igual a Dell i7 8gb
      And Doy clic en el boton dell i7
      And Doy clic en el boton agregar al carrito
      And Capturo la pantalla agregar al carrito
      And acepto la alerta
      And Doy clic en el boton cart
    Then Se verifica que el texto dell i7 sea igual a Dell i7 8gb
      And Capturo la pantalla productos
      And Doy clic en el boton eliminar



