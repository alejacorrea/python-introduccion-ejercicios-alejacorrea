# ejercicio_06.py
# 
# Titulo: Contador de letras en una palabra
#
# Descripcion:
# Crear un programa que cuente las letras de una palabra ingresada por el usuario
# 
# Requisitos:
# 1. Pedir al usuario que ingrese una palabra usando input()
# 2. Usar la funcion len() para contar cuantos caracteres tiene la palabra
# 3. Guardar el resultado en una variable (cantidad_letras)
# 4. Mostrar el resultado con print() usando un f-string
#
# Ejemplo de Entrada:
# Ingresa una palabra: Programación
#
# Ejemplo de Salida Esperada:
# La palabra "Programación" tiene 12 letras

# Paso 1: Pedir al usuario que ingrese una palabra usando input()
palabra = input("Ingresa una palabra: ")
# Paso 2: Usar la funcion len() para contar cuantos caracteres tiene la palabra
cantidad_letras = len(palabra)
# Paso 3: Guardar el resultado en una variable (cantidad_letras) (ya se hizo en el paso anterior)
# Paso 4: Mostrar el resultado con print() usando un f-string
print(f'La palabra "{palabra}" tiene {cantidad_letras} letras')
