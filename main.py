from funcions import *

while True:
    menuPrincipal()
    opc=pedirOpcion()
    match opc:
        case "1":
            inicio, final = pedir_rango()
            generate_primos_gemelos(inicio, final)
        case "2":
            inicio, final = pedir_rango()
            generate_primos_palindromos(inicio, final)
        case "3":
            mostrar_ayuda()
        case "4":
            print("Saliendo del programa...")
            break
