import os #Esta libreria me permite interactuar con las funciones basicas del sistema (comandos de windows, etc.)
import json #Con esta libreria puedo interactuar con los archivos .json, los utilizo para almacenar configuraciones y valores de BCrypt.
import smtplib #NOTE: Comprobar si esto tiene realmente una utilidad. (Posibilidad de eliminarla).

#NOTE: Recuerda que para ejecutar PyInstaller tienes que hacerlo con python -m PyInstaller (respetando las mayúsculas).
#TODO: Revisa el error de "CANNOT OPEN SELF EN EL ARCHIVO EJECUTABLE CON PYINSTALLER"

#Variables Globales del Sistema
#Básicamente la declaro aquí, al principio para poder acceder a ella desde cualquier función, por ello recibe el nombre de variable global.

nameOfUser = "" #Esta variable sirve para que Bcrypt pueda dirigirse a ti por tu nombre... Y para otras funciones :)

def adminMenu():
    path = input("Enter an specific path to run the command: ")
    if path == "":
        command = input("Enter a command to run: ")
        if command == "exit":
            accreditFunction()
        else:
            os.system(command)
            adminMenu()
    else:
        os.chdir(path)
        command = input("Enter a command to run: ")
        os.system(command)
        input()
        os.system("cls")
        adminMenu()


#Esta función no es visible para el usuario, me sirve para tocar parámetros de BCrypt y archivos del sistema.
def adminConsole():
    os.system("cls")
    adminUser = input("Enter your admin username: ")
    adminPassword = input("Enter your admin password: ")

    os.chdir("C:\\BCrypt\\users\\adminworkspace")

    if not os.path.isfile('senna.json'):
        os.system("cls")
        print("No se ha encontrado el archivo de configuración de Senna, presione enter para volver al menú principal.")
        input()
        accreditFunction()
    else:
        fileName = 'senna.json'
        jsonToRead = open(fileName, "r")
        jsonData = jsonToRead.read()
        obj = json.loads(jsonData)
        nameOfAdmin = str(obj[adminUser]["name"])
        passwordOfUser = str(obj[adminUser]["password"])

        if adminPassword == passwordOfUser:
            adminMenu()
        else:
            print("La contraseña es incorrecta, presione enter para volver al menú principal.")
            input()
            accreditFunction()

#Esta función crea los archivos necesarios para que funcione la función de arriba.
def createAdminWorkspace():
    os.chdir("C:\\BCrypt\\users")
    os.mkdir("adminworkspace")

#Básicamente aquí se comprueba si existe el directorio de BCrypt (lo que significa que ya se ha realizado el primer inicio y se pasaria a la accreditFunction), si no existe se crea.
def performFirstStart():
    os.chdir("C:\\")
    if os.path.isdir("BCrypt"):
        accreditFunction()
    else:
        os.mkdir("BCrypt")
        os.chdir("C:\\BCrypt")
        os.mkdir("settings")
        os.chdir("C:\\BCrypt\\settings")

        newSettings = {
            "firstStart": "true"
        }
        with open('settings.json', 'w') as f:
            json.dump(newSettings, f, ensure_ascii = False, indent = 4)
        
        os.chdir("C:\\BCrypt")
        os.mkdir("users")
        createAdminWorkspace()
        accreditFunction()

#Función para crear un usuario, mas claro el agua.
def createUser():
    os.system("cls") #Limpia la terminal de forma que no se acumula texto.
    os.chdir("C:\\BCrypt\\users") #Accede al directorio donde se almacenan los usuarios.

    username = input("Introduce tu nuevo username: ") #Pide el nombre de ususario

    #A partir de aqui se rogen las variables que se van a utilizar para crear el usuario.
    newUser = {
        username: {
            "name": input("Introduce tu nombre: "),
            "email": input("Introduce tu dirección de correo electrónico: "),
            "password": input("Introduce tu nueva contraseña: ")
        }
    }
    #Se crea un archivo .json con el nombre del usuario y se guarda en el directorio de usuarios (por ello el nombre de usuario se pide antes que el nombre y la contraseña).
    filename = username + ".json"
    with open(filename, 'w') as f:
        json.dump(newUser, f, ensure_ascii = False, indent = 4)
    accreditFunction()

#Función para iniciar sesión.
def loginFunction():
    os.system("cls")
    os.chdir("C:\\BCrypt\\users")
    username = input("Introduce tu nombre de usuario: ")
    if not os.path.isfile(username + ".json"):
        os.system("cls")
        print("El usuario no existe, pulse intro para volver al menú.")
        input()
        accreditFunction()
        
    else:
        fileName = username + ".json"
        jsonToRead = open(fileName, "r")
        jsonData = jsonToRead.read()
        obj = json.loads(jsonData)
        nameOfUser = str(obj[username]["name"]) #NOTE TO SEF: Take a look on this, no utility btw.
        passwordOfUser = str(obj[username]["password"])

        password = input("Introduce tu contraseña: ")
        if password == passwordOfUser:
            mainFunction()
        else:
            print("La contraseña es incorrecta, pulse intro para volver al menú.")
            input()
            accreditFunction()

#Esta es la funcion principal tras realizar el primer inicio en el cual se crean los directorios necesarios para funcionar.
def accreditFunction():
    os.system("cls")
    print("Selecciona una opción para comenzar:")
    print("1. Iniciar sesión")
    print("2. Crear usuario")
    print("3. Salir")
    print(" ")
    option = input("Selecciona una opción: ")

    if option == "1":
        loginFunction()
    elif option == "2":
        createUser()
    elif option == "3":
        print("Gracias por utilizar BCrypt. Hasta pronto!")
        quit()
    elif option == "adminconsole":
        adminConsole()
    else:
        os.system("cls")
        print("No has seleccionado ninguna opción válida, pulse intro para volver al menú.")
        input()
        accreditFunction()

#TODO: You'd better create something for this...
#TODO: Try to go from ASCII to BINARY and then, invert the array to finally pass to hexadecimal.

def encryptFunction():
    stringToConvert = input("Enter a string to convert: ")
    result = ' '.join(format(ord(x), 'b') for x in stringToConvert)
    array = result.split()
    array.reverse()
    print(array)
    #converts array into string
    arrayInResult = ''.join(array)
    print(arrayInResult)
    input()
    mainFunction()

def decryptFunction():
    print("This is the decrypt function")

def mainFunction():
    os.system("cls")
    print("Bienvenido a BCrypt!")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3. Salir")
    print(" ")

    option = input("Selecciona una opción: ")

    if option == "1":
        encryptFunction()
    elif option == "2":
        decryptFunction()
    elif option == "3":
        accreditFunction()
    else:
        os.system("cls")
        print("No has seleccionado ninguna opción válida, pulse intro para volver al menú.")
        input()
        mainFunction()

performFirstStart()