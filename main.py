from funcions import *

print("Bienvenido")
while True:
    menuPrincipal()
    opc=pedirOpcion()
    match opc:
        case "1":
            primGemelos()
        case "2":
            primPalindromicos()
        case "3":
            print("Saliendo...")
            break
        case _: 
            print("Ingrese una opciòn valida")
