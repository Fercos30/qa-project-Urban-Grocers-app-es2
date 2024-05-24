# Pruebas de Automatización Proyecto Urban Grocers 
- El objetivo de este proyecto es automatizar las pruebas de la lista de comprobación para la API de Urban Grocers. 
- Haremos pruebas para la creación de nuevo usario y crear un nuevo kit. Tanto positivas como negativas.
# Lenguaje y herramientas:
- Utilizaremos el lenguaje de Python y abriremos nuestro proyecto en programa Pycharm.
- Utiliza documentación en APIDOCS.
# Requisitos para el inicio de pruebas:
1. Lo primero es tener iniciada nuestra URL del servidor y colocarla en el primer archivo configuration.py junto con los demás requisitos 
2. Endpoint para creación de un nuevo usuario
CREATE_USER_PATH = "/api/v1/users/"
3.  Endpoint para creación de un kit
KITS_PATH = "/api/v1/kits/"
4. Tener instaladas las librerias: Pytest, Requests y  JSON. 
5. Crear las funciones positivas y negativas con assert.
# Preparación del proyecto:
- En el archivo sender_stand_request.py enviaremos y almacenaremos todas las solicitudes que necesitamos. Aqui pondremos las solicitudes para: 
-- Crear un nuevo usuario 
-- Crear un nuevo kit de usuario.
- En el archivo create_kit_name_kit_test.py es donde ejecutaremos las pruebas y programamos el código. 
- En el archivo data.py y colocamos el cuerpo de las solicitudes POST.
# Conclusión:
Realizamos 9 pruebas las cuales, cuatro nos dieron error, según el resultado esperado.
