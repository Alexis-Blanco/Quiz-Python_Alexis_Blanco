
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

def es_primo(n):
      if n < 2:
            return False
      for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                  return False
      return True

