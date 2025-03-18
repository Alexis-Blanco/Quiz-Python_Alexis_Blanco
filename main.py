from funcions import menuPrincipal, primGemelos, numeros, pedirOpcion

print("Bienvenido")
while True:
    menuPrincipal()
    opc=pedirOpcion()
    if opc=="1":
        primGemelos()
    elif opc=="2":
        print ("Bucar números palindrónomos")
    elif opc=="3":
        print("Saliendo...")
        break
    else: print("Ingrese una opciòn valida")
