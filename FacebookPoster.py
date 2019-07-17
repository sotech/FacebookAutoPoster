'''
PYTHON SCRIPT: Facebook Auto Poster
Autor: German Sommariva
Contacto
Facebook: www.facebook.com/german.sommariva
'''

from selenium import webdriver
import os
import time

def CargarMensaje():
    print("Cargando mensaje")
    # Mensaje
    archivo = open("mensaje.txt", 'r', encoding="utf8")
    msj = archivo.read()
    archivo.close()
    return msj

def CargarGrupos():
    print("Cargando listado de grupos")
    # Lista de grupos
    archivo = open("grupos.txt", 'r')
    lg = []
    for grupo in archivo.readlines():
        lg.append(grupo)
    archivo.close()
    return lg

def CargarImagen():
    usi = int(input('''
        Ingrese una opcion
        0. No usar imagen
        1. Usar imagen
    '''))
    while (usi != 1 and usi != 0):
        print("Opcion incorrecta, vuelva a intentar")
        usi = int(input('''
            Ingrese una opcion
            0. No usar imagen
            1. Usar imagen
        '''))
    return usi

def CargarDireImagen(op):
    if (op == 1):
        print("Cargando direccion de la imagen")
        # Imagen
        imagen = os.path.join(os.getcwd(), "imagen.jpg")
    else:
        imagen = ""
    return imagen

def CargarLogin():
    # Datos previos
    print("Carga datos del Login")
    # Cargamos el archivo
    archivo = open("datos.txt", "r")
    lineas = []
    for linea in archivo.readlines():
        lineas.append(linea)
    archivo.close()
    # Fin de uso del archivo

    return lineas

#Funcion Logear
def LogearFacebook(u,c):
    #Elementos de facebook
    try:
        login = browser.find_element_by_id("email")
        p = browser.find_element_by_id("pass")
        boton = browser.find_element_by_id("loginbutton")

        # Llenado de datos
        login.send_keys(u)
        p.send_keys(c)
        boton.click()

        return True
    except:
        return False

##########
#Navegador
##########
print("Iniciando Programa")
usar_imagen = CargarImagen()
print("Configurando navegador")
#Configuracion
perfil = webdriver.FirefoxProfile()
#Eliminar notificaciones
perfil.set_preference("dom.webnotifications.enabled", False)
#Creacion del navegador
browser = webdriver.Firefox(firefox_profile=perfil)

print("Entrando a facebook")
browser.get('https://www.facebook.com')
print("Maximizando")
browser.maximize_window()


mensaje = CargarMensaje()
if "mensajeprueba" in mensaje:
    print("Se esta usando el mensaje predeterminado. Modifique el archivo \"mensaje.txt\" con su propio mensaje")
    browser.quit()

lista_grupos = CargarGrupos()
if "www.grupoprueba1.com" in lista_grupos:
    print("Se esta usando la lista de grupos predeterminada. Modifique el archivo \"grupos.txt\" con su propia lista")
    browser.quit()


imagen = CargarDireImagen(usar_imagen)
datos_login = CargarLogin()

usuario = datos_login[0]
contra = datos_login[1]

if usuario == "usuarioprueba" or contra == "contraseñaprueba":
    print("Se estan usando datos de login predeterminada. Modifique el archivo \"datos.txt\" con sus propios datos")
    browser.quit()

print("Logeando")
LogearFacebook(usuario, contra)
#Logear
#Recorrido de grupos
i = 1
cantidad_lograda = 0
for grupo in lista_grupos:
    try:
        print("Entrando al grupo " + str(i) + ". Link: " + grupo)
        browser.get(grupo)
        time.sleep(5)

        print("Realizando posteo")

        #Ubicar la caja de posteo
        p = browser.find_element_by_xpath("//*[@name='xhpc_message_text']")
        print("Enviando mensaje")
        #Enviando mensaje
        p.send_keys(mensaje)
        time.sleep(3)

        if usar_imagen == 1:
            #Cargar imagen
            print("Enviando imagen")
            img = browser.find_element_by_xpath("//input[@class='_n _5f0v']")
            img.send_keys(imagen)
            time.sleep(10)

        #Posteando
        submit = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/span/button')
        print("Posteando")
        submit.click()
        time.sleep(10)
        cantidad_lograda += 1
        print(" ")
    except:
        print("Ocurrio un error con el grupo " + str(i) + ". Link: " + grupo)
    i += 1
print("Se logró publicar en " + str(cantidad_lograda) + "/" + str(len(lista_grupos)) + " grupos.")
print("Proceso finalizado")

browser.quit()
