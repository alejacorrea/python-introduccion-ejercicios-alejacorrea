# ejercicio_05.py
#
# Titulo: Multiplos de 5
#
# Descripcion:
# Pide un numero y si es multiplo de 5, imprime Es multiplo de 5.
#
# Requisitos:
# 1. Pedir un numero al usuario usando input() y convertirlo a int
# 2. Verificar si el numero es multiplo de 5 usando el operador modulo (%)
# 3. Un numero es multiplo de 5 si al dividirlo entre 5 el resultado es 0
# 4. Usar condicional para validad
# 5. Mostrar el mensaje correspondiente con print()
#
# Ejemplo de Entrada:
# Ingresa un numero: 25
#
# Ejemplo de Salida Esperada:
# Es multiplo de 5

# Paso 1: Pedir un numero al usuario
numero = int(input("Ingresa un numero: "))
# Paso 2 y 3: Verificar si el numero es multiplo de 5 usando el operador modulo (%)
if numero % 5 == 0:
    print("Es multiplo de 5")  
else:    print("No es multiplo de 5")
# Paso 4 y 5: Usar condicional para validad y mostrar el mensaje correspondiente con print() (ya se hizo en el paso anterior)