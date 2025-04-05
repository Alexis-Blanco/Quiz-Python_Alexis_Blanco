
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

def pedir_rango():
      while True:
            try:
                  inicio= int(input("Introduce el valor de inicio del rango (número positivo mayor que 0): "))
                  final= int(input("Introduce el valor final del rango (número positivo mayor que 0): "))
                  if inicio <= 0 or final < 0:
                        raise ValueError("Los valores deben ser positivos y mayores que 0.")
                  if inicio >= final:
                        raise ValueError("El valor de inicio no puede ser mayor o igual que el valor final.")
                  if final > 10000:
                        raise ValueError("El valor final debe ser menor o igual a 10,000 para evitar tiempos de ejecución largos.")
                  return inicio, final
            except ValueError as e:
                  print(e)

def find_primos_gemelos(inicio, final):
      primos_gemelos = []
      for num in range(inicio, final +1):
            if es_primo(num) and es_primo(num + 2):
                  primos_gemelos.append((num, num + 2))
      return primos_gemelos

def generate_primos_gemelos(inicio, final):
      primos_gemelos = find_primos_gemelos(inicio, final)
      print("Los números primos gemelos en el rango son:", primos_gemelos)

def find_primos_palindromos(inicio, final):
      primos_palindromos =[]
      for num in range(inicio, final + 1):
            if es_primo(num) and es_palindromo(num):
                  primos_palindromos.append(num)
      return primos_palindromos

def generate_primos_palindromos(inicio, final):
      primos_palindromos = find_primos_palindromos(inicio, final)
      print("Los números primos palíndromos en el rango son:", primos_palindromos)

def mostrar_ayuda():
      ayuda ="""
      Este programa te permite encontrar números primos gemelos y palindromos dentro de un rango de tu elección.
      1. Selecciona '1' para encontrar números primos gemelos.
      2. Selecciona '2' para encontrar números primos palindromos.
      3. Selecciona '3' para recibir ayuda sobre el uso del programa.
      4. Selecciona '4' para salir del programa.
      5. Cuando te pida el rango, introue dos números enteros positivos.
      """
      print(ayuda)
      
           