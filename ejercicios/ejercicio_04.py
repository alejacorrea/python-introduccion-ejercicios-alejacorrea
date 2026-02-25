# ejercicio_04.py
#
# Titulo: Calculadora de edad en días
#
# Descripcion:
# Crear una programa que le pregunte al usuario cuantos años tiene
# y luego calcular cuantos días ha vivido aproximadamente
# Cada año tiene 365 días
#
# Requisitos:
# 1. ingresar la edad usando input()
# 2. Convertir ese valor a numero entero con int()
# 3. Multiplicar la edad por 365 para sacar los días
# 4. Mostrar el resultador con print() y un f-string
#
# Ejemplo de Entrada:
# ¿Cuantos años tienes?: 22
#
# Ejemplo de Salida Esperada:
# Has vivido 8030 días aproximadamente

# Paso 1: ingresar la edad usando input()
edad = int(input("¿Cuantos años tienes?: "))
# Paso 2: Convertir ese valor a numero entero con int() (ya se hizo en el paso anterior)
# Paso 3: Multiplicar la edad por 365 para sacar los días  
dias_vividos = edad * 365
# Paso 4: Mostrar el resultador con print() y un f-string
print(f"Has vivido {dias_vividos} días aproximadamente")


