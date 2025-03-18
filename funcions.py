numeros=[]
def menuPrincipal():
    menues="""
    ******Bienvenido al menú principal********
    1.Encontrar numeros primos gemelos
    2.Encontrar numeros primos palindromicos
    3.Salir
    *****************************
    """
    print(menues)

def pedirOpcion():
       return input("Por favor elija una opción correcta: ")

def primGemelos():
    dividir=0
    Rangemayor=int(input("Por favor ingrese el numero limite del rango de busqueda deseada: "))
    indice=1
    if Rangemayor>2:
        for i in range(2, Rangemayor):
            if i%2==0 and i!=2: 
                dividir+=1
            elif i%3==0 and i!=3:
                dividir+=1
            elif i%5==0 and i!=5:
                dividir+=1
            elif i%7==0 and i!=7:
                dividir+=1
            elif i%9==0 and i!=9:
                dividir+=1            
            if dividir==0:
                    numeros.append(i)
            dividir=0
        for numero in numeros:
              if numero==numeros[-1]:
                    print('**')
              elif numeros[indice]-numero==2:
                    print(f"({numero},{numeros[indice]})")
              indice+=1
        numeros.clear()

