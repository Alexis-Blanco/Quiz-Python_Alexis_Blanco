
def menuPrincipal():
    menues="""
    ******Bienvenido al menú principal********
    1.Encontrar numeros primos gemelos
    2.Encontrar numeros primos palindromicos
    3.Recibir ayuda sobre el uso del programa
    4.Salir
    ******************************************
    """
    print(menues)

def pedirOpcion():
       while True:
             try:
                   opc=input("Seleccione una opción (1,2,3,4): ")
                   if opc not in ["1", "2", "3", "4"] :                         
                         raise ValueError("Por favor ingresa una opción inválida (1,2,3). ")
                   return opc
             except ValueError as e:
                   print(e)

def es_primo(n):
      if n < 2:
            return False
      for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                  return False
      return True

def es_palindromo(n):
      return str(n) == str(n)[::-1]

