# automation_python_demoblaze ![Status badge](https://img.shields.io/badge/status%20-finished-green)

* Este proyecto nos permite automatizar varias paginas web en la misma solución ya que las funciones principales de selenium se reutilizan para cualquier proyecto,la data de selenium los tomamos de un json, y se utiliza cucumber para realizar los test.

Nota: Para poder ejecutar el test de cucumber se requiere tener una licencia de pycharm profesional.

## 🚀 Comenzando :

* Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

## 📋 Pre-requisitos :

1. Clonar el proyecto.
2. Tener instalado python 3.9 o superior.
3. Instalar PyCharm.
4. Copiar la ruta relativa del proyecto.

    Nota : Ingresar al cmd  y  escribir cd espacio y pegar la ruta relativa del proyecto ejemplo : cd C:\Users\Eduardo_Sanchez\Documents\proyectosTrabajo\automation_testing

5. Dentro del proyecto se encuentra un archivo llamado requierements.txt
6. En el cmd escribiremos: pip install -r .\requierements.txt y damos enter, se instalaran los paquetes que necesitamos para el environment.
7. Abrimos la solución en PyChrarm y debemos de instalar el interprete.
8. Abrimos la clase llamada functions, si se visualizan  las librerias subrayados en color rojo, pasamos el mouse y nos saldra una alerta de instalar el paquete, damos clic  para que lo instale asi sucesivamente con los demas paquetes que tengan este incovneniente.

##  ⚙ Ejecutando las pruebas :

* Para ejecutar los casos de prueba ingresamos a la carpeta de features y se encontratrara el script  CPA_10_sign_up.feature -> damos clic para que se visualice la información de los test y damos clic derecho run CPA_10_sign_up.feature.


* En este link se ve la ejecución de los tres scripts : http://g.recordit.co/iGzBso62ak.gif

* Antes de crear el reporte de allure tenemos que editar el archivo llamado EjecutarConBehaveTags, en este archivo cambiaremos la ruta relativa en donde se encuentra nuestro proyecto, ya que se realiza el cambio lo guardamos y ejecutamos se mostrara la pantalla del cmd ejecutando los scripts, en nuestro proyecto se creara una carpeta llamada allure-results, despues de que se termine de ejecutar los casos de prueba cerramos el cmd y cambiamos la ruta del archivo llamado generar Reporte guardamos y ejecutamos con este archivo generamos el reporte, si no se visualiza el reporte en automatico tenemos que entrar al proyecto en pycharm y buscar la carpeta allure-result se mostrara un html en la parte derecha pasamos el mouse y se visualizaran los navegadores para poderlo ver.

* En este link se visualiza la ejecución del reporte: https://recordit.co/TcNSTaFjQK



## 🔩 Pruebas end-to-end :

* Se crea un usuario nuevo.
* Se ingresa con el usuario y cerramos sesión.
* Se agrega una lap top al carrito de compras y se verifica que se haya agregado.

## 📜 Licencia :

* The MIT License (MIT).

