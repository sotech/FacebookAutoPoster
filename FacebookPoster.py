from selenium import webdriver
import os
import time

#Navegador

#Configuracion
perfil = webdriver.FirefoxProfile()

#Eliminar notificaciones
perfil.set_preference("dom.webnotifications.enabled", False)

#Creacion del navegador
browser = webdriver.Firefox(firefox_profile=perfil)

#Mensaje
archivo = open("mensaje.txt", 'r',encoding="utf8")
mensaje = archivo.read()
archivo.close()

#Lista de grupos
archivo = open("grupos.txt", 'r')
lista_grupos = []
for grupo in archivo.readlines():
    lista_grupos.append(grupo)
archivo.close()

#Imagen
imagen = os.path.join(os.getcwd(), "imagen.jpg")

print(imagen)
print("Entrando a facebook")
browser.get('https://www.facebook.com')
print("Maximizando")
browser.maximize_window()

#Datos previos
print("Carga del archivo")
#Cargamos el archivo
archivo = open("datos.txt", "r")
lineas = []
for linea in archivo.readlines():
    lineas.append(linea)
archivo.close()
#Fin de uso del archivo

usuario = lineas[0]
contra = lineas[1]

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
print("Logeando")
#Logear

if LogearFacebook(usuario,contra):
    #Recorrido de grupos
    i=1
    for grupo in lista_grupos:
        print("Entrando al grupo " + str(i) + ". Link: " + grupo)
        browser.get(grupo)
        print("Ubicando caja de posteo")
        #Ubicar la caja de posteo
        p = browser.find_element_by_xpath("//*[@name='xhpc_message_text']")
        print("Enviando mensaje")
        #Enviando mensaje
        p.send_keys(mensaje)
        #Cargar imagen
        img = browser.find_element_by_xpath("//input[@class='_n _5f0v']")
        img.send_keys(imagen)
        time.sleep(10)

        submit = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/span/button')
        submit.click()
        time.sleep(10)
        i+=1
    print("Proceso finalizado")
else:
    print("Ocurrio un error en el Logeo")

browser.quit()