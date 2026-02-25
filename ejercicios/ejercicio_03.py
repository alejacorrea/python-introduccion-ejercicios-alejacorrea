# ejercicio_03.py
#
# Titulo: Calculadora promedio de notas
#
# Descripcion:
# Realizar un programa que calcule el promedio de notas de un estudiante.
# 
# Requisitos:
# 1. Pedir tres notas con decimales
# 2. Sumar las tres notas
# 3. Dividir la suma entre 3 para sacar el promedio
# 4. Mostrar el promedio
#
# Ejemplo de entrada:
# Primera nota: 4.5
# Segunda nota: 3.8
# Tercera nota: 4.2
#
# Ejemplo de Salida Esperada:
# Su promedio es de: 4.17

# Paso 1: Pedir tres notas con decimales
nota1 = float(input("Ingrese la primera nota: "))  
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
# Paso 2: Sumar las tres notas
suma_notas = nota1 + nota2 + nota3 
# Paso 3: Dividir la suma entre 3 para sacar el promedio
promedio = suma_notas / 3
# Paso 4: Mostrar el promedio
print(f"Su promedio es de: {promedio:.2f}")

